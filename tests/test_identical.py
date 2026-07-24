"""
Make sure all test codes in questions and solutions are identical.
"""

from pathlib import Path

from views.challenge import Challenge, Level


def test_identical(solution_file: Path):
    """
    Checks that the test code embedded in the given solution file matches the test code in the corresponding question file.
    
    Reads the solution file to construct a Challenge object (using the solution file's parent directory name to derive level and challenge name), extracts each challenge's test code up to the marker "\n## End of test code ##\n", strips surrounding whitespace, and asserts the two extracted test code segments are equal.
    
    Parameters:
        solution_file (Path): Path to the solution file whose test code will be compared to the question file located at the same directory with name "question.py".
    """
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