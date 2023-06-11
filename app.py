from flask import Flask, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

# init SQLAlchemy so we can use it later in our models
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

@app.route('/')
def index():
    return 'Welcome to the Index page'

@app.route('/profile')
def profile():
    return 'This is the Profile page'

@app.route('/login')
def login():
    return 'Please login to access your account'

@app.route('/signup', methods=['GET'])
def signup():
    return 'Sign up for a new account'

@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()


    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    return 'You have been logged out'

if __name__ == '__main__':
    app.cli.add_command(db.create_all)
    app.run()