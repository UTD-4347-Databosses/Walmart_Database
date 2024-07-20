from flask import Blueprint, make_response, redirect, render_template, session

from app.db import db
from app.InputForms import EmployeeCustomerForm, EmployeeViewForm, EmployeeInventoryForm, SettingsForm
from app.db import Base

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    if 'role' not in session:
        session['role'] = 'customer'
    return render_template('walmart.html', role=session['role'])


@bp.route('/customers', methods=['GET', 'POST'])
def customer():
    form = EmployeeCustomerForm()
    if form.validate_on_submit():
        if form.radio.data == 'Fname':
            query = db.session.query(Base.classes.Customer).filter(Base.classes.Customer.Fname == form.Fname.data).all()
        else:
            query = db.session.query(Base.classes.Customer).filter(Base.classes.Customer.Lname == form.Lname.data).all()
        count = len(query)
        return render_template('customers.html', form=form, customers=query, count=count)
    return render_template('customers.html', form=form)

@bp.route('/employee', methods=['GET', 'POST'])
def employee():
    return render_template('employee.html')

@bp.route('/employee_view', methods=['GET', 'POST'])
def employee_view():
    # TODO: Implement the employee view logic
    form = EmployeeViewForm()
    return render_template('employee_view.html', form=form)

@bp.route('/employee_inventory', methods=['GET', 'POST'])
def employee_inventory():
    # TODO: Implement the employee inventory logic
    form = EmployeeInventoryForm()
    return render_template('employee_inventory.html', form=form)

@bp.route('/employee_customers', methods=['GET', 'POST'])
def employee_customers():
    # TODO: Implement the employee customers logic
    form = EmployeeCustomerForm()
    return render_template('employee_customers.html', form=form)

@bp.route('/vendor', methods=['GET', 'POST'])
def vendor():
    return render_template('vendor.html')


@bp.route('/settings', methods=['GET', 'POST'])
def settings():
    form = SettingsForm()
    if form.validate_on_submit():
        # set the cookie for the role
        response = make_response(redirect('/'))
        session['role'] = form.role.data
        response.set_cookie('role', session['role'], max_age=60 * 60)
        return response
    return render_template('settings.html', form=form)
