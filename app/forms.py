from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    email = StringField('E-Mail Address', [DataRequired()])
    password = PasswordField('Password', [DataRequired(),
                                          EqualTo('password_confirm',
                                                  'Passwords must match')])
    password_confirm = PasswordField('Password (repeat)')
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Sign in')
