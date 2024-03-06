import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
dbdir = basedir + "/database"
# Enable debug mode.
DEBUG = True
# Connect to the database
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(dbdir , 'todo.db')
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False


STATIC_FOLDER='resources/static'
TEMPLATE_FOLDER='resources/templates'