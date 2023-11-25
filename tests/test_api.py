from pathlib import Path

from flask.testing import FlaskClient


def test_get_challenge(test_client: FlaskClient, question_file: Path):
    level, challenge_name = question_file.parent.name.split("-", maxsplit=1)
    response = test_client.get(f"/{level}/{challenge_name}")

    # Verify the returned HTML contains a challenge's source code
    assert "TODO" in response.text


def test_run_challenge(test_client: FlaskClient, question_file: Path):
    level, challenge_name = question_file.parent.name.split("-", maxsplit=1)
    response = test_client.post(f"run/{level}/{challenge_name}", data="")

    # Verify backend can run type check and return results
    assert response.json is not None


def test_invalid_challenge_redirect_to_homepage(test_client: FlaskClient):
    response = test_client.get("/foo/bar")
    assert response.status_code == 302
    assert response.location == "/"
