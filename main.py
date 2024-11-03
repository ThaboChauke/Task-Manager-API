from os import getenv
from flask import Flask, jsonify
from flask import request
from models import db, Tasks, Users
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///manager.db'
app.config["SECRET_KEY"] = getenv('SECRET_KEY')

db.init_app(app)

with app.app_context():
    db.create_all()

@app.post("/register")
def register():
    data = request.get_json()

    existing_user = Users.query.filter_by(email=data['username']).first()
    if existing_user:
        return jsonify({"error": "Username already exists"}), 400

    existing_email = Users.query.filter_by(email=data['email']).first()
    if existing_email:
        return jsonify({"error": "Email already registered"}), 400

    new_user = Users(name=data['name'], email=data['email'], username=data['username'])
    new_user.set_password(data['password'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success" : "Registration successful" }), 200

@app.post("/login")
def login():
    pass

@app.post("/tasks")
def create_task():
    pass

@app.get("/tasks")
def get_tasks():
    pass

@app.put("/tasks")
def update_task():
    pass

@app.delete("/tasks")
def delete_task():
    pass

if __name__ == "__main__":
    app.run(debug=True)