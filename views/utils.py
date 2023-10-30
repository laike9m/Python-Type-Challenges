import os
import glob
from dataclasses import dataclass
from enum import IntEnum
from pathlib import Path
from typing import TypeAlias, Literal
from typing_extensions import DefaultDict

import libcst as cst
from libcst.metadata import MetadataWrapper, WhitespaceInclusivePositionProvider
from mypy import api


ROOT_DIR = Path(__file__).parent.parent


ChallengeName: TypeAlias = str


@dataclass
class Challenge:
    name: ChallengeName
    difficulty: str
    code: str
    code_under_test: str = ""
    test_code: str = ""
    test_code_should_pass: str = ""
    test_code_should_fail: str = ""

    def __post_init__(self):
        self.parse_code()

    def parse_code(self):
        start_lineno = 0
        module = cst.parse_module(self.code)
        challenge = self

        class RemoveTargetFunctionTransformer(cst.CSTTransformer):
            METADATA_DEPENDENCIES = (WhitespaceInclusivePositionProvider,)

            def visit_FunctionDef(self, node: cst.FunctionDef):
                if node.name.value == "should_pass":
                    challenge.test_code_should_pass = module.code_for_node(node)
                    test_start_lineno = self.get_metadata(
                        WhitespaceInclusivePositionProvider, node
                    ).start.line
                    code_lines = challenge.code.split(os.linesep)
                    challenge.code_under_test = os.linesep.join(
                        code_lines[:test_start_lineno]
                    )
                    challenge.test_code = os.linesep.join(
                        code_lines[test_start_lineno + 1 :]
                    )
                if node.name.value == "should_fail":
                    challenge.test_code_should_fail = module.code_for_node(node)

        wrapper = MetadataWrapper(module)
        modified_module = wrapper.visit(RemoveTargetFunctionTransformer())


@dataclass
class ChallengeInfo:
    name: str
    difficulty: str


@dataclass
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

    # returns (result_should_pass, result_should_fail)
    def run_challenge(
        self, name: str, code_under_test: str
    ) -> tuple[TypeCheckResult, TypeCheckResult]:
        challenge = self.get_challenge(name)
        code_should_pass_type_check = code_under_test + challenge.test_code_should_pass
        code_should_fail_type_check = code_under_test + challenge.test_code_should_fail
        return (
            self._type_check_with_mypy(code_should_pass_type_check),
            self._type_check_with_mypy(code_should_fail_type_check),
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
    def _type_check_with_mypy(code) -> TypeCheckResult:
        raw_result = api.run(["--check-untyped-defs", "-c", code])
        return TypeCheckResult(
            stdout=raw_result[0], stderr=raw_result[1], passed=raw_result[2] == 0
        )


challenge_manager = ChallengeManager()
