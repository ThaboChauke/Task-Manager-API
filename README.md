# Task Manager API

This project is a RESTful API for managing user tasks, built with Flask. The API supports user registration, login, and task management features, including task creation, viewing, updating, and deletion. User authentication is handled via JWT tokens, ensuring secure access to protected endpoints.

## Features

- **User RegistrationTask Management API and Login**: Users can register and log in to obtain a JWT token.
- **JWT Authentication**: Secures task management routes, allowing only authenticated users to access their data.
- **Task Management**: Create, view, update, and delete tasks with due dates.

## Endpoints
- Detailed endpoint documentation can be found in the [endpoints.md](endpoints.md) file.

- **`/register`** (`POST`): Register a new user.
- **`/login`** (`POST`): Log in a user and receive a JWT token.
- **`/tasks`**:
  - **`POST`**: Create a new task (JWT-protected).
  - **`GET`**: Fetch tasks for the authenticated user (coming soon).
  - **`PUT`**: Update an existing task (coming soon).
  - **`DELETE`**: Delete a task (coming soon).
---
## Prerequisites

- **Python 3.8+**
- **Flask** and related packages (listed in `requirements.txt`)
- **SQLite** (or another database configured in `SQLALCHEMY_DATABASE_URI`)
---
## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ThaboChauke/Task-Manager-API
   cd Task-Manager-API
   ```

2. **Set up environment variables**: Create a `.env` file with the following keys:
   ```
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

   The API will be available at `http://localhost:5000`.
---
## Usage

Here’s the **Usage** section with headers, payloads, and responses entirely moved to `endpoints.md`:


## Usage

### User Registration
- **Endpoint**: `POST /register`

### User Login
- **Endpoint**: `POST /login`

### Task Creation (JWT-Protected)
- **Endpoint**: `POST /tasks`

---
## Upcoming Features

- **Update Task**: Modify task details.
- **Delete Task**: Remove a task from the database.
---
## License

This project is licensed under the [MIT License](LICENSE).

---

