"""
Make sure all solutions type check.
"""

from pathlib import Path

from views.challenge import ChallengeManager


def test_solution_valid(solution_file: Path):
    with solution_file.open() as f:
        code = f.read()
    result = ChallengeManager._type_check_with_pyright(user_code="", test_code=code)
    assert result.passed, result.message
