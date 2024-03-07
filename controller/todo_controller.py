import sys
from flask import render_template, redirect, url_for, request, abort,json
from model.todo_model import Todo

def index():
    """
    A function that returns all Todo items.
    """
    return Todo.fetch_all()

def store():
    """
    This function stores todo and returns the result.
    """
    return Todo.add_row(request=request)

def show(id):
    """
    This function return specific todo items.
    """
    return Todo.get_row(id)