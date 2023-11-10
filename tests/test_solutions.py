from pathlib import Path

import pytest

from views.utils import ChallengeManager

CHALLENGES_DIR = Path(__file__).parent.parent / "challenges"
ALL_SOLUTIONS = list(CHALLENGES_DIR.glob("**/solution.py"))


@pytest.mark.parametrize("solution_file", ALL_SOLUTIONS, ids=lambda x: x.parent.name)
def test_solution_valid(solution_file: Path):
    with solution_file.open() as f:
        code = f.read()
    result = ChallengeManager._type_check_with_pyright(user_code="", test_code=code)
    assert result.passed, result.message
