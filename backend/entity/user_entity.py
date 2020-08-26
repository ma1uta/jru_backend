from datetime import datetime

from backend.__main__ import db


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    login = db.Column(db.Text, unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.today())
    confirmed_at = db.Column(db.DateTime)
    password = db.Column(db.Text, nullable=False)
