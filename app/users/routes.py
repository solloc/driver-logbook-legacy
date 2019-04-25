from app import db
from flask import render_template, redirect, url_for, flash
from app.forms import RegistrationForm, LoginForm
from app.model import User
from flask_login import login_required, login_user, current_user, logout_user
from app.users import bp


@bp.route('/index')
@bp.route('/')
@login_required
def listUsers():
    users = User.query.all()
    return render_template('users_list.html.j2', users=users)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('users.login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html.j2', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('register.html.j2', form=form)


# should only be allowed as admin
# could be implemented with decorators, just start with checks
@bp.route('/new')
@login_required
def createUser():
    return render_template('user_create.html.j2')
