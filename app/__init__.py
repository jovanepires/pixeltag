from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from app.config import *

from app.api.tag import bp as api_tag

def create_app(application_mode='config.DevelopmentConfig'):
    """ Application Factories
        http://flask.pocoo.org/docs/patterns/appfactories/
    """
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    app.register_blueprint(api_tag)

    from app.models.db import db
    db.init_app(app)

    with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run...
        db.create_all()

    return app
