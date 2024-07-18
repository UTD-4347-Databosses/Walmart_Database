from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField


class CustomerForm(FlaskForm):
    Fname = StringField('First Name')
    Lname = StringField('Last Name')
    radio = RadioField('Search By',
                          choices=[('Fname', 'First Name'), ('Lname', 'Last Name')],
                          default='name')
    submit = SubmitField('Submit')

class SettingsForm(FlaskForm):
    role = RadioField('Role',
                     choices=[('customer', 'Customer'), ('employee', 'Employee'), ('vendor', 'Vendor')],
                     default='customer')
    submit = SubmitField('Submit')

