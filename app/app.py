from flask import Flask, Blueprint
from flask_cors import CORS
from app.routes.main.routes import main
from app.routes.auth.routes import auth
from app.routes.essay.routes import essay

def create_app():

    sources = {r"/*": {"origins": "*"}}

    app = Flask(__name__)

    CORS(app, resources=sources)

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(essay)

    return app