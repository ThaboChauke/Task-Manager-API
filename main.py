from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post("/register")
def register():
    pass

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