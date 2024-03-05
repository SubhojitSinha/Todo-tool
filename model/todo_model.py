from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String(500))

    @property
    def serialize(self):
        """
        Property function to serialize the object into a dictionary.
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

    @classmethod
    def fetch_all(self):
        """
        Fetches all the user data and returns it as JSON.
        """
        data = self.query.all()
        user_data = []
        for user in data:
            user_data.append({
                'id': user.id,
                'title': user.title,
                'desc': user.description
            })

        # Return the list of user data as JSON
        return user_data

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
                description=req_data['description']
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