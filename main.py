import json
from model.Todo import Todo
from flask import Flask,render_template
from flask_migrate import Migrate
from model.Todo import db
from routes import route_bp

app = Flask(__name__,template_folder='resources/templates')
app.config.from_object('const')

app.register_blueprint(route_bp, url_prefix='/todo')

db.init_app(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"), debug=True)