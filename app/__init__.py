from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml
import os

db = SQLAlchemy()

def load_config():
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def create_app(config_name='development'):
    app = Flask(__name__)
    config = load_config()
    app.config['SECRET_KEY'] = config['app']['secret_key']
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{config['database']['name']}"
    app.config['SQLALCHEMY_ECHO'] = config['database']['echo']
    db.init_app(app)
    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    return app
