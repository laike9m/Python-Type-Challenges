import os
from collections import namedtuple
from flask import Blueprint, render_template, request, redirect
import libcst as cst

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
        code_under_test=challenge.code_under_test,
        test_code=challenge.test_code,
    )


@app_views.route("/run/<name>", methods=["POST"])
def run_challenge(name) -> str:
    code = request.get_data(as_text=True)
    try:
        module = cst.parse_module(code)
    except cst.ParserSyntaxError as e:
        return (
            f'<b style="color:red;">Your code has syntax error(s):</b>\n\n{e.message}'
        )

    result_should_pass, result_should_fail = challenge_manager.run_challenge(
        code_under_test=code, name=name
    )
    print(result_should_fail)
    if result_should_pass.passed and not result_should_fail.passed:
        return "<h2>✅ Congratulations! You completed the challenge 🎉</h2>"

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
