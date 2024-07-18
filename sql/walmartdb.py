from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.query import Query
from app.db import db

class Customer(db.Model):
	__tablename__ = 'Customer'
	Customer_id = db.Column(db.Integer, primary_key=True, nullable=False)
	Fname = db.Column(db.String(45), nullable=True)
	Lname = db.Column(db.String(45), nullable=True)
