import sys
from flask import render_template, redirect, url_for, request, abort,json
from model.Todo import Todo
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def index():
    data = Todo.query.all()
    return {}

def store():
    # print(json.loads(request.data));
    todo_obj = Todo(
            id="1",
            title="Task1",
            description = "desc"
        )
    res = db.session.add(todo_obj)
    db.session.commit()

    print(res)