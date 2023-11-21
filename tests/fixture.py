"""
I can't get fixture to work well with parameterized test, so just create some constants here
"""

from pathlib import Path

QUESTION = "question.py"
CHALLENGES_DIR = Path(__file__).parent.parent / "challenges"
ALL_QUESTIONS = list(CHALLENGES_DIR.glob("**/question.py"))
ALL_SOLUTIONS = list(CHALLENGES_DIR.glob("**/solution.py"))
