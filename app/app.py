import os
import dotenv
from flask import Flask
from flask_cors import CORS

# Import Blueprints
from app.routes.main.routes import main
from app.routes.auth.routes import auth
from app.routes.essay.routes import essay
from app.routes.games.routes import games
from app.routes.classes.routes import classes
from app.routes.admin.routes import admin

def create_app():
    app = Flask(__name__)

    # --- Configuration Loading Logic ---
    secret_key = None
    import_source = None

    # 1. Try loading from instance/config.py
    try:
        from instance.config import SECRET_KEY as config_key
        if config_key:
            secret_key = config_key
            import_source = 'instance.config'
    except (ImportError, AttributeError):
        pass

    # 2. If not found, try loading from .env / Environment Variables
    if secret_key is None:
        try:
            dotenv.load_dotenv()
            env_key = os.getenv('SECRET_KEY')
            if env_key:
                secret_key = env_key
                import_source = '.env'
        except Exception:
            pass

    # 3. Apply key or fallback to default
    if secret_key:
        app.secret_key = secret_key
        print(f'SECRET_KEY imported from: {import_source}')
    else:
        print('Error importing SECRET_KEY from config or dotenv. Using default unsafe value.')
        app.secret_key = "adm@adm"

    # --- CORS Configuration ---
    # Allow all origins for all routes (Use specific origins in production)
    sources = {r"/*": {"origins": "*"}}
    CORS(app, resources=sources)

    # --- Register Blueprints ---
    blueprints = [main, auth, essay, games, classes, admin]
    for bluep in blueprints:
        app.register_blueprint(bluep)

    return app