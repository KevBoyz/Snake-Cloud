from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    fullName = db.Column(db.String())
    website = db.Column(db.String())
    address = db.Column(db.String())
    company = db.Column(db.String())
    bio = db.Column(db.String(200))

