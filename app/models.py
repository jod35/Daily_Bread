from .extensions import db


class Record(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    verse = db.Column(db.Text(), nullable=False)
    notes = db.Column(db.Text(),nullable=False)

    def __init__(self, verse, notes):
        self.verse = verse
        self.notes = notes

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
