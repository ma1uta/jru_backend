from datetime import datetime

from app.main import db


class User(db.Model):
    """User"""
    __tablename__ = "users"

    username = db.Column(db.Text, primary_key=True)
    server = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    ip = db.Column(db.Text)

    def __repr__(self):
        return "<User '{}'>".format(self.username)
