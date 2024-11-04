from datetime import timedelta, datetime, timezone
from os import getenv
from flask import Flask, jsonify
from flask import request
from models import db, Users, Tasks, TokenBlocklist
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt, \
    get_current_user

from utility import convert_date

load_dotenv()
ACCESS_EXPIRES = timedelta(hours=1)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SECRET_KEY"] = getenv('SECRET_KEY')
app.config["JWT_SECRET_KEY"] = getenv('JWT_SECRET_KEY')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    user_id = jwt_data["sub"]
    return Users.query.get(user_id)


@app.post("/register")
def register():
    data = request.get_json()

    existing_user = Users.query.filter_by(username=data['username']).first()
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
    data = request.get_json()

    username = data['username']
    password = data['password']

    user = Users.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "Username doesnt exist"}), 400

    if not user.check_password(password=password):
        return jsonify({"error": "Incorrect password"}), 400

    assess_token = create_access_token(identity=user.id)
    return jsonify({"success": "Login successful","token": assess_token}), 200


@app.post("/tasks")
@jwt_required()
def create_task():
    data = request.get_json()
    current_user = get_jwt_identity()
    due_date = convert_date(data['due_date'])

    new_task = Tasks(title=data['title'], description=data['description'], user_id=current_user, due_date=due_date)

    db.session.add(new_task)
    db.session.commit()

    return jsonify({"msg": "Task created"}), 201


@app.get("/tasks")
def get_tasks():
    pass

@app.put("/tasks")
def update_task():
    pass

@app.delete("/tasks")
def delete_task():
    pass


@app.route("/logout", methods=["DELETE"])
@jwt_required(verify_type=False)
def modify_token():
    token = get_jwt()
    jti = token["jti"]
    ttype = token["type"]
    now = datetime.now(timezone.utc)

    current_user = get_current_user()  # This now works since user_lookup_loader is defined
    token_block = TokenBlocklist(jti=jti, type=ttype, user_id=current_user.id, created_at=now)

    db.session.add(token_block)
    db.session.commit()
    return jsonify({"msg": "token successfully revoked"})


if __name__ == "__main__":
    app.run(debug=True)