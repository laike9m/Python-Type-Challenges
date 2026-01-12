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


@pytest.fixture()
def assets_dir() -> Path:
    """
    Path to the test assets directory located alongside this file.
    
    Returns:
        Path: Path to the "assets" directory adjacent to this conftest.py file.
    """
    return Path(__file__).parent / "assets"


@pytest.fixture()
def mgr(assets_dir: Path):
    """
    Create a ChallengeManager for the "challenges" subdirectory of the provided assets directory.
    
    Parameters:
        assets_dir (Path): Path to the test assets directory containing challenge data.
    
    Returns:
        ChallengeManager: Instance initialized with `assets_dir / "challenges"`.
    """
    return ChallengeManager(assets_dir / "challenges")


@pytest.fixture()
def test_client() -> FlaskClient:
    """
    Create a Flask test client for the application.
    
    Returns:
        test_client (FlaskClient): A test client bound to the application for issuing HTTP requests in tests.
    """
    return app.test_client()


@pytest.fixture(params=ALL_QUESTIONS, ids=lambda x: x.parent.name)
def question_file(request):
    return request.param


@pytest.fixture(params=ALL_SOLUTIONS, ids=lambda x: x.parent.name)
def solution_file(request):
    return request.param