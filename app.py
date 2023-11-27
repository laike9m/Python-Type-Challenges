import threading
from flask import Flask, redirect, request, send_from_directory
from typing import cast

from views import views, challenge
from views.sitemap import sitemapper

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static",
)
app.register_blueprint(views.app_views)
sitemapper.init_app(app)


@app.errorhandler(404)
def page_not_found(e):
    return redirect("/")


@app.route("/robots.txt")
def robots_txt():
    return send_from_directory(cast(str, app.static_folder), request.path[1:])


@app.route("/sitemap.xml")
def r_sitemap():
    return sitemapper.generate()


print("sss")

# Temporary solution for
# https://github.com/laike9m/Python-Type-Challenges/issues/49
threading.Thread(
    target=challenge.challenge_manager.run_challenge,
    kwargs={
        "key": challenge.ChallengeKey(challenge.Level("basic"), "any"),
        "user_code": "",
    },
).start()
