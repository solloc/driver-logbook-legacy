from app import app, db
from flask import render_template, redirect, url_for
from app.forms import FuelLogCreateForm
from app.model import FuelLog
from flask_login import login_required, current_user


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html.j2', title='Home')


@app.route('/fuel-logs')
@login_required
def fuelLogs():
    fuelLogs = FuelLog.query.filter_by(user_id=current_user.id)
    return render_template('fuel_log_records.html.j2', fuelLogs=fuelLogs)


@app.route('/fuel-logs/new', methods=['GET', 'POST'])
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
