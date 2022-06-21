from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_required, current_user
from werkzeug.exceptions import abort
from website.models import User
from . import db

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
    return render_template('profile_overview.html', user_page=user, current_user=current_user)


@login_required
@views.route('/<user_name>/edit', methods=('GET', 'POST'))
def profile_edit(user_name):
    user = User.query.filter_by(name=user_name).first()
    if not user:
        return abort(401)
    if request.method == 'POST':
        user.fullName = request.form.get('fullName')
        user.bio = request.form.get('bio')
        user.website = request.form.get('website')
        user.address = request.form.get('address')
        user.company = request.form.get('company')
        db.session.commit()
    return render_template('profile_edit.html', user_page=current_user, user=current_user)
