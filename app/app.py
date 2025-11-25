from flask import Flask, Blueprint, session
from flask_cors import CORS
from app.routes.main.routes import main
from app.routes.auth.routes import auth
from app.routes.essay.routes import essay
from app.routes.games.routes import games
from app.routes.classes.routes import classes
from app.routes.admin.routes import admin


def create_app():

    blueprints = [main, auth, essay, games, classes, admin]
    sources = {r"/*": {"origins": "*"}}

    app = Flask(__name__)
    app.secret_key = 'adm@adm'

    CORS(app, resources=sources)

    for bluep in blueprints:
        app.register_blueprint(bluep)

    return app