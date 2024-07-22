from sqlalchemy import (
    Column, Integer, String, ForeignKey, Date, DECIMAL,
    Table, MetaData, UniqueConstraint
    )
from sqlalchemy.orm import DeclarativeBase

metadata = MetaData()

# Define tables using Table construct
customer_table = Table(
    "Customer", metadata,
    Column("Customer_id", Integer, primary_key=True),
    Column("Fname", String(100)),
    Column("Lname", String(100)),
    Column("Email", String(100)),
    Column("Phone_num", String(15)),
    Column("Street_address", String(255)),
    Column("City", String(100)),
    Column("State", String(50)),
    UniqueConstraint("Customer_id", name="Customer_pk")
    )

location_table = Table(
    "Location", metadata,
    Column("Location_id", Integer, primary_key=True),
    Column("Street_address", String(255)),
    Column("City", String(100)),
    Column("State", String(50)),
    UniqueConstraint("Location_id", name="Location_pk")
    )

position_type_table = Table(
    "Position_type", metadata,
    Column("Position_name", String(50), primary_key=True),
    Column("Hourly_wage", DECIMAL(10, 2)),
    Column("Salary", DECIMAL(20, 2)),
    UniqueConstraint("Position_name", name="Position_type_pk")
    )

employee_table = Table(
    "Employee", metadata,
    Column("Employee_id", Integer, primary_key=True),
    Column("Fname", String(100)),
    Column("Lname", String(100)),
    Column("Start_date", Date),
    Column("Position_name", String(50), ForeignKey('Position_type.Position_name')),
    UniqueConstraint("Employee_id", name="Employee_pk")
    )

transaction_table = Table(
    "Transaction", metadata,
    Column("Transaction_id", Integer, primary_key=True),
    Column("Location_id", Integer, ForeignKey('Location.Location_id')),
    Column("Customer_id", Integer, ForeignKey('Customer.Customer_id')),
    Column("Employee_id", Integer, ForeignKey('Employee.Employee_id')),
    Column("Transaction_amount", DECIMAL(10, 2)),
    UniqueConstraint("Transaction_id", name="Transaction_pk")
    )

vendor_table = Table(
    "Vendor", metadata,
    Column("Vendor_id", Integer, primary_key=True),
    Column("Vendor_name", String(255)),
    UniqueConstraint("Vendor_id", name="Vendor_pk")
    )

inventory_table = Table(
    "Inventory", metadata,
    Column("Item_id", Integer, primary_key=True),
    Column("Vendor_id", Integer, ForeignKey('Vendor.Vendor_id'), primary_key=True),
    Column("Quantity", Integer),
    Column("Item_name", String(255)),
    UniqueConstraint("Item_id", "Vendor_id", name="Inventory_pk")
    )

works_at_table = Table(
    "Works_at", metadata,
    Column("Location_id", Integer, ForeignKey('Location.Location_id'), primary_key=True),
    Column("Employee_id", Integer, ForeignKey('Employee.Employee_id'), primary_key=True),
    UniqueConstraint("Location_id", "Employee_id", name="Works_at_pk")
    )


class Base(DeclarativeBase):
    pass


# Map classes to tables and specify primary keys using __mapper_args__
class Customer(Base):
    __table__ = customer_table
    __mapper_args__ = {"primary_key": [customer_table.c.Customer_id]}

class Location(Base):
    __table__ = location_table
    __mapper_args__ = {"primary_key": [location_table.c.Location_id]}

class PositionType(Base):
    __table__ = position_type_table
    __mapper_args__ = {"primary_key": [position_type_table.c.Position_name]}

class Employee(Base):
    __table__ = employee_table
    __mapper_args__ = {"primary_key": [employee_table.c.Employee_id]}

class Transaction(Base):
    __table__ = transaction_table
    __mapper_args__ = {"primary_key": [transaction_table.c.Transaction_id]}

class Vendor(Base):
    __table__ = vendor_table
    __mapper_args__ = {"primary_key": [vendor_table.c.Vendor_id]}

class Inventory(Base):
    __table__ = inventory_table
    __mapper_args__ = {"primary_key": [inventory_table.c.Item_id, inventory_table.c.Vendor_id]}

class WorksAt(Base):
    __table__ = works_at_table
    __mapper_args__ = {"primary_key": [works_at_table.c.Location_id, works_at_table.c.Employee_id]}

class Classes:
    def __init__(self):
        self.Customer = Customer
        self.Location = Location
        self.Position_type = PositionType
        self.Employee = Employee
        self.Transaction = Transaction
        self.Vendor = Vendor
        self.Inventory = Inventory
        self.Works_at = WorksAt

        def __getitem__(self, key):
            return getattr(self, key)

class Tables:
    def __init__(self):
        self.Customer = customer_table
        self.Location = location_table
        self.Position_type = position_type_table
        self.Employee = employee_table
        self.Transaction = transaction_table
        self.Vendor = vendor_table
        self.Inventory = inventory_table
        self.Works_at = works_at_table

        def __getitem__(self, key):
            return getattr(self, key)
class Map:
    def __init__(self):
        self.metadata = metadata
        self.classes = Classes()
        self.tables = Tables()
        self.base = Base
        self.engine = None
    def connect(self, engine):
        self.engine = engine