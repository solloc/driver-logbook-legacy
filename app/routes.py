from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import RegistrationForm, LoginForm, FuelLogCreateForm
from app.model import User, FuelLog
from flask_login import login_required, login_user, current_user, logout_user


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html.j2', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html.j2', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html.j2', form=form)


@app.route('/fuel-logs')
@login_required
def fuelLogs():
    fuelLogs = FuelLog.query.filter_by(user_id=current_user.id)
    return render_template('fuel_log_records.html.j2', fuelLogs=fuelLogs)


@app.route('/create-fuel-log', methods=['GET', 'POST'])
@login_required
def createFuelLogs():
    form = FuelLogCreateForm()
    if form.validate_on_submit():
        fuelLog = FuelLog(user_id=current_user.id,
                          distance=form.distance.data,
                          quantity=form.quantity.data,
                          recorded=form.recorded.data)
        db.session.add(fuelLog)
        db.session.commit()
        return redirect(url_for('fuelLogs'))
    return render_template('fuel_log_create.html.j2', form=form)
