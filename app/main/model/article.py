from app.main import db


class Article(db.Model):
    """Articles"""
    __tablename__ = "articles"

    uuid = db.Column(db.Text, primary_key=True)
    author = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    posted = db.Column(db.DateTime)
    modified = db.Column(db.DateTime)
    published = db.Column(db.Boolean)
    tags = db.Column(db.Text)
    alias = db.Column(db.Text)

    def __repr__(self):
        return "<Article '{}'>".format(self.title)
