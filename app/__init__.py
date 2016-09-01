from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from app.config import *
from app.models.db import db
from app.api.tag import bp as api_tag

def create_app(application_mode='config.DevelopmentConfig'):
    """ Application Factories
        http://flask.pocoo.org/docs/patterns/appfactories/
    """
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    app.register_blueprint(api_tag)
    db = SQLAlchemy()
    db.init_app(app)
    return app
