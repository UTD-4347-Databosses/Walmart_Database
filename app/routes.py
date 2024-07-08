from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')

def index():
    return render_template('index.html')

@bp.route('/inventory')
def inventory():
    return render_template('inventory.html')

@bp.route('/customers')
def customers():
    return render_template('customers.html')

