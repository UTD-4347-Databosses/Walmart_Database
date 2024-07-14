from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    return render_template('walmart.html')

@bp.route('/employee')
def inventory():
    return render_template('employee.html')

@bp.route('/customers')
def customers():
    return render_template('customers.html')

@bp.route('/vendor')
def vendor():
    return render_template('vendor.html')
