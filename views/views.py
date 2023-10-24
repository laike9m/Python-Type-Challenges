from flask import Blueprint, render_template, request

from .utils import (
    load_challenges,
    type_check_with_mypy,
    trim_function_from_code,
    preprocess_code,
)

app_views = Blueprint("app_views", __name__)
challenges = load_challenges()


@app_views.route("/")
def hello(name=None):
    return render_template("index.html")


@app_views.route("/challenges/<name>", methods=["GET"])
def get_challenge(name):
    return render_template("challenge.html", code=challenges[name])


@app_views.route("/run", methods=["POST"])
def run_challenge():
    code_should_pass_type_check, code_should_fail_type_check = preprocess_code(
        request.get_data(as_text=True)
    )
    result_should_pass = type_check_with_mypy(code_should_pass_type_check)
    result = (
        "❌ challenge failed"
        if result_should_pass.code != 0
        else "✅ challenge completed"
    )
    message = (
        f"<b>should_pass</b>\n{result_should_pass.stdout}{result_should_pass.stderr}"
    )

    result_should_fail = type_check_with_mypy(code_should_fail_type_check)
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
