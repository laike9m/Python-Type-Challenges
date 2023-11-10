import glob
import io
import os
import re
import subprocess
import tempfile
import tokenize
from collections import OrderedDict
from dataclasses import dataclass, field
from enum import StrEnum
from functools import lru_cache
from pathlib import Path
from typing import ClassVar, Literal, TypeAlias, get_args, cast

ROOT_DIR = Path(__file__).parent.parent


ChallengeName: TypeAlias = str


class Level(StrEnum):
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXTREME = "extreme"


LEVELs = [l.value for l in Level]


@dataclass
class Challenge:
    CODE_SPLITTER: ClassVar[str] = "\n## End of your code ##\n"

    name: ChallengeName
    level: Level
    code: str
    user_code: str = field(default="", init=False)
    test_code: str = field(default="", init=False)

    def __post_init__(self):
        self.parse_code()

    def parse_code(self):
        self.user_code, _, self.test_code = self.code.partition(self.CODE_SPLITTER)


@dataclass(frozen=True, slots=True)
class ChallengeInfo:
    name: ChallengeName
    level: Level


@dataclass(frozen=True, slots=True)
class TypeCheckResult:
    message: str
    passed: bool


class ChallengeManager:
    def __init__(self):
        self.challenges = self._load_challenges()
        self.challenge_names = [
            ChallengeInfo(name=name, level=c.level)
            for name, c in self.challenges.items()
        ]

    @property
    @lru_cache
    def challenges_groupby_level(self) -> dict[Level, list[ChallengeName]]:
        groups = {}

        for challenge in self.challenge_names:
            groups.setdefault(challenge.level, []).append(challenge.name)

        # Sort name alphabetically
        for names in groups.values():
            names.sort()

        # Use OrderedDict to keep the order of the level
        return OrderedDict([(level, groups[level]) for level in LEVELs])

    def has_challenge(self, name: str) -> bool:
        return name in self.challenges

    def get_challenge(self, name: str) -> Challenge:
        return self.challenges[name]

    def run_challenge(self, name: str, user_code: str) -> TypeCheckResult:
        challenge = self.get_challenge(name)
        return self._type_check_with_pyright(user_code, challenge.test_code)

    @staticmethod
    def _load_challenges() -> dict[ChallengeName, Challenge]:
        challenges = {}
        for filename in glob.glob(f"{ROOT_DIR}/challenges/*/question.py"):
            dir_name = os.path.basename(os.path.dirname(filename))
            level, challenge_name = dir_name.split("-", maxsplit=1)
            with open(filename, "r") as file:
                code = file.read()
            challenges[challenge_name] = Challenge(
                name=challenge_name,
                level=Level(level),
                code=code,
            )

        return challenges

    EXPECT_ERROR_COMMENT = "expect-type-error"

    # Pyright error messages look like:
    # `<filename>:<line_no>:<col_no> - <error|warning|information>: <message>`
    # Here we only capture the error messages and line numbers
    PYRIGHT_MESSAGE_REGEX = r"^(?:.+?):(\d+):[\s\-\d]+(error:.+)$"

    @classmethod
    def _type_check_with_pyright(
        cls, user_code: str, test_code: str
    ) -> TypeCheckResult:
        code = f"{user_code}{test_code}"
        buffer = io.StringIO(code)

        # This produces a stream of TokenInfos, example:
        # TokenInfo(type=4 (NEWLINE), string='\n', start=(4, 3), end=(4, 4), line='"""\n'),
        # TokenInfo(type=62 (NL), string='\n', start=(5, 0), end=(5, 1), line='\n')
        # See https://docs.python.org/3/library/tokenize.html#tokenize.tokenize for more details
        tokens = list(tokenize.generate_tokens(buffer.readline))

        # Find all lines that are followed by a comment # expect-type-error
        expect_error_line_numbers = [
            token.start[0]
            for token in tokens
            if token.type == tokenize.COMMENT
            and token.string[1:].strip() == cls.EXPECT_ERROR_COMMENT
        ]
        # Tracks whether an expected error has been reported by type checker.
        error_line_seen_in_err_msg: dict[int, bool] = {
            lineno: False for lineno in expect_error_line_numbers
        }

        with tempfile.NamedTemporaryFile(suffix=".py") as temp:
            temp.write(code.encode())
            temp.flush()
            # TODO: switch to json output to simplify output parsing.
            # https://microsoft.github.io/pyright/#/command-line?id=json-output
            raw_result = subprocess.run(
                ["pyright", "--pythonversion", "3.12", temp.name],
                capture_output=True,
                text=True,
            ).stdout
        error_lines: list[str] = []

        # Substract lineno in merged code by lineno_delta, so that the lineno in
        # error message matches those in the test code editor. Fixed #20.
        lineno_delta = len(user_code.splitlines())
        for line in raw_result.splitlines():
            m = re.match(cls.PYRIGHT_MESSAGE_REGEX, line)
            if m is None:
                continue
            line_number, message = int(m.group(1)), m.group(2)
            if line_number in error_line_seen_in_err_msg:
                # Each reported error should be attached to a specific line,
                # If it is commented with # expect-type-error, let it pass.
                error_line_seen_in_err_msg[line_number] = True
                continue
            # Error could be thrown from user code too, in which case delta shouldn't be applied.
            error_lines.append(
                f"{line_number if line_number <= lineno_delta else line_number - lineno_delta}:{message}"
            )

        # If there are any lines that are expected to fail but not reported by pyright,
        # they should be considered as errors.
        for line_number, seen in error_line_seen_in_err_msg.items():
            if not seen:
                error_lines.append(
                    f"{line_number - lineno_delta}: error: Expected type error but instead passed"
                )

        passed = len(error_lines) == 0
        if passed:
            error_lines.append("\nAll tests passed")
        else:
            error_lines.append(f"\nFound {len(error_lines)} errors")

        return TypeCheckResult(message="\n".join(error_lines), passed=passed)


challenge_manager = ChallengeManager()
