"""
In `conftest.py` we define fixtures that are used in multiple tests. pytest will automatically
inject them into the test functions that need them by signature matching.
"""


from pathlib import Path

import pytest
from flask.testing import FlaskClient

from app import app
from views.challenge import ChallengeManager

CHALLENGES_DIR = Path(__file__).parent.parent / "challenges"
ALL_QUESTIONS = list(CHALLENGES_DIR.glob("**/question.py"))
ALL_SOLUTIONS = list(CHALLENGES_DIR.glob("**/solution*.py"))
ALL_HINTS = list(CHALLENGES_DIR.glob("**/hints.md"))


@pytest.fixture()
def assets_dir() -> Path:
    """The directory contains test assets."""
    return Path(__file__).parent / "assets"


@pytest.fixture()
def mgr(assets_dir: Path):
    return ChallengeManager(assets_dir / "challenges")


@pytest.fixture()
def test_client() -> FlaskClient:
    return app.test_client()


@pytest.fixture(params=ALL_QUESTIONS, ids=lambda x: x.parent.name)
def question_file(request):
    return request.param


@pytest.fixture(params=ALL_SOLUTIONS, ids=lambda x: x.parent.name)
def solution_file(request):
    return request.param


@pytest.fixture(params=ALL_HINTS, ids=lambda x: x.parent.name)
def hint_file(request) -> Path:
    return request.param
