# Flask adalah micro framework web development
# 1. Service kecil
# 2. Biasa dipake untuk ngebuat API

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello, World Aplication!!'

@app.route('/profile')
def profile():
    return 'Halaman Profile'


# 127.0.0.1:5000/
# 127.0.0.1:5000/hello


# 127.0.0.1:5000/profile
