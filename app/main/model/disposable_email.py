from app.main import db


class DisposableEmail(db.Model):
    """Disposable emails"""
    __tablename__ = "disposableemails"

    domain = db.Column(db.Text, primary_key=True)
    state = db.Column(db.Text, nullable=False)
    json = db.Column(db.Text)

    def __repr__(self):
        return "<Disposable email '{}'>".format(self.domain)
