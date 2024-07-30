import csv
import os

from sqlalchemy import MetaData

from sqlalchemy import Column, Integer, String, ForeignKey, Date, DECIMAL, PrimaryKeyConstraint
from sqlalchemy.ext.automap import automap_base
from flask_sqlalchemy import SQLAlchemy
from sql.WalmartDB import Map, Base
import logging

db = SQLAlchemy()
map = Map()



def init_db(app):
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

		db.init_app(app)

		logging.info("Database connected successfully.")
		return db

	except Exception as e:
		logging.error("Failed to connect to the database.", exc_info=True)
		raise e


def reset_customers():
	db.session.query(map.classes.Customer).delete()
	db.session.commit()
	logging.info("Customers table reset successfully.")


def reset_employees():
	db.session.query(map.classes.Employee).delete()
	db.session.commit()
	logging.info("Employees table reset successfully.")


def reset_vendors():
	db.session.query(map.classes.Vendor).delete()
	db.session.commit()
	logging.info("Vendors table reset successfully.")


def reset_inventory():
	db.session.query(map.classes.Inventory).delete()
	db.session.commit()
	logging.info("Inventory table reset successfully.")


def reset_locations():
	db.session.query(map.classes.Location).delete()
	db.session.commit()
	logging.info("Locations table reset successfully.")


def reset_position_types():
	db.session.query(map.classes.Position_type).delete()
	db.session.commit()
	logging.info("Position types table reset successfully.")


def reset_transactions():
	db.session.query(map.classes.Transaction).delete()
	db.session.commit()
	logging.info("Transaction table reset successfully.")


def reset_works_at():
	db.session.query(map.classes.Works_at).delete()
	db.session.commit()
	logging.info("Works at table reset successfully.")


def reset_all():
	reset_customers()
	reset_employees()
	reset_inventory()
	reset_vendors()
	reset_locations()
	reset_position_types()
	reset_transactions()
	reset_works_at()


def reinit_db(file="./sql/setup.sql"):
	reset_all()
	with open(file, 'r') as f:
		sql = f.read()
	db.session.execute(sql)
	logging.info("Database reset successfully.")


def populate_customers(file="./data/Customer.csv"):
	reader = csv.reader(open(file, 'r'))
	next(reader)
	for row in reader:
		if db.session.query(db.session.query(map.classes.Customer.Customer_id).filter(
				map.classes.Customer.Customer_id == row[0]).exists()).scalar():
			continue
		db.session.add(map.classes.Customer(Customer_id=row[0],
		                                    Fname=row[1],
		                                    Lname=row[2],
		                                    Email=row[3],
		                                    Phone_num=row[4],
		                                    Street_address=row[5],
		                                    City=row[6],
		                                    State=row[7]))
		db.session.commit()
	logging.info("Database populated with customers successfully.")


def populate_employees(file="./data/Employee.csv"):
	reader = csv.reader(open(file, 'r'))
	next(reader)
	for row in reader:
		if db.session.query(db.session.query(map.classes.Employee.Employee_id).filter(
				map.classes.Employee.Employee_id == row[0]).exists()).scalar():
			continue
		db.session.add(map.classes.Employee(Employee_id=row[0],
		                                    Fname=row[1],
		                                    Lname=row[2],
		                                    Start_date=row[3],
		                                    Position_name=row[4]))
		db.session.commit()
	logging.info("Database populated with employees successfully.")


def populate_inventory(file="./data/Inventory.csv"):
	reader = csv.reader(open(file, 'r'))
	next(reader)
	for row in reader:
		if db.session.query(db.session.query(map.classes.Inventory.Item_id).filter(
				map.classes.Inventory.Item_id == row[0]).exists()).scalar():
			continue
		db.session.add(map.classes.Inventory(Item_id=row[0],
		                                     Vendor_id=row[1],
		                                     Quantity=row[2],
		                                     Item_name=row[3]))
		db.session.commit()
	logging.info("Database populated with inventory successfully.")


def populate_locations(file="./data/Location.csv"):
	reader = csv.reader(open(file, 'r'))
	next(reader)
	for row in reader:
		if db.session.query(db.session.query(map.classes.Location.Location_id).filter(
				map.classes.Location.Location_id == row[0]).exists()).scalar():
			continue
		db.session.add(map.classes.Location(Location_id=row[0],
		                                    Street_address=row[1],
		                                    City=row[2],
		                                    State=row[3]))
		db.session.commit()
	logging.info("Database populated with locations successfully.")


def populate_position_types(file="./data/Position_type.csv"):
	reader = csv.reader(open(file, 'r'))
	next(reader)
	for row in reader:
		if db.session.query(db.session.query(map.classes.Position_type.Position_name).filter(
				map.classes.Position_type.Position_name == row[0]).exists()).scalar():
			continue
		db.session.add(map.classes.Position_type(Position_name=row[0],
		                                        Hourly_wage=row[1],
		                                        Salary=row[2]))
		db.session.commit()


def populate_transactions(file="./data/Transaction.csv"):
	reader = csv.reader(open(file, 'r'))
	next(reader)
	for row in reader:
		if db.session.query(db.session.query(map.classes.Transaction.Transaction_id).filter(
				map.classes.Transaction.Transaction_id == row[0]).exists()).scalar():
			continue
		db.session.add(map.classes.Transaction(Transaction_id=row[0],
		                                       Location_id=row[1],
		                                       Customer_id=row[2],
		                                       Employee_id=row[3],
		                                       Transaction_amount=row[4]))
	logging.info("Database populated with Transaction successfully.")


def populate_vendors(file="./data/Vendor.csv"):
	reader = csv.reader(open(file, 'r'))
	next(reader)
	for row in reader:
		if db.session.query(db.session.query(map.classes.Vendor.Vendor_id).filter(
				map.classes.Vendor.Vendor_id == row[0]).exists()).scalar():
			continue
		db.session.add(map.classes.Vendor(Vendor_id=row[0],
		                                  Vendor_name=row[1]))
		db.session.commit()
	logging.info("Database populated with vendors successfully.")


def populate_works_at(file="./data/Works_at.csv"):
	reader = csv.reader(open(file, 'r'))
	next(reader)
	for row in reader:
		if db.session.query(db.session.query(map.classes.Works_at.Location_id).filter(
				map.classes.Works_at.Location_id == row[0],
				map.classes.Works_at.Employee_id == row[1]).exists()).scalar():
			continue
		db.session.add(map.classes.Works_at(Location_id=row[0],
		                                    Employee_id=row[1]))
		db.session.commit()
	logging.info("Database populated with works_at successfully.")


def populate_all():
	populate_vendors()
	populate_inventory()
	populate_position_types()
	populate_customers()
	populate_employees()
	populate_locations()
	populate_transactions()
	populate_works_at()
	logging.info("Database populated successfully.")
