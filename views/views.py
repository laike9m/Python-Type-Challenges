import ast
import platform
from functools import wraps

from flask import (
    abort,
    Blueprint,
    jsonify,
    redirect,
    render_template,
    request,
)

from .challenge import ChallengeKey, Level, challenge_manager
from .sitemap import sitemapper

app_views = Blueprint("app_views", __name__)


def validate_challenge(view_func):
    @wraps(view_func)
    def wrapper(level, name, *args, **kwargs):
        if Level.is_valid_level(level) and challenge_manager.has_challenge(
            ChallengeKey(Level(level), name)
        ):
            return view_func(level, name, *args, **kwargs)  # valid challenge
        abort(404)

    return wrapper


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
@validate_challenge
def get_challenge(level: str, name: str):
    challenge = challenge_manager.get_challenge(ChallengeKey(Level(level), name))
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
@validate_challenge
def run_challenge(level: str, name: str):
    code = request.get_data(as_text=True)
    try:
        ast.parse(code)
    except SyntaxError as e:
        return jsonify(
            {"passed": False, "message": f"😱 SyntaxError: {e.msg} (line {e.lineno})"}
        )

    result = challenge_manager.run_challenge(
        user_code=code, key=ChallengeKey(Level(level), name)
    )
    if result.passed:
        message = "<h2>✅ Congratulations! You passed the test 🎉</h2>"
        return jsonify(
            {"passed": True, "message": message, "debug_info": result.debug_info}
        )

    error_message = "<h2>❌ Challenge failed 😢</h2>"
    error_message += f"<p>Error:\n{result.message}</p>"
    return jsonify(
        {"passed": False, "message": error_message, "debug_info": result.debug_info}
    )


@app_views.route("/random", methods=["GET"])
def run_random_challenge():
    challenge = challenge_manager.get_random_challenge()
    return redirect(f"/{challenge['level']}/{challenge['name']}")
