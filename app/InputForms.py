from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField, SelectField


class EmployeeCustomerForm(FlaskForm):
    Fname = StringField('First Name')
    Lname = StringField('Last Name')
    ID = StringField('Customer ID')
    Email = StringField('Email')
    Phone = StringField('Phone')
    Address = StringField('Address')
    City = StringField('City')
    State = StringField('State')
    radio = RadioField('Search By',
                          choices=[('Fname', 'First Name'), ('Lname', 'Last Name'), ('ID', 'Customer ID')],
                          default='name')
    Operation = SelectField('Operation', choices=[('add', 'Add Customer'), ('update', 'Update Customer'), ('delete', 'Delete Customer'), ('search', 'Search')])
    submit = SubmitField('Submit')

class EmployeeViewForm(FlaskForm):
    Fname = StringField('First Name')
    Lname = StringField('Last Name')
    ID = StringField('Employee ID')
    Date = StringField('Start Date')
    Position = StringField('Position')
    radio = RadioField('Search By',
                          choices=[('Fname', 'First Name'), ('Lname', 'Last Name'), ('ID', 'Employee ID'),
                                    ('Date', 'Start Date'), ('Position', 'Position')],
                          default='name')
    Operation = SelectField('Operation', choices=[('add', 'Add Employee'), ('update', 'Update Employee'), ('delete', 'Delete Employee'), ('search', 'Search')])
    submit = SubmitField('Submit')

class EmployeeInventoryForm(FlaskForm):
    ID = StringField('Item ID')
    Name = StringField('Item Name')
    Vendor = StringField('Vendor ID')
    Quantity = StringField('Quantity')
    radio = RadioField('Search By',
                            choices=[('ID', 'Item ID'), ('Name', 'Item Name'), ('Vendor', 'Vendor ID')],
                            default='name')
    Operation = SelectField('Operation', choices=[('add', 'Add Item'), ('update', 'Update Item'), ('delete', 'Delete Item'), ('search', 'Search')])
    submit = SubmitField('Submit')

class SettingsForm(FlaskForm):
    role = RadioField('Role',
                     choices=[('customer', 'Customer'), ('employee', 'Employee'), ('vendor', 'Vendor')],
                     default='customer')
    submit = SubmitField('Submit')
