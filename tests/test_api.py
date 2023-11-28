from pathlib import Path

from flask.testing import FlaskClient

from views.challenge import ChallengeKey, Level, challenge_manager


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


def test_run_code_with_syntax_error(test_client: FlaskClient):
    response = test_client.post(f"run/basic/any", data="""class A::""")
    assert response.json == {
        "message": "😱 SyntaxError: invalid syntax (line 1)",
        "passed": False,
    }


def test_invalid_challenge_redirect_to_homepage(test_client: FlaskClient):
    response = test_client.get("/foo/bar")
    assert response.status_code == 302
    assert response.location == "/"


def test_get_random_challenge(test_client: FlaskClient):
    response = test_client.get("/random")
    assert response.status_code == 302
    level, challenge_name = response.location[1:].split("/")
    assert Level.is_valid_level(level)
    assert challenge_manager.has_challenge(ChallengeKey(Level(level), challenge_name))
