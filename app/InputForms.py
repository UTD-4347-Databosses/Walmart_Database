from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField, SelectField


'''
**************************************************************************************************
CUSTOMER SECTION *********************************************************************************
**************************************************************************************************
'''


class CustomerInventoryForm(FlaskForm):
    ID = StringField('Item ID')
    Name = StringField('Item Name')
    Price = StringField('Price')
    radio = RadioField('Search By',
                       choices=[('ID', 'Item ID'), ('Name', 'Item Name'), ('Price', 'Price')],
                       default='ID')
    Operation = SelectField('Operation', choices=[('search', 'Search')])
    submit = SubmitField('Submit')

class CustomerTransactionForm(FlaskForm):
    TransactionID = StringField('Transaction ID')
    CustomerID = StringField('Customer ID')
    EmployeeID = StringField('Employee ID')
    LocationID = StringField('Location ID')
    TransactionAmount = StringField('Transaction Amount')
    radio = RadioField('Search By',
                    choices=[('TransactionID', 'Transaction ID'), ('CustomerID', 'Customer ID'), ('EmployeeID', 'Employee ID'), ('LocationID', 'Location ID'), ('TransactionAmount', 'Transaction Amount')],
                       default='TransactionID')
    Operation = SelectField('Operation', choices=[('search', 'Search')])
    submit = SubmitField('Submit')



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
                          default='Fname')
    Operation = SelectField('Operation', choices=[('add', 'Add Customer'), ('update', 'Update Customer'), ('delete', 'Delete Customer'), ('search', 'Search')])
    submit = SubmitField('Submit')


class EmployeeViewForm(FlaskForm):
    Fname = StringField('First Name')
    Lname = StringField('Last Name')
    ID = StringField('Employee ID')
    Date = StringField('Start Date')
    Position = StringField('Position')
    Salary = StringField('Salary')
    Hourly = StringField('Hourly')
    radio = RadioField('Search By',
                          choices=[('Fname', 'First Name'), ('Lname', 'Last Name'), ('ID', 'Employee ID'),
                                    ('Date', 'Start Date'), ('Position', 'Position'), ('Salary', 'Salary'), ('Hourly', 'Hourly')],
                          default='Fname')

    Operation = SelectField('Operation', choices=[('add', 'Add Employee'), ('update', 'Update Employee'), ('delete', 'Delete Employee'), ('search', 'Search')])
    submit = SubmitField('Submit')

class EmployeeInventoryForm(FlaskForm):
    ID = StringField('Item ID')
    Name = StringField('Item Name')
    Vendor = StringField('Vendor ID')
    Quantity = StringField('Quantity')
    Price = StringField('Price')
    radio = RadioField('Search By',
                            choices=[('ID', 'Item ID'), ('Name', 'Item Name'), ('Vendor', 'Vendor ID'), ('Price', 'Price')],
                            default='ID')
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
