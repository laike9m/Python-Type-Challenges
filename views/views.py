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
challenge_list = [(name, c.display_order) for name, c in challenges.items()]


@app_views.route("/")
def index():
    return render_template("index.html")


@app_views.route("/challenges/<name>", methods=["GET"])
def get_challenge(name):
    return (
        render_template(
            "challenge.html", challenge_names=challenge_list, code=challenges[name].code
        )
        if name in challenges
        else redirect("/")
    )


@app_views.route("/run", methods=["POST"])
def run_challenge() -> str:
    preprocess_result = preprocess_code(code=request.get_data(as_text=True))
    if preprocess_result.error:
        return preprocess_result.error

    result_should_pass = type_check_with_mypy(
        preprocess_result.code_should_pass_type_check
    )
    result = (
        "❌ challenge failed"
        if result_should_pass.code != 0
        else "✅ challenge completed"
    )
    message = (
        f"<b>should_pass</b>\n{result_should_pass.stdout}{result_should_pass.stderr}"
    )

    result_should_fail = type_check_with_mypy(
        preprocess_result.code_should_fail_type_check
    )
    if result_should_fail.code == 0:
        message += "\n\n<b>should_fail</b>\nType check should fail but passed."
        result = "❌ challenge failed"
    else:
        message += (
            f"\n\n<b>should_fail</b><br>"
            + result_should_fail.stdout
            + result_should_fail.stderr
        )

    print(f"{result_should_pass} \n {result_should_fail}")

    return f"{result}\n\n{message}"
