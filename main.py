from datetime import timedelta, datetime, timezone
from os import getenv
from flask import Flask, jsonify, request, send_from_directory
from models import db, Users, Tasks, TokenBlocklist
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt, \
    get_current_user
from flask_swagger_ui import get_swaggerui_blueprint

from utility import convert_date

load_dotenv()

ACCESS_EXPIRES = timedelta(hours=1)
SWAGGER_URL = '/swagger'
API_DOCS_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_DOCS_URL, config={ 'app_name': 'Task Manager API'})

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
app.config["SECRET_KEY"] = getenv('SECRET_KEY')
app.config["JWT_SECRET_KEY"] = getenv('JWT_SECRET_KEY')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    user_id = jwt_data["sub"]
    return Users.query.get(user_id)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(_jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = TokenBlocklist.query.filter_by(jti=jti).first()
    return token is not None

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static',path)

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
@jwt_required()
def get_tasks():
    current_user = get_jwt_identity()
    tasks = Tasks.query.filter_by(user_id=current_user).all()

    tasks_json = [task.to_json() for task in tasks]

    return jsonify({"tasks": tasks_json}), 200


@app.put("/tasks/<int:task_id>")
@jwt_required()
def update_task(task_id):
    current_user = get_jwt_identity()
    task = Tasks.query.filter_by(id=task_id, user_id=current_user).first()

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid data"}), 400

    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'status' in data:
        task.status = data['status']
    if 'priority' in data:
        task.priority = data['priority']
    if 'due_date' in data:
        task.due_date = convert_date(data['due_date']) if data['due_date'] else None

    db.session.commit()
    return jsonify({"task_id": task.id, "message": "Updated Successfully"}), 200


@app.delete("/tasks/<int:task_id>")
@jwt_required()
def delete_task(task_id):
    current_user = get_jwt_identity()
    task = Tasks.query.filter_by(id=task_id, user_id=current_user).first()  # Corrected here

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"msg": "Task deleted"}), 200


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
    app.run(host='0.0.0.0', port=5000)
