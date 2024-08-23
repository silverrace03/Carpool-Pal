import random
import string
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

from emailer import send_email
from mongo_functions import *


app = Flask(__name__)
app.config['SECRET_KEY'] = '825'

def random_car_number_generator():
    states = ['AP','AR','AS','BR','CG','DL','GA','GJ','HR','HP','JK','JH','KA','KL','LD','MP','MH','MN','ML','MZ','NL','PY','PB','RJ','SK','TN','TS','TR','UP','WB','AN','CH','DN','DD', 'LA']
    return random.choice(states)+str(random.randint(10,99))+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+str(random.randint(1000,9999))

@app.route('/')
def index():
    if 'username' in session:
        is_loggedin = session.pop('is_loggedin', False) 

        if is_loggedin:
            return render_template('index.html', is_loggedin=True, button_text="Logout")

        else:
            return render_template('index.html', is_loggedin=False, button_text="Login | Sign In")
        
    return render_template('index.html', is_loggedin=False, button_text="Login | Sign In")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'is_loggedin' in session:
        session['is_loggedin'] = False

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if authenticate_team(username, password):
            session['username'] = username
            session['is_loggedin'] = True

            return redirect(url_for('index'))
        else:
            redirect(url_for('signup'))

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form.get('fullname').strip()
        username = request.form.get('username').strip()
        email = request.form.get('email').strip()
        password = request.form.get('password')
        
        if add_user(
            full_name,
            username,
            email,
            password
        ):
            return redirect(url_for('login'))
        else:
            return jsonify({"message": "failed to add the user"})

    return render_template('signup.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        print(request.form)
        
        destination_point = str(request.form['destination_point']).encode('ascii', 'ignore').decode()
        pickup_point = str(request.form['pickup_point']).encode('ascii', 'ignore').decode()
        departure_date = str(request.form['departure_date']).encode('ascii', 'ignore').decode()
        departuretime = str(request.form['departure_time']).encode('ascii', 'ignore').decode()
        no_of_passengers = str(request.form['no_of_passengers']).encode('ascii', 'ignore').decode()
        emailId = str(request.form['email_id']).encode('ascii', 'ignore').decode()

        try:
            _ = send_email(
                emailId,
                "Mr. Ramesh Kumar",
                departure_date,
                departuretime,
                str(random_car_number_generator()),
                pickup_point,
                destination_point,
                no_of_passengers
            )
            return render_template("success.html")
        
        except Exception as e:
            return jsonify({"output": str(e)})

@app.route('/logout')

def logout():
    session.pop('username', None)
    session.pop('is_loggedin', None)
    return redirect(url_for('login'))

@app.route('/bookride')
def bookride():
    return render_template('formPage.html')

@app.route('/rentcar')
def rentcar():
    return render_template('rent.html')

# @app.route('/bookride')
# def bookride():
#     return render_template('book.html')

@app.route('/contact')
def contact():
    return render_template('contactUs.html')

@app.route('/rent2')
def rent2():
    return render_template('rent2.html')

if __name__ == '_main_':
    app.run(debug=True)
