from flask import Flask, redirect, url_for, request, flash
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import declarative_base, Session, sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
engine = create_engine('sqlite:///sqlite.db')
db = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class User(UserMixin, db):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = Column(String(100), unique=True)
    password = Column(String(100))
    first_name = Column(String(1000))
    last_name = Column(String(1000))

db.metadata.create_all(engine)

@app.route('/')
def index():
    return 'Welcome to Gawe.In'

@app.route('/profile')
@login_required
def profile():
    return 'This is profile page'

@app.route('/login')
def login():
    return 'Login'

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = session.query(User).filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again')
        return redirect(url_for('login'))
    
    login_user(user, remember=remember)
    return redirect(url_for('profile'))

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return session.query(User).get(id=id)

@app.route('/signup')
def signup():
    return 'Signup'

@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    user = session.query(User).filter_by(email=email).first()

    if user:
        return redirect(url_for('login'))
    
    new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password, method='sha256'))
    session.add(new_user)
    session.commit()

    return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logout'

if __name__ == '__main__':
    app.run(debug=True, port=8000)