from app.main import db


class ArchivePref(db.Model):
    """Archive prefs"""
    __tablename__ = "archive_prefs"

    username = db.Column(db.Text, primary_key=True)
    definition = db.Column("def", db.Text)
    always = db.Column(db.Text)
    never = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __repr__(self):
        return "<Archive prefs '{}'>".format(self.username)
