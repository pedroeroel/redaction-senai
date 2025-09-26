from app.app import create_app
import os

app = create_app()

if __name__ == '__main__':
    if os.path.exists('instance/config.py'):
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        app.run()