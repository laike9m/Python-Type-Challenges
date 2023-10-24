import os
import glob
from mypy import api
from pathlib import Path
from dataclasses import dataclass

import libcst as cst


ROOT_DIR = Path(__file__).parent.parent


def load_challenges():
    challenge_dict = {}
    for filename in glob.glob(f"{ROOT_DIR}/challenges/*/code.py"):
        dir_name = os.path.basename(os.path.dirname(filename))
        key = dir_name.split("-")[1]
        with open(filename, "r") as file:
            content = file.read()
        challenge_dict[key] = content

    return challenge_dict


def preprocess_code(code: str) -> tuple[str, str]:
    code_should_pass_type_check = trim_function_from_code(code, "should_fail")
    code_should_fail_type_check = trim_function_from_code(code, "should_pass")
    return code_should_pass_type_check, code_should_fail_type_check


def trim_function_from_code(code: str, func_name: str) -> str:
    module = cst.parse_module(code)

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
