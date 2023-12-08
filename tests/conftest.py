"""
In `conftest.py` we define fixtures that are used in multiple tests. pytest will automatically
inject them into the test functions that need them by signature matching.
"""


import random
from pathlib import Path

import pytest
from app import app
from flask.testing import FlaskClient
from views.challenge import Challenge, Level

CHALLENGES_DIR = Path(__file__).parent.parent / "challenges"
ALL_QUESTIONS = list(CHALLENGES_DIR.glob("**/question.py"))
ALL_SOLUTIONS = list(CHALLENGES_DIR.glob("**/solution.py"))


@pytest.fixture()
def test_client() -> FlaskClient:
    return app.test_client()


@pytest.fixture(params=ALL_QUESTIONS, ids=lambda x: x.parent.name)
def question_file(request):
    return request.param


@pytest.fixture(params=ALL_SOLUTIONS, ids=lambda x: x.parent.name)
def solution_file(request):
    return request.param


@pytest.fixture()
def random_q_challenge():
    """Return a random challenge object from the questions poll."""
    file = random.choice(ALL_QUESTIONS)
    level, challenge_name = file.parent.name.split("-", maxsplit=1)
    return Challenge(name=challenge_name, level=Level(level), code=file.read_text())
