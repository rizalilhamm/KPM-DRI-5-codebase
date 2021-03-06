from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tentang-kami')
def tentang_kami():
    return render_template('about_kami.html')

@app.route('/login')
def login():
    return render_template('login.html')