from collections import namedtuple
from flask import Blueprint, render_template, request, redirect

from .utils import (
    load_challenges,
    type_check_with_mypy,
    trim_function_from_code,
    preprocess_code,
)

app_views = Blueprint("app_views", __name__)

# TODO: wrap this in a class.
challenges = load_challenges()
ChallengeInfo = namedtuple("ChallengeInfo", ["name", "difficulty"])
challenge_names = [
    ChallengeInfo(name=name, difficulty=c.difficulty) for name, c in challenges.items()
]


@app_views.route("/")
def index():
    print(challenge_names)
    return render_template("index.html", challenge_names=challenge_names)


@app_views.route("/challenges/<name>", methods=["GET"])
def get_challenge(name):
    return (
        render_template(
            "challenge.html",
            challenge_names=challenge_names,
            code=challenges[name].code,
        )
        if name in challenges
        else redirect("/")
    )


@app_views.route("/run", methods=["POST"])
def run_challenge() -> str:
    preprocess_result = preprocess_code(code=request.get_data(as_text=True))
    if preprocess_result.error:
        return preprocess_result.error  # e.g. syntax error

    result_should_pass = type_check_with_mypy(
        preprocess_result.code_should_pass_type_check
    )
    result_should_fail = type_check_with_mypy(
        preprocess_result.code_should_fail_type_check
    )
    if result_should_pass.passed and not result_should_fail.passed:
        return "<h2>✅ Congratulations! You completed the challenge 🎉</h2>"

    # Constructing error message.
    error_message = "<h2>❌ Challenge failed 😢\n\n</h2>"
    if not result_should_pass.passed:
        error_message += (
            '<b>Test case <code style="background-color: #FFFFCC;">should_pass</code>'
            " didn't pass type check.</b>"
            f"\nError:\n{result_should_pass.stdout}{result_should_pass.stderr}\n\n"
        )
    if result_should_fail.passed:
        error_message += (
            f'<b>Test case <code style="background-color: #FFFFCC;">should_fail</code>'
            " should fail type check, but it passed.</b>"
        )

    return error_message
