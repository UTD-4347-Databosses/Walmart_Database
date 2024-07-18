from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField


class InventoryForm(FlaskForm):
   serial_number = StringField('Serial Number')
   submit = SubmitField('Submit')

class SettingsForm(FlaskForm):
   role = RadioField('Role',
                     choices=[('customer', 'Customer'), ('employee', 'Employee'), ('vendor', 'Vendor')],
                     default='customer')
   submit = SubmitField('Submit')

