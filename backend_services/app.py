import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# https://docs.python.org/3/library/os.path.html (Referensi belajar library os python)
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
db = SQLAlchemy(app)

# kunci rahasia
SECRET_KEY = os.getenv('SECRET_KEY') or 'ini-rahasia'

# 
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello, World Aplication!!'

@app.route('/profile')
def profile():
    return 'Halaman Profile'

# USER MODEL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)    # render automaticlly by server if not inisilized
    nama = db.Column(db.String(50), nullable=False, unique=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    bio = db.COlumn(db.String(150), nullable=True, unique=False)

    def __repr__(self):
        return self.nama