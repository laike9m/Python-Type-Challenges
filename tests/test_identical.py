"""
Make sure all test codes in questions and solutions are identical.
"""

from pathlib import Path

from views.challenge import Challenge, Level


def test_identical(solution_file: Path, question: str):
    level, challenge_name = solution_file.parent.name.split("-", maxsplit=1)
    with solution_file.open() as f:
        solution_code = f.read()
    solution_test = Challenge(
        name=challenge_name, level=Level(level), code=solution_code
    ).test_code

    question_file = solution_file.parent / question
    with question_file.open() as f:
        question_code = f.read()
    question_test = Challenge(
        name=challenge_name, level=Level(level), code=question_code
    ).test_code
    assert solution_test.strip() == question_test.strip()
