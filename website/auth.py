from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from website.models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash('Logged successfully')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Email not found', category='error')
    return render_template('login.html', user=current_user)


@auth.route('/sing-up', methods=('GET', 'POST'))
def sing_up():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if User.query.filter_by(email=email).first():
            flash('This email already exists', category='error')
        elif User.query.filter_by(name=name).first():
            flash('This name is already in use, try another', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(email) < 3 or len(email) == 0:
            flash('Email is to short!', category='error')
        else:
            new_user = User(name=name, email=email, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account registered!', category='success')
            return redirect(url_for('auth.login'))
    return render_template('sing-up.html', user=current_user)



@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out', category='success')
    return redirect(url_for('auth.login'))


