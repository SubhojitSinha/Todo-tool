from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
import datetime
db = SQLAlchemy()
class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    todo_id = db.Column(db.String)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)


    @property
    def serialize(self):
        """
        Property function to serialize the object into a dictionary.
        """
        return {
            'id': self.id,
            'todo_id': self.title,
            'start_time': self.start_time,
            'end_time': self.end_time
        }
