# 📝 Task Manager API

A RESTful API built with Flask, designed for managing user tasks. This API supports user registration, login, and task management features, all protected with JWT authentication for secure access to user-specific data.

## 🌟 Features

- **User Registration & Login**: Users can register and log in to obtain a JWT token.
- **JWT Authentication**: Protects task management routes, ensuring only authenticated users can access their data.
- **Task Management**: Authenticated users can create, view, update, and delete tasks, with optional due dates.

---

## 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ThaboChauke/Task-Manager-API
   cd Task-Manager-API
   ```

2. **Set up environment variables**: Create a `.env` file in the root directory with the following keys:
   ```plaintext
   DATABASE_URL=<your-database-url>
   SECRET_KEY=<your-secret-key>
   JWT_SECRET_KEY=<your-jwt-secret-key>
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   flask run
   ```

5. The API will be available at `http://localhost:5000`.


### Running with Docker

1. Build the Docker image:

    ```bash
        docker build -t myapp .
    ```
2. Run the container:

    ```bash
        sudo docker run --env-file .env -p 5000:5000 myapp
    ```
3. The API will now be accessible at http://localhost:5000.

---

### GitHub Actions Workflow
The CI pipeline is set up to run unit tests automatically using the workflow defined in [yml file](.github/workflows/python-app.yml). Every time code is pushed to the repository, the workflow triggers and executes the tests.

## 📚 Endpoints

- Detailed endpoint documentation, including request headers, payloads, and responses, can be found in [`endpoints.md`](endpoints.md).
- Access endpoints in Swagger

    [![Swagger UI](https://img.shields.io/badge/Swagger-UI-green)](https://task-manager-api-o274.onrender.com/swagger/)

### Summary of Endpoints

- **User Registration**: `POST /register`
- **User Login**: `POST /login`
- **Task Management**:
  - `POST /tasks`: Create a new task (JWT-protected)
  - `GET /tasks`: Fetch all tasks for the authenticated user
  - `PUT /tasks/<task_id>`: Update a specific task
  - `DELETE /tasks/<task_id>`: Delete a specific task
  - **Logout**: `DELETE /logout` (JWT-protected, revokes token)

---

## 🧩 Prerequisites

- **Python 3.8+**
- **Flask** and related packages (installed via `requirements.txt`)
- **SQLite** (or another configured database)
- **Docker**


---

## 📘 Usage Overview

The full **Usage** section, with headers, payloads, and responses, has been moved to `endpoints.md` for clarity. Here’s a quick summary:

### User Registration
- **Endpoint**: `POST /register`

### User Login
- **Endpoint**: `POST /login`

### Task Management (JWT-Protected)
- **Create Task**: `POST /tasks`
- **View Tasks**: `GET /tasks`
- **Update Task**: `PUT /tasks/<task_id>`
- **Delete Task**: `DELETE /tasks/<task_id>`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👥 Contributing

Contributions are welcome! Please follow the typical [GitHub flow](https://guides.github.com/introduction/flow/) and submit a pull request for any additions or improvements.

---

Enjoy building and managing tasks with the Task Manager API!