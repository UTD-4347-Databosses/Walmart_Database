from flask import Blueprint, make_response, redirect, render_template, session

from app.InputForms import AdminPopulateForm, AdminResetForm, EmployeeCustomerForm, EmployeeInventoryForm, EmployeeViewForm, SettingsForm
from app.db import *
from app.InputForms import EmployeeCustomerForm, EmployeeViewForm, EmployeeInventoryForm, SettingsForm
from app.db import map

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
            query = db.session.query(map.classes.Customer).filter(map.classes.Customer.Fname == form.Fname.data).all()
        else:
            query = db.session.query(map.classes.Customer).filter(map.classes.Customer.Lname == form.Lname.data).all()
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
    if form.validate_on_submit():
        if form.radio.data == 'Fname':
            query = db.session.query(map.classes.Employee).filter(map.classes.Employee.Fname == form.Fname.data).all()
        elif form.radio.data == 'Lname':
            query = db.session.query(map.classes.Employee).filter(map.classes.Employee.Lname == form.Lname.data).all()
        elif form.radio.data == 'ID':
            query = db.session.query(map.classes.Employee).filter(map.classes.Employee.Employee_id == form.ID.data).all()
        elif form.radio.data == 'Date':
            query = db.session.query(map.classes.Employee).filter(map.classes.Employee.Start_date == form.Date.data).all()
        else:
            query = db.session.query(map.classes.Employee).filter(map.classes.Employee.Position_name == form.Position.data).all()
        count = len(query)
        return render_template('employee_view.html', form=form, employees=query, count=count)
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

@bp.route('/admin', methods=['GET', 'POST'])
def admin():
    reset_form = AdminResetForm()
    populate_form = AdminPopulateForm()
    if reset_form.validate_on_submit():
        if reset_form.options.data == 'reset_all':
            reset_all()
        elif reset_form.options.data == 'reset_customers':
            reset_customers()
        elif reset_form.options.data == 'reset_employees':
            reset_employees()
        elif reset_form.options.data == 'reset_vendors':
            reset_vendors()
        else:
            pass

    elif populate_form.validate_on_submit():
        if populate_form.options.data == 'populate_all':
            populate_all()
        elif populate_form.options.data == 'populate_customers':
            populate_customers()
        elif populate_form.options.data == 'populate_employees':
            populate_employees()
        elif populate_form.options.data == 'populate_vendors':
            populate_vendors()
        else:
            pass
    return render_template('admin.html', reset_form=reset_form, populate_form=populate_form)