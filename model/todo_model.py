from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
import datetime
db = SQLAlchemy()
class Todo(db.Model):
    __tablename__ = 'todo'
    status_array = ["Ongoing", "Due", "Hold", "Ongoing"]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String(500))
    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)

    @property
    def serialize(self):
        """
        Property function to serialize the object into a dictionary.
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at,
            'completed_at':self.completed_at
        }

    @classmethod
    def fetch_all(self, request):
        """
        Fetches all the user data and returns it as JSON.
        """
        message = ''
        status = request.args.get('status')
        id = request.args.get('id')
        search = request.args.get('search')
        qry = self.query
        if(status):
            qry = qry.filter(self.status.in_(status.split(',')))
        if(id):
            qry = qry.filter(self.id.in_(id.split(',')))
        if(search):
            qry = qry.filter(or_(self.title.like('%'+search+'%'), self.description.like('%'+search+'%')))

        data = qry.all()
        user_data = []
        for user in data:
            user_data.append({
                'id': user.id,
                'title': user.title,
                'desc': user.description,
                'status': user.status,
                'status_text':self.status_array[user.status],
                'created_at':user.created_at,
                'completed_at': user.completed_at
            })
        if(not user_data):
            message = "No data found!"
        # Return the list of user data as JSON
        return {
                'status': True,
                'message': message,
                'data': user_data
            }

    @classmethod
    def add_row(self, request):
        """
        Adds a new row to the database with the provided data.

        Args:
            self: The class instance.
            request: The request object containing the JSON data.

        Returns:
            dict: A dictionary containing the status of the operation, a message, and the new ID if the operation was successful, or an error message and an empty list if the operation failed.
        """
        try:
            return_data = {}
            req_data = request.get_json()
            new_todo = Todo(
                title=req_data['title'],
                description=req_data['description'],
                status=req_data['status'],
                created_at = datetime.datetime.now(),
            )
            db.session.add(new_todo)
            db.session.commit()
            new_id = new_todo.id

            if new_id is not None:
                return_data = {
                    'status': True,
                    'message': 'Data added successfully',
                    'new_id': new_id
                }
            else:
                return_data = {
                    'status': False,
                    'message': 'Something Went Wrong !!',
                    'data': []
                }
        except Exception as e:
            return_data = {
                'status': False,
                'message': str(e),
                'data': []
            }

        return return_data

    @classmethod
    def get_row(self, id):
        """
        Fetches specific data and returns it as JSON.
        """
        data = self.query.get(id)
        item = {
                'id': data.id,
                'title': data.title,
                'desc': data.description,
                'status':data.status,
                'status_text':self.status_array[data.status],
                'created_at':data.created_at,
                'completed_at': data.completed_at
            }

        # Return the list of user data as JSON
        return {
            'status': True,
            'message': '',
            'data': item
        }

    @classmethod
    def delete_row(self, request):
        """
        Delete specific data.
        """
        req_data = request.get_json()
        data = self.query.filter(self.id.in_(req_data['id'])).delete()
        print('pop')
        if(data):
            message = 'Item deleted sucessfully!'
        else:
            message = 'Item not found!'

        return {
            'status': True,
            'message': message,
            'data': []
        }