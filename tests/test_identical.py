"""
Make sure all test codes in questions and solutions are identical.
"""

from pathlib import Path

from views.challenge import Challenge, Level


def test_identical(solution_file: Path):
    def get_test_code(path: Path):
        TEST_SPLITTER = "\n## End of test code ##\n"
        level, challenge_name = path.parent.name.split("-", maxsplit=1)

        with solution_file.open() as f:
            challenge_code = f.read()
        challenge = Challenge(
            name=challenge_name, level=Level(level), code=challenge_code
        )

        return challenge.test_code.partition(TEST_SPLITTER)[0]

    solution_test = get_test_code(solution_file)
    question_test = get_test_code(solution_file.parent / "question.py")

    assert solution_test.strip() == question_test.strip()
