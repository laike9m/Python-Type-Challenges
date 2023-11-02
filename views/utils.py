import glob
import io
import os
import re
import tokenize
from dataclasses import dataclass, field
from pathlib import Path
from typing import TypeAlias

from mypy import api

ROOT_DIR = Path(__file__).parent.parent
MYPY_CONFIG = ROOT_DIR / "pyproject.toml"


ChallengeName: TypeAlias = str
CODE_SPLITTER = "\n## End of your code ##\n"
EXPECT_ERROR_COMMENT = "expect-type-error"

MYPY_MESSAGE_REGEX = r"^(?:.+?):(\d+):(\s*error:.+)$"


@dataclass
class Challenge:
    name: ChallengeName
    difficulty: str
    code: str
    user_code: str = field(default="", init=False)
    fixture_code: str = field(default="", init=False)

    def __post_init__(self):
        self.parse_code()

    def parse_code(self):
        self.user_code, _, self.fixture_code = self.code.partition(CODE_SPLITTER)


@dataclass(frozen=True, slots=True)
class ChallengeInfo:
    name: str
    difficulty: str


@dataclass(frozen=True, slots=True)
class TypeCheckResult:
    stdout: str
    stderr: str
    passed: bool


class ChallengeManager:
    def __init__(self):
        self.challenges = self._load_challenges()
        self.challenge_names = [
            ChallengeInfo(name=name, difficulty=c.difficulty)
            for name, c in self.challenges.items()
        ]

    def has_challenge(self, name: str) -> bool:
        return name in self.challenges

    def get_challenge(self, name: str) -> Challenge:
        return self.challenges[name]

    def run_challenge(self, name: str, user_code: str) -> TypeCheckResult:
        challenge = self.get_challenge(name)
        code = f"{user_code}\n{challenge.fixture_code}"
        buffer = io.StringIO(code)
        tokens = list(tokenize.generate_tokens(buffer.readline))
        expect_error_lines = [
            token.start[0]
            for token in tokens
            if token.type == tokenize.COMMENT
            and token.string[1:].strip() == EXPECT_ERROR_COMMENT
        ]
        raw_result = self._type_check_with_mypy(code)
        mypy_outputs: list[str] = []

        for line in raw_result.stdout.splitlines():
            m = re.match(MYPY_MESSAGE_REGEX, line)
            if m is None:
                continue
            line_number = int(m.group(1))
            message = m.group(2)
            if line_number in expect_error_lines:
                expect_error_lines.remove(line_number)
                continue
            mypy_outputs.append(f"{line_number}:{message}")

        if expect_error_lines:
            for line_number in expect_error_lines:
                mypy_outputs.append(f"Expected type error on line: {line_number}")

        passed = len(mypy_outputs) == 0
        if passed:
            mypy_outputs.append("\nAll tests passed")
        else:
            mypy_outputs.append(f"\nFound {len(mypy_outputs)} errors")
        return TypeCheckResult(
            stdout="\n".join(mypy_outputs), stderr=raw_result.stderr, passed=passed
        )

    @staticmethod
    def _load_challenges() -> dict[ChallengeName, Challenge]:
        challenges = {}
        for filename in glob.glob(f"{ROOT_DIR}/challenges/*/question.py"):
            dir_name = os.path.basename(os.path.dirname(filename))
            difficulty, challenge_name = dir_name.split("-", maxsplit=1)
            with open(filename, "r") as file:
                code = file.read()
            challenges[challenge_name] = Challenge(
                name=challenge_name,
                difficulty=difficulty,
                code=code,
            )

        return challenges

    @staticmethod
    def _type_check_with_mypy(code: str) -> TypeCheckResult:
        raw_result = api.run(["--config-file", str(MYPY_CONFIG), "-c", code])
        return TypeCheckResult(
            stdout=raw_result[0], stderr=raw_result[1], passed=raw_result[2] == 0
        )


challenge_manager = ChallengeManager()
