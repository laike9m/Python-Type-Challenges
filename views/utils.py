import os
import glob
from dataclasses import dataclass
from enum import IntEnum
from pathlib import Path
from typing import TypeAlias, Literal
from typing_extensions import DefaultDict

import libcst as cst
from mypy import api


ROOT_DIR = Path(__file__).parent.parent


ChallengeName: TypeAlias = str
difficulty_to_order = {"basic": 0, "intermediate": 1, "advanced": 2}


@dataclass
class Challenge:
    name: ChallengeName
    difficulty: str
    code: str
    display_order: int


def load_challenges() -> dict[ChallengeName, Challenge]:
    challenges = {}
    for filename in glob.glob(f"{ROOT_DIR}/challenges/*/question.py"):
        dir_name = os.path.basename(os.path.dirname(filename))
        difficulty, challenge_name = dir_name.split("-")
        with open(filename, "r") as file:
            code = file.read()
        challenges[challenge_name] = Challenge(
            name=challenge_name,
            difficulty=difficulty,
            display_order=difficulty_to_order[difficulty],
            code=code,
        )

    return challenges


@dataclass
class PreprocessResult:
    error: str | None = None
    code_should_pass_type_check: str | None = None
    code_should_fail_type_check: str | None = None


def preprocess_code(code: str) -> PreprocessResult:
    try:
        module = cst.parse_module(code)
    except cst.ParserSyntaxError as e:
        return PreprocessResult(
            error=f'<b style="color:red;">Your code has syntax error(s):</b>\n\n{e.message}'
        )
    return PreprocessResult(
        code_should_pass_type_check=trim_function_from_code(module, "should_fail"),
        code_should_fail_type_check=trim_function_from_code(module, "should_pass"),
    )


def trim_function_from_code(module: cst.Module, func_name: str) -> str:
    # TODO: replace with empty lines to keep lineno unchanged.
    class RemoveShouldFailTransformer(cst.CSTTransformer):
        def leave_FunctionDef(self, original_node, updated_node):
            if original_node.name.value == func_name:
                return cst.RemoveFromParent()
            return updated_node

    modified_module = module.visit(RemoveShouldFailTransformer())
    return modified_module.code


@dataclass
class TypeCheckResult:
    stdout: str
    stderr: str
    code: int


def type_check_with_mypy(code):
    raw_result = api.run(["--check-untyped-defs", "-c", code])
    return TypeCheckResult(
        stdout=raw_result[0], stderr=raw_result[1], code=raw_result[2]
    )
