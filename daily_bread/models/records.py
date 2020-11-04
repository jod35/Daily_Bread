from ..extensions.database import db
from datetime import datetime
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Verse(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    bible_verse=db.Column(db.String(),nullable=False)
    date_read=db.Column(db.DateTime(),default=datetime.utcnow)
    notes=db.Column(db.Text)

    def __repr__(self):
        return f'{self.bible_verse} on {self.date_read}'

    def __init__(self,bible_verse,notes):
        self.bible_verse=bible_verse
        self.notes=notes
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class VerseSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model=Verse
        sqla_session=db.session

    id=fields.Integer()
    bible_verse=fields.String()
    date_read=fields.DateTime()


