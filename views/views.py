import platform

from flask import Blueprint, redirect, render_template, request

from .utils import challenge_manager

app_views = Blueprint("app_views", __name__)


@app_views.route("/")
def index():
    return render_template(
        "index.html", challenge_names=challenge_manager.challenge_names
    )


@app_views.route("/challenges/<name>", methods=["GET"])
def get_challenge(name):
    if not challenge_manager.has_challenge(name):
        return redirect("/")

    challenge = challenge_manager.get_challenge(name)
    return render_template(
        "challenge.html",
        name=name,
        challenge_names=challenge_manager.challenge_names,
        code_under_test=challenge.user_code,
        test_code=challenge.test_code,
        python_info=platform.python_version(),
    )


@app_views.route("/run/<name>", methods=["POST"])
def run_challenge(name):
    code = request.get_data(as_text=True)

    result = challenge_manager.run_challenge(user_code=code, name=name)
    if result.passed:
        return "<h2>✅ Congratulations! You completed the challenge 🎉</h2>"

    error_message = "<h2>❌ Challenge failed 😢</h2>"
    error_message += f"<p>Error:\n{result.stdout}{result.stderr}</p>"
    return error_message
