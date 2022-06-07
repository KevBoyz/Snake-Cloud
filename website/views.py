from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)


@login_required
@views.route('/<user_name>')
def profile(user_name):
    return render_template('profile.html', user=current_user)
