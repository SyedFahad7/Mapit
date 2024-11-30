from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['UPLOAD_FOLDER'] = 'static/uploads'
    app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 * 1024  # Limit uploads to 2 GB

    # Register Blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
