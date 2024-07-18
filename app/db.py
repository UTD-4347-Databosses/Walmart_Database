import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import logging

db = SQLAlchemy()
Base = automap_base()

def init_db(app):
    global db
    global Base
    try:
        # Configure the SQLAlchemy part of the app instance
        FLASK_SQLALCHEMY_DATABASE_URI = (os.environ['FLASK_SQLALCHEMY_DATABASE_FLAVOR'] +
                                         '://' + os.environ['FLASK_SQLALCHEMY_DATABASE_USERNAME'] +
                                         ':' + os.environ['FLASK_SQLALCHEMY_DATABASE_PASSWORD'] +
                                         '@' + os.environ['FLASK_SQLALCHEMY_DATABASE_HOSTNAME'] +
                                         ':' + os.environ['FLASK_SQLALCHEMY_DATABASE_PORT'] +
                                         '/' + os.environ['FLASK_SQLALCHEMY_DATABASE_NAME'])

        app.config['SQLALCHEMY_DATABASE_URI'] = FLASK_SQLALCHEMY_DATABASE_URI
        app.config['FLASK_SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        app.config['FLASK_SQLALCHEMY_ECHO'] = True

        # Bind the instance to the Flask app

    except Exception as e:
        logging.error("Failed to connect to the database.", exc_info=True)
        raise e
    finally:
        with app.app_context():
            db.init_app(app)
            Base.prepare(db.engine, reflect=True)
            logging.info("Database connected successfully.")
            return db
