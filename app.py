from flask import Flask, redirect
from views import views

app = Flask(__name__)
app.register_blueprint(views.app_views)


@app.errorhandler(404)
def page_not_found(e):
    return redirect("/")
