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

---

## 📚 Endpoints

- Detailed endpoint documentation, including request headers, payloads, and responses, can be found in [`endpoints.md`](endpoints.md).
- Access endpoints in Postman

    [<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://god.gw.postman.com/run-collection/34710539-c41de9a5-19a5-4daf-bcd1-9146f5cfc31a?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D34710539-c41de9a5-19a5-4daf-bcd1-9146f5cfc31a%26entityType%3Dcollection%26workspaceId%3Dae458e47-48f9-4540-8629-8b6de6c7df43)

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