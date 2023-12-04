"""
Make sure all questions fail type check.
"""

from pathlib import Path

import pytest

from views.challenge import ChallengeManager


def test_solution_valid(question_file: Path):
    # Skip the challenges whose question can't fail type check no matter how many tests are added.
    if question_file.parent.name == "basic-any":
        pytest.skip(f"Skipping test: {question_file}")

    with question_file.open() as f:
        code = f.read()
    result = ChallengeManager._type_check_with_pyright(user_code="", test_code=code)

    assert not result.passed, result
