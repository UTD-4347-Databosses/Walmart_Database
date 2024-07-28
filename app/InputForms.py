from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField, SelectField


'''
**************************************************************************************************
CUSTOMER SECTION *********************************************************************************
**************************************************************************************************
'''
#class CustomerInventoryForm(FlaskForm):





'''
**************************************************************************************************
EMPLOYEE SECTION *********************************************************************************
**************************************************************************************************
'''

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
                          default='Fname')

    Operation = SelectField('Operation', choices=[('add', 'Add Employee'), ('update', 'Update Employee'), ('delete', 'Delete Employee'), ('search', 'Search')])
    submit = SubmitField('Submit')

class EmployeeInventoryForm(FlaskForm):
    ID = StringField('Item ID')
    Name = StringField('Item Name')
    Vendor = StringField('Vendor ID')
    Quantity = StringField('Quantity')
    radio = RadioField('Search By',
                            choices=[('ID', 'Item ID'), ('Name', 'Item Name'), ('Vendor', 'Vendor ID')],
                            default='ID')
    Operation = SelectField('Operation', choices=[('add', 'Add Item'), ('update', 'Update Item'), ('delete', 'Delete Item'), ('search', 'Search')])
    submit = SubmitField('Submit')

class CustomerInventoryForm(FlaskForm):
    ID = StringField('Item ID')
    Name = StringField('Item Name')
    Quantity = StringField('Quantity')
    radio = RadioField('Search By',
                       choices=[('ID', 'Item ID'), ('Name', 'Item Name')],
                       default='name')
    Operation = SelectField('Operation', choices=[('add', 'Add Item'), ('update', 'Update Item'), ('delete', 'Delete Item'), ('search', 'Search')])
    submit = SubmitField('Submit')


'''
**************************************************************************************************
OTHER SECTION *********************************************************************************
**************************************************************************************************
'''
class SettingsForm(FlaskForm):
    role = RadioField('Role',
                      choices=[('customer', 'Customer'), ('employee', 'Employee'), ('vendor', 'Vendor')],
                      default='customer')
    submit = SubmitField('Submit')


class AdminResetForm(FlaskForm):
    # Multiple choice, if all is selected, then the rest of the fields are greyed out
    options = RadioField('Options',
                         choices=[('reset_all', 'Reset All'),
                                  ('reset_customers', 'Reset Customers'),
                                  ('reset_employees', 'Reset Employees'),
                                  ('reset_vendors', 'Reset Vendors')],
                         default='reset_all')
    submit = SubmitField('Submit')


class AdminPopulateForm(FlaskForm):
    # Multiple choice, if all is selected, then the rest of the fields are greyed out
    options = RadioField('Options',
                         choices=[('populate_all', 'Populate All'),
                                  ('populate_customers', 'Populate Customers'),
                                  ('populate_employees', 'Populate Employees'),
                                  ('populate_vendors', 'Populate Vendors')],
                         default='populate_all')
    submit = SubmitField('Submit')
