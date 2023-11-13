from flask import Flask, redirect

from views import views

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static",
)
app.register_blueprint(views.app_views)


@app.errorhandler(404)
def page_not_found(e):
    return redirect("/")
