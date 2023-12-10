"""
Make sure all questions fail type check.
"""

from pathlib import Path

import pytest

from views.challenge import ChallengeManager


def test_solution_valid(question_file: Path):
    with question_file.open() as f:
        code = f.read()
    result = ChallengeManager._type_check_with_pyright(user_code="", test_code=code)

    assert not result.passed, result
