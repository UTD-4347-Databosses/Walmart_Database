from flask import Blueprint, make_response, redirect, render_template, session, flash, url_for

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
        return render_template('customers.html', form=form, results=query, count=count)
    return render_template('customers.html', form=form)


@bp.route('/employee', methods=['GET', 'POST'])
def employee():
    return render_template('employee.html')


@bp.route('/employee_view', methods=['GET', 'POST'])
def employee_view():
    # TODO: Implement the employee view logic
    query = []  # Reset query to ensure previous search is cleared after every search
    form = EmployeeViewForm()
    if form.validate_on_submit():
        if form.Operation.data == "add":
            try:
                existing_employee = db.session.query(map.classes.Employee).filter_by(Employee_id=form.ID.data).first()
                if existing_employee:
                    flash(message='Employee already exists!', category='danger')

                else:
                    # Assuming user inputs all necessary info for the Employee
                    new_employee = map.classes.Employee(
                        Fname=form.Fname.data,
                        Lname=form.Lname.data,
                        Employee_id=form.ID.data,
                        Start_date=form.Date.data,
                        Position_name=form.Position.data
                    )

                    db.session.add(new_employee)
                    db.session.commit()
                    flash('Employee added successfully!', 'success')  # For verification

                query = db.session.query(map.classes.Employee).all()
                count = len(query)
                return render_template('employee_view.html', form=form, results=query, count=count)
            except Exception as e:
                db.session.rollback()  # Rollback on error
                print(f"Error adding employee: {e}", "danger")
                query = db.session.query(map.classes.Employee).all()
                count = len(query)
                return render_template('employee_view.html', form=form, results=query, count=count, error=str(e))

        elif form.Operation.data == "search":
            if form.radio.data == 'Fname':
                query = db.session.query(map.classes.Employee).filter(
                    map.classes.Employee.Fname == form.Fname.data).all()
            elif form.radio.data == 'Lname':
                query = db.session.query(map.classes.Employee).filter(
                    map.classes.Employee.Lname == form.Lname.data).all()
            elif form.radio.data == 'ID':
                query = db.session.query(map.classes.Employee).filter(
                    map.classes.Employee.Employee_id == form.ID.data).all()
            elif form.radio.data == 'Date':
                query = db.session.query(map.classes.Employee).filter(
                    map.classes.Employee.Start_date == form.Date.data).all()
            else:
                query = db.session.query(map.classes.Employee).filter(
                    map.classes.Employee.Position_name == form.Position.data).all()
            count = len(query)
            return render_template('employee_view.html', form=form, results=query, count=count)

        elif form.Operation.data == "update":
            employee = db.session.query(map.classes.Employee).filter(
                map.classes.Employee.Employee_id == form.ID.data).first()
            if employee:
                employee.Fname = form.Fname.data
                employee.Lname = form.Lname.data
                employee.Start_date = form.Date.data
                employee.Position_name = form.Position.data
                db.session.commit()
                flash('Employee updated successfully!', 'success!')
            else:
                flash('Employee not found!', 'danger!')
        elif form.Operation.data == "delete":
            employee = db.session.query(map.classes.Employee).filter(
                map.classes.Employee.Employee_id == form.ID.data).first()
            if employee:
                db.session.delete(employee)
                db.session.commit()
                flash('Employee deleted successfully!', 'success')
            else:
                flash('Employee not found!', 'danger')

        query = db.session.query(map.classes.Employee).all()
        count = len(query)
        return render_template('employee_view.html', form=form, results=query, count=count)
    else:
        query = db.session.query(map.classes.Employee).all()
        count = len(query)
        return render_template('employee_view.html', form=form, results=query, count=count)
    # return render_template('employee_view.html', form=form, column_names=map.tables.Employee.columns.keys())


@bp.route('/employee_inventory', methods=['GET', 'POST'])
def employee_inventory():
    # TODO: Implement the employee inventory logic
    query = []  # Reset query to ensure previous search is cleared after every search
    form = EmployeeInventoryForm()
    if form.validate_on_submit():
        if form.radio.data == 'ID':
            query = db.session.query(map.classes.Inventory).filter(map.classes.Inventory.Item_id == form.ID.data).all()
        elif form.radio.data == 'Name':
            query = db.session.query(map.classes.Inventory).filter(map.classes.Inventory.Item_name == form.Name.data).all()
        elif form.radio.data == 'Vendor':
            query = db.session.query(map.classes.Inventory).filter(map.classes.Inventory.Vendor_id == form.Vendor.data).all()
        count = len(query)

        if form.Operation.data == "search":
            return render_template('employee_inventory.html', form=form, inventory=query, count=count)
        elif form.Operation.data == "add":
            # Assuming form has all necessary fields for an Inventory item
            new_inventory = map.classes.Inventory(
                ID=form.ID.data,
                Name=form.Name.data,
                Quantity=form.Quantity.data,
                Vendor=form.Vendor.data
            )
            db.session.add(new_inventory)
            db.session.commit()
            flash('Inventory item added successfully!', 'success')
        elif form.Operation.data == "update":
            inventory_item = db.session.query(map.classes.Inventory).filter(
                map.classes.Inventory.Item_id == form.ID.data).first()
            if inventory_item:
                inventory_item.Item_name = form.Name.data
                inventory_item.Quantity = form.Quantity.data
                inventory_item.Vendor_id = form.Vendor.data
                db.session.commit()
                flash('Inventory item updated successfully!', 'success')
            else:
                flash('Inventory item not found!', 'danger')
        elif form.Operation.data == "delete":
            inventory_item = db.session.query(map.classes.Inventory).filter(
                map.classes.Inventory.Item_id == form.ID.data).first()
            if inventory_item:
                db.session.delete(inventory_item)
                db.session.commit()
                flash('Inventory item deleted successfully!', 'success!')
            else:
                flash('Inventory item not found!', 'danger!')

        return redirect(url_for('employee_inventory'))
    return render_template('employee_inventory.html', form=form)


@bp.route('/employee_customers', methods=['GET', 'POST'])
def employee_customers():
    # TODO: Implement the employee customers logic
    form = EmployeeCustomerForm()
    return render_template('employee_customers.html', form=form, column_names=map.tables.Customer.columns.keys())


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