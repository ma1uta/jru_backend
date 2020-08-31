from app.main import db


class AuthToken(db.Model):
    """Auth tokens"""
    __tablename__ = "auth_tokens"

    id = db.Column(db.BigInteger, primary_key=True)
    jid = db.Column(db.Text)
    uuid = db.Column(db.Text)
    expires = db.Column(db.DateTime)

    def __repr__(self):
        return "<auth token '{}'>".format(self.id)
