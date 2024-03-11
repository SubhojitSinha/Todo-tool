from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
import datetime
db = SQLAlchemy()
class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    todo_id = db.Column(db.Integer)
    note = db.Column(db.String(500))
    created_at = db.Column(db.DateTime)


    @property
    def serialize(self):
        """
        Property function to serialize the object into a dictionary.
        """
        return {
            'id': self.id,
            'todo_id': self.title,
            'note': self.note,
            'created_at': self.created_at
        }
