"""
Make sure all questions fail type check.
"""

from pathlib import Path

import pytest

from views.challenge import ChallengeManager

CHALLENGES_DIR = Path(__file__).parent.parent / "challenges"
ALL_QUESTIONS = list(CHALLENGES_DIR.glob("**/question.py"))


@pytest.mark.parametrize("question_file", ALL_QUESTIONS, ids=lambda x: x.parent.name)
def test_solution_valid(question_file: Path):
    test_id = question_file.parent.name

    # TODO: remove "advanced-generic-param" once fixed
    # Skip the challenges whose question can't fail type check no matter how many tests are added.
    if test_id in ("basic-any"):
        pytest.skip(f"Skipping test: {question_file}")

    with question_file.open() as f:
        code = f.read()
    result = ChallengeManager._type_check_with_pyright(user_code="", test_code=code)

    assert not result.passed, result
