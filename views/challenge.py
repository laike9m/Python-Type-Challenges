import io
import random
import re
import subprocess
import tempfile
import tokenize
from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path
from typing import ClassVar, Optional, TypeAlias

ROOT_DIR = Path(__file__).parent.parent


class Level(StrEnum):
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXTREME = "extreme"

    @classmethod
    def is_valid_level(cls, level: str):
        return level in cls._value2member_map_


ChallengeName: TypeAlias = str


@dataclass(frozen=True)
class ChallengeKey:
    level: Level
    name: ChallengeName

    @classmethod
    def from_str(cls, key: str):
        """Create a key object form a string like "basic-foo"."""
        level, name = key.split("-", maxsplit=1)
        return cls(Level(level), name)


@dataclass
class Challenge:
    """A challenge object.

    :param hints: An optional string of hints, use markdown syntax.
    """

    CODE_SPLITTER: ClassVar[str] = "\n## End of your code ##\n"

    name: ChallengeName
    level: Level
    code: str
    user_code: str = field(default="", init=False)
    test_code: str = field(default="", init=False)
    hints: Optional[str] = None

    def __post_init__(self):
        self.parse_code()

    def parse_code(self):
        self.user_code, _, self.test_code = self.code.partition(self.CODE_SPLITTER)


@dataclass(frozen=True, slots=True)
class TypeCheckResult:
    message: str
    passed: bool
    debug_info: dict = field(default_factory=dict)  # For debugging purposes


class ChallengeManager:
    """The manager for challenges.

    :param root_dir: The root directory that contains the files of challenges,
        use "{PROJECT_ROOT}/challenges" by default.
    """

    def __init__(self, root_dir: Optional[Path] = None):
        if not root_dir:
            root_dir = ROOT_DIR / "challenges"
        self.challenges: dict[ChallengeKey, Challenge] = self._load_challenges(root_dir)
        self.challenges_groupby_level: dict[Level, list[ChallengeName]]
        self.challenges_groupby_level = self._get_challenges_groupby_level()

    def has_challenge(self, key: ChallengeKey) -> bool:
        return key in self.challenges

    def get_challenge(self, key: ChallengeKey) -> Challenge:
        return self.challenges[key]

    def get_challenge_cnt(self) -> int:
        """Get the count of challenges."""
        return len(self.challenges)

    def run_challenge(self, key: ChallengeKey, user_code: str) -> TypeCheckResult:
        challenge = self.get_challenge(key)
        # Make sure user code ends with a new line to avoid issue #63.
        return self._type_check_with_pyright(user_code + "\n", challenge.test_code)

    def get_random_challenge(self) -> dict[str, str]:
        level = random.choice(list(self.challenges_groupby_level.keys()))
        name = random.choice(self.challenges_groupby_level[level])
        return {"level": level, "name": name}

    @staticmethod
    def _load_challenges(root_dir: Path) -> dict[ChallengeKey, Challenge]:
        challenges = {}
        for challenge_folder in root_dir.iterdir():
            question_source = challenge_folder / "question.py"
            if not question_source.exists():
                continue

            # Try to read the optional hints file
            hints_file = challenge_folder / "hints.md"
            if hints_file.exists():
                hints = hints_file.read_text().strip()
            else:
                hints = None

            key = ChallengeKey.from_str(challenge_folder.name)
            challenges[key] = Challenge(
                name=key.name,
                level=key.level,
                code=question_source.read_text(),
                hints=hints,
            )
        return challenges

    def _get_challenges_groupby_level(self) -> dict[Level, list[ChallengeName]]:
        groups: dict[str, list[ChallengeName]] = {}

        for challenge in self.challenges.values():
            groups.setdefault(challenge.level, []).append(challenge.name)

        # Sort challenge by name alphabetically.
        for challenge_names in groups.values():
            challenge_names.sort()

        # Make sure groups are ordered by level (from easy to hard)
        return {level: groups.get(level, []) for level in Level}

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
            )
            stdout, stderr = raw_result.stdout, raw_result.stderr
            if stderr:
                return TypeCheckResult(message=stderr, passed=False)
        error_lines: list[str] = []

        # Substract lineno in merged code by lineno_delta, so that the lineno in
        # error message matches those in the test code editor. Fixed #20.
        lineno_delta = len(user_code.splitlines())
        for line in stdout.splitlines():
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
