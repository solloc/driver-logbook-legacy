from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    # return "Hello, World! (Driver Log)"


@app.route('/login')
def login():
    return "login"


@app.route('/logout')
def logout():
    return "logout"


@app.route('/register')
def register():
    return "register"
