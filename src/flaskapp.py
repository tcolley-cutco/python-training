from flask import Flask, render_template, session, \
    send_from_directory, abort, request, redirect
from functools import wraps
import sys
import csv
import json
import conn_util
from random import randint


# TODO Is it possible to make a Connection program that handles the disparity between the midrange and local so
# TODO that you can actually do local testing as intended? Maybe load different drivers based on os.name and then
# TODO if you're on local, do an outbound connection? There's still a roadblock with connecting over the wire to the
# TODO 400 but that must be solvable if programs can be run from the Linux box targeting the 400 DB. If not, can I rip
# TODO the driver out of the 400 directly and then modify it to run in NT, or is there possibly an open-source driver?

app = Flask(__name__)
conn = conn_util.fetch_db2_connection()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function


def close(cursor):
    if cursor:
        try:
            cursor.close()
        except Exception as e:
            print("Couldn't close cursor due to " + str(e))


@app.route("/")
@login_required
def hello():
    name = request.args.get('username')
    name = '' if name is None else ' ' + name

    return render_template('index.html', name=name)


@app.route("/cookies")
def cookies():
    return render_template('cookies-recipe.html')


@app.route("/eight-ball")
def eight_ball():

    file = open("templates/res/txt/8-ball-answers.txt", 'r')
    reader = csv.reader(file)
    answers = [row for row in reader]
    max_index = len(answers) - 1
    index = randint(0, max_index)
    answer = answers[index][0]

    return json.dumps(answer)


@app.route("/formAddSupply")
@login_required
def form_add_supply():
    return render_template('formAddSupply.html')


def fetch_supply_types():
    cur = conn.cursor()
    sql = "select * from pgfiles.supplyty"
    cur.execute(sql)

    supply_types = []
    for row in cur:
        this_supply_type = (row[0], row[1])
        supply_types.append(this_supply_type)

    return supply_types


@app.route("/bootstrapAddSupply")
@login_required
def bootstrap_add_supply():
    success = ''
    errors = []
    if 'bootstrapAddSupplySuccess' in session:
        success = session['bootstrapAddSupplySuccess']
        session.pop('bootstrapAddSupplySuccess')
    if 'bootstrapAddSupplyFailure' in session:
        errors = session['bootstrapAddSupplyFailure']
        session.pop('bootstrapAddSupplyFailure')

    return render_template('index2.html', success=success, errors=errors,
                           supply_types=fetch_supply_types())


@app.route('/addSupply', methods=['POST'])
@login_required
def add_supply():

    # read the posted values from the UI
    supply_name = request.form['supply_name']
    supply_brand = request.form['supply_brand']
    supply_color = request.form['supply_color']
    supply_quantity = request.form['supply_quantity']
    supply_type = request.form['supply_type']
    in_stock_form = 'N'
    if 'in_stock' in request.form:
        in_stock_form = request.form['in_stock']
    is_backordered = 'is_backordered' in request.form
    notes = request.form['notes']

    # Coalesce any values to True/False
    in_stock = in_stock_form == 'Y'

    output = 'Name: ' + supply_name + '<br>Brand: ' + supply_brand + '<br>Color: ' + supply_color + \
             '<br>Quantity: ' + supply_quantity + '<br>Type: ' + supply_type + '<br>In Stock? ' + str(in_stock) + \
             '<br>Backordered? ' + str(is_backordered) + '<br>Notes: ' + notes

    print(output)

    errors = []
    if len(supply_name) <= 0:
        errors.append('The supply name cannot be blank!')
    if len(supply_brand) <= 0:
        errors.append('The supply brand cannot be blank!')
    if len(supply_quantity) <= 0 or not supply_quantity.isnumeric():
        errors.append('The supply quantity must be a number!')

    if errors:
        session['bootstrapAddSupplyFailure'] = errors
    else:
        ps = conn.cursor()
        sql = 'INSERT INTO PGFILES.SUPPLIES (supply_brand, supply_type) values(?, ?)'
        ps.execute(sql, (supply_brand, supply_type))

        session['bootstrapAddSupplySuccess'] = 'true'

    return redirect('/bootstrapAddSupply')


def authenticate_user(username, password):
    is_authenticated = False
    errors = []
    if len(username) > 0 and len(password) > 0:

        cursor = None
        try:
            cursor = conn_util.fetch_db2_connection_with_credentials(username, password)
            is_authenticated = True     # If we reach this line, it didn't throw an exception. We're good to go
        except Exception as e:
            print(str(e) + " | User couldn't sign on because the user/pass combo were invalid!")
            errors.append('Invalid user/pass combo')
            is_authenticated = False
        finally:
            close(cursor)

    else:
        errors.append('Username and password cannot be blank!')

    if not is_authenticated:
        session['logonErrors'] = errors

    return is_authenticated


@app.route('/login', methods=['GET', 'POST'])
def login():
    valid_logon = False
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            if authenticate_user(username, password):
                session['user'] = username
                valid_logon = True

    if valid_logon:
        return redirect("/bootstrapAddSupply")
    else:
        errors = []
        if 'logonErrors' in session:
            errors = session['logonErrors']
            session.pop('logonErrors')
        return render_template('login.html', errors=errors)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect("/login")


# Listener for static resources. Should be restricted to local + testing. It uses whitelist restrictions to prevent
# unrestricted file access. Obviously this would be provided by Apache/Nginx/etc in the real world, but it's okay here
@app.route('/res/<path:path>/<path:filename>')
def send_files(path, filename):
    valid_paths = ['css', 'js', 'img']
    if path in valid_paths:
        full_path = 'templates/res/' + path + '/'
        return send_from_directory(full_path, filename)
    else:
        return abort(404)


if __name__ == "__main__":

    system_platform = sys.platform
    on_400 = system_platform == 'aix6'

    debug = True
    host = 'localhost'
    if on_400:
        debug = False
        host = '0.0.0.0'

    print("Platform: " + system_platform)
    print("Debug?: " + str(debug))
    print("Host: " + host)

    app.secret_key = 'cutcokey'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=debug, port=9110, host=host)
