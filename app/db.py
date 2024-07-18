from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

# Initialize the database connection
db = SQLAlchemy()

def init_db(app):
    try:
        # Configure the SQLAlchemy part of the app instance
        app.config['SQLALCHEMY_DATABASE_URI'] = (
            'mysql+pymysql://databoss:3is3x6vL^405AOGf@databoss-database.czk2mm6e60xo.us-east-1.rds.amazonaws.com:3306/Walmart'
        )
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Bind the instance to the Flask app
        db.init_app(app)
        logging.info("Database connected successfully.")
        return db
    except Exception as e:
        logging.error("Failed to connect to the database.", exc_info=True)
        raise e
