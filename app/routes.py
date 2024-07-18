from flask import Blueprint, make_response, redirect, render_template, session

from app.db import db
from app.InputForms import CustomerForm, SettingsForm
from app.db import Base

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    if 'role' not in session:
        session['role'] = 'customer'
    return render_template('walmart.html', role=session['role'])


@bp.route('/customers', methods=['GET', 'POST'])
def inventory():
    form = CustomerForm()
    if form.validate_on_submit():
        if form.radio.data == 'Fname':
            query = db.session.query(Base.classes.Customer).filter(Base.classes.Customer.Fname == form.Fname.data).all()
        else:
            query = db.session.query(Base.classes.Customer).filter(Base.classes.Customer.Lname == form.Lname.data).all()
        count = len(query)
        return render_template('customers.html', form=form, customers=query, count=count)
    return render_template('customers.html', form=form)

@bp.route('/employee', methods=['GET', 'POST'])
def customers():
    return render_template('employee.html')


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
