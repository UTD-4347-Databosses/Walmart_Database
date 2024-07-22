import os
import random

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap, Bootstrap5


from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

from dotenv import load_dotenv

from flask import Flask

from app.db import init_db



def create_app():
    # This is what hides the database credentials
    load_dotenv(".env")
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ['FLASK_SECRET_KEY']
    os.environ['FLASK_SESSION_ID'] = str(random.randint(0, 1000000))

    with app.app_context():
        csrf = CSRFProtect(app)
        csrf.init_app(app)
        bootstrap = Bootstrap(app)
        init_db(app)


    from . import routes
    app.register_blueprint(routes.bp)

    return app
