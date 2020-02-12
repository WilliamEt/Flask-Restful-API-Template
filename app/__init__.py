# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_map

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    db.init_app(app)

    from .api_1_0 import api_1_0 as api_bp
    app.register_blueprint(api_bp, url_prefix="/api/v1.0")

    return app

