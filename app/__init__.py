from flask import Flask

from app.db import init_db


def create_app():
    app = Flask(__name__)

    # Initialize the database
    db = init_db(app)


    from . import routes
    app.register_blueprint(routes.bp)

    return app
