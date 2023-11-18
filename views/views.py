import platform

from flask import Blueprint, jsonify, redirect, render_template, request

from .utils import challenge_manager

app_views = Blueprint("app_views", __name__)


@app_views.route("/")
def index():
    return render_template(
        "index.html",
        challenges_groupby_level=challenge_manager.challenges_groupby_level,
    )


@app_views.route("/challenges/<name>", methods=["GET"])
def get_challenge(name: str):
    if not challenge_manager.has_challenge(name):
        return redirect("/")

    challenge = challenge_manager.get_challenge(name)
    return render_template(
        "challenge.html",
        name=name,
        challenges_groupby_level=challenge_manager.challenges_groupby_level,
        code_under_test=challenge.user_code,
        test_code=challenge.test_code,
        python_info=platform.python_version(),
    )


@app_views.route("/run/<name>", methods=["POST"])
def run_challenge(name: str):
    code = request.get_data(as_text=True)

    result = challenge_manager.run_challenge(user_code=code, name=name)
    if result.passed:
        message = "<h2>✅ Congratulations! You passed the test 🎉</h2>"
        return jsonify({"passed": True, "message": message})

    error_message = "<h2>❌ Challenge failed 😢</h2>"
    error_message += f"<p>Error:\n{result.message}</p>"
    return jsonify({"passed": False, "message": error_message})
