from app.main import db


class Feedback(db.Model):
    """Feedbacks"""
    __tablename__ = "feedbacks"

    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.Text)
    message = db.Column(db.Text)
    ip = db.Column(db.Text)

    def __repr__(self):
        return "<Feedback '{}'>".format(self.id)
