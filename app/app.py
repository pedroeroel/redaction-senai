from flask import Flask, Blueprint
from flask_cors import CORS
from app.routes.main.routes import main

def create_app():

    sources = {r"/*": {"origins": "*"}}

    app = Flask(__name__)

    CORS(app, resources=sources)

    app.register_blueprint(main)

    return app