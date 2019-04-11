from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'users.login'

from app.users import bp as users_bp  # noqa: E402
app.register_blueprint(users_bp)

from app import routes, model  # noqa: E402,F401
