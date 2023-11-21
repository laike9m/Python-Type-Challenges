"""
Make sure all solutions type check.
"""

from pathlib import Path

import pytest

from views.challenge import ChallengeManager
from .fixture import ALL_SOLUTIONS


@pytest.mark.parametrize("solution_file", ALL_SOLUTIONS, ids=lambda x: x.parent.name)
def test_solution_valid(solution_file: Path):
    with solution_file.open() as f:
        code = f.read()
    result = ChallengeManager._type_check_with_pyright(user_code="", test_code=code)
    assert result.passed, result.message
