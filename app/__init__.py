import os
import random

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

from dotenv import load_dotenv

from flask import Flask

from app.db import init_db


def create_app():
    load_dotenv(".env")
    app = Flask(__name__)
    FLASK_SQLALCHEMY_DATABASE_URI = (os.environ['FLASK_SQLALCHEMY_DATABASE_FLAVOR'] +
                               '://' + os.environ['FLASK_SQLALCHEMY_DATABASE_USERNAME'] +
                               ':' + os.environ['FLASK_SQLALCHEMY_DATABASE_PASSWORD'] +
                               '@' + os.environ['FLASK_SQLALCHEMY_DATABASE_HOSTNAME'] +
                               ':' + os.environ['FLASK_SQLALCHEMY_DATABASE_PORT'] +
                               '/' + os.environ['FLASK_SQLALCHEMY_DATABASE_NAME'])

    app.config['FLASK_SQLALCHEMY_DATABASE_URI'] = FLASK_SQLALCHEMY_DATABASE_URI
    app.config['FLASK_SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = os.environ['FLASK_SECRET_KEY']
    os.environ['FLASK_SESSION_ID'] = str(random.randint(0, 1000000))

    # Bootstrap-Flask requires this line
    bootstrap = Bootstrap5(app)
    # Flask-WTF requires this line
    csrf = CSRFProtect(app)
    csrf.init_app(app)

    # Initialize the database
    db = init_db(app)


    from . import routes
    app.register_blueprint(routes.bp)

    return app
