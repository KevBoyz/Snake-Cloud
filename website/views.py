from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required, current_user
from werkzeug.exceptions import abort
from website.models import User

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)


@login_required
@views.route('/<user_name>')
def profile(user_name):
    user = User.query.filter_by(name=user_name).first()
    if not user:
        return abort(404)
    return render_template('profile.html', user_page=user, current_user=current_user)
