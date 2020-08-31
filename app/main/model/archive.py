from app.main import db


class Archive(db.Model):
    """Archive"""
    __tablename__ = "archive"

    id = db.Column(db.BigInteger, primary_key=True)
    timestamp = db.Column(db.DateTime)
    username = db.Column(db.Text)
    bare_peer = db.Column(db.Text)
    kind = db.Column(db.Text)
    nick = db.Column(db.Text)
    txt = db.Column(db.Text)
    xml = db.Column(db.Text)

    def __repr__(self):
        return "<Archive '{}'>".format(self.username)
