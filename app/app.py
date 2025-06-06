from flask import Flask, Blueprint
from flask_cors import CORS
from app.routes.main.routes import main
from app.routes.auth.routes import auth

def create_app():

    sources = {r"/*": {"origins": "*"}}

    app = Flask(__name__)

    CORS(app, resources=sources)

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app