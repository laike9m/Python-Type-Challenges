import platform

from flask import (
    Blueprint,
    jsonify,
    redirect,
    render_template,
    request,
)

from .challenge import challenge_manager, Level, ChallengeKey
from .sitemap import sitemapper

app_views = Blueprint("app_views", __name__)


@sitemapper.include(changefreq="daily", priority=1.0)
@app_views.route("/")
def index():
    return render_template(
        "index.html",
        challenges_groupby_level=challenge_manager.challenges_groupby_level,
    )


@sitemapper.include(
    changefreq="daily",
    priority=0.5,
    # https://github.com/h-janes/flask-sitemapper/wiki/Usage#dynamic-routes
    url_variables={
        "level": [c.level for c in challenge_manager.challenges.keys()],
        "name": [c.name for c in challenge_manager.challenges.keys()],
    },
)
@app_views.route("/<level>/<name>", methods=["GET"])
def get_challenge(level: str, name: str):
    challenge_key = ChallengeKey(Level(level), name)
    if not challenge_manager.has_challenge(challenge_key):
        return redirect("/")

    challenge = challenge_manager.get_challenge(challenge_key)
    return render_template(
        "challenge.html",
        name=name,
        level=challenge.level,
        challenges_groupby_level=challenge_manager.challenges_groupby_level,
        code_under_test=challenge.user_code,
        test_code=challenge.test_code,
        python_info=platform.python_version(),
    )


@app_views.route("/run/<level>/<name>", methods=["POST"])
def run_challenge(level: str, name: str):
    challenge_key = ChallengeKey(Level(level), name)
    code = request.get_data(as_text=True)

    result = challenge_manager.run_challenge(user_code=code, key=challenge_key)
    if result.passed:
        message = "<h2>✅ Congratulations! You passed the test 🎉</h2>"
        return jsonify({"passed": True, "message": message})

    error_message = "<h2>❌ Challenge failed 😢</h2>"
    error_message += f"<p>Error:\n{result.message}</p>"
    return jsonify({"passed": False, "message": error_message})
