from pathlib import Path

import pytest
from werkzeug.test import TestResponse
from app import app
from .fixture import ALL_QUESTIONS


@pytest.mark.parametrize("question_file", ALL_QUESTIONS, ids=lambda x: x.parent.name)
def test_get_challenge(question_file: Path):
    level, challenge_name = question_file.parent.name.split("-", maxsplit=1)
    response = app.test_client().get(f"/{level}/{challenge_name}")

    # Verify the returned HTML contains a challenge's source code
    assert "TODO" in response.text


@pytest.mark.parametrize("question_file", ALL_QUESTIONS, ids=lambda x: x.parent.name)
def test_run_challenge(question_file: Path):
    level, challenge_name = question_file.parent.name.split("-", maxsplit=1)
    response = app.test_client().post(f"run/{level}/{challenge_name}", data="")

    # Verify backend can run type check and return results
    assert response.json is not None
