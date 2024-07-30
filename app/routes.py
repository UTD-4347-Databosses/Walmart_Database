from flask import Blueprint, make_response, redirect, render_template, session, flash, url_for

from app.InputForms import AdminPopulateForm, AdminResetForm, EmployeeCustomerForm, EmployeeInventoryForm, \
    EmployeeViewForm, SettingsForm, CustomerInventoryForm, CustomerTransactionForm, BadCustomerInventoryForm
from app.db import *
from app.InputForms import EmployeeCustomerForm, EmployeeViewForm, EmployeeInventoryForm, SettingsForm
from app.db import map
from sqlalchemy import text
import mysql.connector




bp = Blueprint('main', __name__)



@bp.route('/')
def index():
    if 'role' not in session:
        session['role'] = 'customer'
    return render_template('walmart.html', role=session['role'])



'''
**************************************************************************************************
CUSTOMER SECTION *********************************************************************************
**************************************************************************************************
'''

@bp.route('/customer', methods=['GET', 'POST'])
def customer():
    return render_template('customer.html')

###################
# GOOD ONE
####################

@bp.route('/customer_inventory', methods=['GET', 'POST'])
def customer_inventory():
    query = []  # Reset query to ensure previous search is cleared after every search
    form = CustomerInventoryForm()


    if form.validate_on_submit():

        if form.Operation.data == "search":
            if form.radio.data == 'ID':
                query = db.session.query(map.classes.Inventory, map.classes.Vendor).join(map.classes.Vendor).filter(map.classes.Inventory.Item_id == form.ID.data).all()
            elif form.radio.data == 'Name':
                query = db.session.query(map.classes.Inventory, map.classes.Vendor).join(map.classes.Vendor).filter(map.classes.Inventory.Item_name  == form.Name.data).all()
            elif form.radio.data == 'Price':
                query = db.session.query(map.classes.Inventory, map.classes.Vendor).join(map.classes.Vendor).filter(map.classes.Inventory.Price == form.Price.data).all()

            count = len(query)
            return render_template('customer_inventory.html', form=form, results=query, count=count)


    else:
        query = db.session.query(map.classes.Inventory, map.classes.Vendor).join(map.classes.Vendor).all()
        #item = query[0]
        count = len(query)
        return render_template('customer_inventory.html', form=form, results=query, count=count)




###################
# BAD ONE
####### ##############
@bp.route('/bad_customer_inventory', methods=['GET', 'POST'])
def bad_inventory():
    form = BadCustomerInventoryForm()
    query = []

    if form.validate_on_submit():

        # use
        # 1' OR '1'='1
        if form.Operation.data == 'Search':

            if form.radio.data == 'ID':
                id = form.ID.data
                # Adjusting the SQL query to prevent duplication
                query = db.session.execute(
                    text(f"SELECT DISTINCT i.Item_id, i.Item_name, i.Quantity, v.Vendor_id, v.Vendor_name, i.Price "
                         f"FROM Inventory as i "
                         f"JOIN Vendor as v ON i.Vendor_id = v.Vendor_id "
                         f"WHERE i.Item_id = '{id}'")
                ).fetchall()

            elif form.radio.data == 'Name':
                name = form.Name.data
                # Adjusting the SQL query to prevent duplication
                query = db.session.execute(
                    text(f"SELECT DISTINCT i.Item_id, i.Item_name, i.Quantity, v.Vendor_id, v.Vendor_name, i.Price "
                         f"FROM Inventory as i "
                         f"JOIN Vendor as v ON i.Vendor_id = v.Vendor_id "
                         f"WHERE i.Item_name = '{name}'")
                ).fetchall()

            elif form.radio.data == 'Price':
                price = form.Price.data
                # Adjusting the SQL query to prevent duplication
                query = db.session.execute(
                    text(f"SELECT DISTINCT i.Item_id, i.Item_name, i.Quantity, v.Vendor_id, v.Vendor_name, i.Price "
                         f"FROM Inventory as i "
                         f"JOIN Vendor as v ON i.Vendor_id = v.Vendor_id "
                         f"WHERE i.Price = '{price}'")
                ).fetchall()

            count = len(query)
            return render_template('bad_customer_inventory.html', form=form, results=query, count=count)



        # use in "name" feild
        #     '; DROP TABLE Inventory; --

        elif form.Operation.data == 'Update':


            # Establish a database connection (replace placeholders with your actual credentials)
            connection = mysql.connector.connect(
                host="databoss-database.czk2mm6e60xo.us-east-1.rds.amazonaws.com",
                user="databoss",
                password="PASSWORD",
                database="Walmart"
            )

            id = form.ID.data
            name = form.Name.data
            vendor_id = form.Vendor.data
            quantity = form.Quantity.data
            price = form.Price.data

            # Secure update statement using parameterized queries
            vulnerable_update_statement = f"""
                UPDATE Inventory
                SET Item_name = '{name}',
                Vendor_id = {vendor_id},
                Quantity = {quantity},
                Price = {price} 
                WHERE Item_id = {id}
                """

            cursor = connection.cursor()
            cursor.execute(vulnerable_update_statement)
            connection.commit()
            cursor.close()
            connection.close()

            query = db.session.execute(text("SELECT DISTINCT i.Item_id, i.Item_name, i.Quantity, v.Vendor_id, v.Vendor_name, i.Price FROM Inventory as i JOIN Vendor as v ON i.Vendor_id = v.Vendor_id ")).fetchall()
            item = query[0]
            count = len(query)
            return render_template('bad_customer_inventory.html', form=form, results=query, count=count)

    else:
        query = db.session.execute(text("SELECT DISTINCT i.Item_id, i.Item_name, i.Quantity, v.Vendor_id, v.Vendor_name, i.Price FROM Inventory as i JOIN Vendor as v ON i.Vendor_id = v.Vendor_id ")).fetchall()
        item = query[0]
        count = len(query)
        return render_template('bad_customer_inventory.html', form=form, results=query, count=count)
















@bp.route('/customer_transactions', methods=['GET', 'POST'])
def customer_transactions():
    query = []  # Reset query to ensure previous search is cleared after every search
    form = CustomerTransactionForm()
    if form.validate_on_submit():

        if form.Operation.data == "search":
            if form.radio.data == 'TransactionID':
                query = db.session.query(map.classes.Transaction).filter(map.classes.Transaction.Transaction_id == form.TransactionID.data).all()
            elif form.radio.data == 'CustomerID':
                query = db.session.query(map.classes.Transaction).filter(map.classes.Transaction.Lname == form.CustomerID.data).all()
            elif form.radio.data == 'EmployeeID':
                query = db.session.query(map.classes.Transaction).filter(map.classes.Transaction.Employee_id == form.EmployeeID.data).all()
            elif form.radio.data == 'LocationID':
                query = db.session.query(map.classes.Transaction).filter(map.classes.TransactionEmployee.Start_date == form.LocationID.data).all()
            elif form.radio.data == 'TransactionAmount':
                query = db.session.query(map.classes.Transaction).filter(map.classes.Transaction.Start_date == form.TransactionAmount.data).all()

            count = len(query)
            return render_template('customer_transactions.html', form=form, results=query, count=count)


    else:
        query = db.session.query(map.classes.Transaction).all()
        count = len(query)
        return render_template('customer_transactions.html', form=form, results=query, count=count)










'''
**************************************************************************************************
EMPLOYEE SECTION *********************************************************************************
**************************************************************************************************
'''


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

                query = db.session.query(map.classes.Employee, map.classes.Position_type).join(map.classes.Position_type).all()
                count = len(query)
                return render_template('employee_view.html', form=form, results=query, count=count)


            except Exception as e:
                db.session.rollback()  # Rollback on error
                print(f"Error adding employee: {e}", "danger")
                query = db.session.query(map.classes.Employee, map.classes.Position_type).join(map.classes.Position_type).all()
                count = len(query)
                return render_template('employee_view.html', form=form, results=query, count=count, error=str(e))



        elif form.Operation.data == "search":
            if form.radio.data == 'Fname':
                query = db.session.query(map.classes.Employee, map.classes.Position_type).join(map.classes.Position_type).filter(map.classes.Employee.Fname == form.Fname.data).all()
            elif form.radio.data == 'Lname':
                query = db.session.query(map.classes.Employee, map.classes.Position_type).join(map.classes.Position_type).filter(map.classes.Employee.Lname == form.Lname.data).all()
            elif form.radio.data == 'ID':
                query = db.session.query(map.classes.Employee, map.classes.Position_type).join(map.classes.Position_type).filter(map.classes.Employee.Employee_id == form.ID.data).all()
            elif form.radio.data == 'Date':
                query = db.session.query(map.classes.Employee, map.classes.Position_type).join(map.classes.Position_type).filter(map.classes.Employee.Start_date == form.Date.data).all()
            elif form.radio.data == 'Position':
                query = db.session.query(map.classes.Employee, map.classes.Position_type).join(map.classes.Position_type).filter(map.classes.Employee.Position_name == form.Position.data).all()
            elif form.radio.data == 'Salary':
                query = db.session.query(map.classes.Employee, map.classes.Position_type).join(map.classes.Position_type).filter(map.classes.Position_type.Salary == form.Salary.data).all()
            elif form.radio.data == 'Hourly':
                query = db.session.query(map.classes.Employee, map.classes.Position_type).join(map.classes.Position_type).filter(map.classes.Positionn_type.Hourly_wage == form.Hourly.data).all()
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
            employee = db.session.query(map.classes.Employee).filter(map.classes.Employee.Employee_id == form.ID.data).first()
            if employee:
                db.session.delete(employee)
                db.session.commit()
                flash('Employee deleted successfully!', 'success')
            else:
                flash('Employee not found!', 'danger')

        query = db.session.query(map.classes.Employee, map.classes.Position_type).join(map.classes.Position_type).all()
        count = len(query)
        return render_template('employee_view.html', form=form, results=query, count=count)
    else:
        query = db.session.query(map.classes.Employee, map.classes.Position_type).join(map.classes.Position_type).all()
        count = len(query)
        return render_template('employee_view.html', form=form, results=query, count=count)








@bp.route('/employee_inventory', methods=['GET', 'POST'])
def employee_inventory():
    # TODO: Implement the employee inventory logic
    query = []  # Reset query to ensure previous search is cleared after every search
    form = EmployeeInventoryForm()


    if form.validate_on_submit():


        if form.Operation.data == "add":
            # Assuming form has all necessary fields for an Inventory item
            new_inventory = map.classes.Inventory(
                Item_id=form.ID.data,
                Item_name=form.Name.data,
                Quantity=form.Quantity.data,
                Vendor_id=form.Vendor.data,
                Price = form.Price.data
            )
            db.session.add(new_inventory)
            db.session.commit()
            flash('Inventory item added successfully!', 'success')

            count = len(query)
            return render_template('employee_inventory.html', form=form, results=query, count=count)



        elif form.Operation.data == "search":
            if form.radio.data == 'ID':
                query = db.session.query(map.classes.Inventory, map.classes.Vendor).join(map.classes.Vendor).filter(
                    map.classes.Inventory.Item_id == form.ID.data).all()
            elif form.radio.data == 'Name':
                query = db.session.query(map.classes.Inventory, map.classes.Vendor).join(map.classes.Vendor).filter(
                    map.classes.Inventory.Item_name == form.Name.data).all()
            elif form.radio.data == 'Vendor':
                query = db.session.query(map.classes.Inventory, map.classes.Vendor).join(map.classes.Vendor).filter(
                    map.classes.Inventory.Vendor_id == form.Vendor.data).all()
            elif form.radio.data == 'Price':
                query = db.session.query(map.classes.Inventory, map.classes.Vendor).join(map.classes.Vendor).filter(
                map.classes.Inventory.Price == form.Price.data).all()

            count = len(query)
            return render_template('employee_inventory.html', form=form, results=query, count=count)



        elif form.Operation.data == "update":
            inventory_item = db.session.query(map.classes.Inventory, map.classes.Vendor).join(map.classes.Vendor).filter(
                map.classes.Inventory.Item_id == form.ID.data).first()
            if inventory_item:
                inventory_item.Item_name = form.Name.data
                inventory_item.Quantity = form.Quantity.data
                inventory_item.Vendor_id = form.Vendor.data
                inventory_item.Price = form.Price.data
                db.session.commit()
                flash('Inventory item updated successfully!', 'success')
            else:
                flash('Inventory item not found!', 'danger')

            count = len(query)
            return render_template('employee_inventory.html', form=form, resutls=query, count=count)



        elif form.Operation.data == "delete":
            inventory_item = db.session.query(map.classes.Inventory, map.classes.Vendor).join(map.classes.Vendor).filter(map.classes.Inventory.Item_id == form.ID.data).first()
            if inventory_item:
                db.session.delete(inventory_item)
                db.session.commit()
                flash('Inventory item deleted successfully!', 'success!')
            else:
                flash('Inventory item not found!', 'danger!')

            count = len(query)
            return render_template('employee_inventory.html', form=form, results=query, count=count)

    else:
        query = db.session.query(map.classes.Inventory, map.classes.Vendor).join(map.classes.Vendor).all()
        count = len(query)
        return render_template('employee_inventory.html', form=form, results=query, count=count)



@bp.route('/employee_customers', methods=['GET', 'POST'])
def employee_customers():
    # TODO: Implement the employee customers logic
    form = EmployeeCustomerForm()
    query = []  # Reset query to ensure previous search is cleared after every search

    if form.validate_on_submit():


        if form.Operation.data == "add":
            # Assuming form has all necessary fields for an Inventory item
            new_customer = map.classes.Customer(
                Customer_id=form.ID.data,
                Fname=form.Fname.data,
                Lname=form.Lname.data,
                Email=form.Email.data,
                Phone_num=form.Phone.data,
                Street_address=form.Address.data,
                City=form.City.data,
                State=form.State.data
            )
            db.session.add(new_customer)
            db.session.commit()
            flash('Customer info added successfully!', 'success')


        elif form.Operation.data == "search":
            if form.radio.data == 'ID':
                query = db.session.query(map.classes.Customer).filter(
                    map.classes.Customer.Customer_id == form.ID.data).all()
            elif form.radio.data == 'FName':
                query = db.session.query(map.classes.Customer).filter(
                    map.classes.Customer.Fname == form.Fname.data).all()
            elif form.radio.data == 'LName':
                query = db.session.query(map.classes.Customer).filter(
                    map.classes.Customer.Lname == form.Lname.data).all()
            count = len(query)
            return render_template('employee_customers.html', form=form, results=query, count=count)



        elif form.Operation.data == "update":
            customer_info = db.session.query(map.classes.Customer).filter(
                map.classes.Customer.Customer_id == form.ID.data).first()
            if customer_info:
                customer_info.Customer_id = form.ID.data,
                customer_info.Fname = form.Fname.data,
                customer_info.Lname = form.Lname.data,
                customer_info.Email = form.Email.data,
                customer_info.Phone_num = form.Phone.data,
                customer_info.Street_address = form.Address.data,
                customer_info.City = form.City.data,
                customer_info.State = form.State.data
                db.session.commit()
                flash('Customer information updated successfully!', 'success')
            else:
                flash('Customer information not found!', 'danger')



        elif form.Operation.data == "delete":
            customer_info = db.session.query(map.classes.Customer).filter(
                map.classes.Customer.Customer_id == form.ID.data).first()
            if customer_info:
                db.session.delete(customer_info)
                db.session.commit()
                flash('Customer information deleted successfully!', 'success!')
            else:
                flash('Inventory item not found!', 'danger!')

        return redirect(url_for('main.employee_customers'))


    else:
        query = db.session.query(map.classes.Customer).all()
        count = len(query)
        return render_template('employee_customers.html', form=form, results=query, count=count)











'''
**************************************************************************************************
OTHER SECTION *********************************************************************************
**************************************************************************************************
'''
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