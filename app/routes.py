from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! (Driver Log)"


@app.route('/login')
def login():
    return "login"


@app.route('/logout')
def logout():
    return "logout"


@app.route('/register')
def register():
    return "register"
