from flask import Flask, jsonify, abort, request
from flask.ext.sqlalchemy import SQLAlchemy
from app.config import *
from models.db import db

def create_app(application_mode='config.DevelopmentConfig'):
    """ Application Factories
        http://flask.pocoo.org/docs/patterns/appfactories/
    """
    app = Flask(__name__)
    app.config.from_object(enviroment)


    db.init_app(app)

    return app

    =
