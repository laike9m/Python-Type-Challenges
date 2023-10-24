from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views.app_views)
