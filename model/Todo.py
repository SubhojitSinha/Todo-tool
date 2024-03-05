from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String(500))
    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }