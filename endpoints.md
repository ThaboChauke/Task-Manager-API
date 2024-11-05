# Endpoints Documentation for Task Manager API

This document provides details on all endpoints available in the Task Manager API.

---

### 1. **POST** `/register`
Register a new user.

#### Request:
```json
{
  "name": "John Doe",
  "email": "johndoe@email.com",
  "username": "johnny",
  "password": "password123"
}
```

#### Success Response:
```json
{
  "success": "Registration successful"
}
```

#### Error Responses:
- **Email already registered**
  ```json
  {
    "error": "Email already registered"
  }
  ```
- **Username already taken**
  ```json
  {
    "error": "Username already exists"
  }
  ```

---

### 2. **POST** `/login`
Log in an existing user.

#### Request:
```json
{
  "username": "johnny",
  "password": "password123"
}
```

#### Success Response:
```json
{
  "success": "Login successful",
  "token": "token..."
}
```

#### Error Responses:
- **Incorrect Password**
  ```json
  {
    "error": "Incorrect password"
  }
  ```
- **Username doesn't exist**
  ```json
  {
    "error": "Username doesnt exist"
  }
  ```

---

### 3. **DELETE** `/logout`
Log out and revoke the JWT token.

#### Request:
- **Authorization Header**: Required
  ```http
  Authorization: Bearer <JWT_TOKEN>
  ```

#### Response:
```json
{
  "msg": "token successfully revoked"
}
```

---

### 4. **POST** `/tasks`
Create a new task.

#### Request:
- **Authorization Header**: Required
  ```http
  Authorization: Bearer <JWT_TOKEN>
  ```

```json
{
  "title": "Finish Flask Project",
  "description": "Complete all remaining routes and test cases",
  "due_date": "2024-12-01 18:00",
  "priority": "medium"
}
```

#### Success Response:
```json
{
  "msg": "Task created"
}
```

#### Error Responses:
- **Missing Authorization Header**
  ```json
  {
    "msg": "Missing Authorization Header"
  }
  ```
- **Invalid Token/Signature verification failed**
  ```json
  {
    "msg": "Signature verification failed"
  }
  ```
- **Token Expired**
  ```json
  {
    "msg": "Token has expired"
  }
  ```

---

### 5. **GET** `/tasks`
Retrieve all tasks for the authenticated user.

#### Request:
- **Authorization Header**: Required
  ```http
  Authorization: Bearer <JWT_TOKEN>
  ```

#### Success Response:
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Finish Flask Project",
      "description": "Complete all remaining routes and test cases",
      "due_date": "2024-12-01T08:00:00",
      "priority": "Medium",
      "status": "Pending",
      "user_id": 1
    }
  ]
}
```

#### Error Responses:
- **Missing Authorization Header**
  ```json
  {
    "msg": "Missing Authorization Header"
  }
  ```
- **Invalid Token/Signature verification failed**
  ```json
  {
    "msg": "Signature verification failed"
  }
  ```
- **Token Expired**
  ```json
  {
    "msg": "Token has expired"
  }
  ```

---

### 6. **PUT** `/tasks/{task_id}`
Update a specific task.

#### Request:
- **Authorization Header**: Required
  ```http
  Authorization: Bearer <JWT_TOKEN>
  ```

##### Examples:

- **Update title and status**:
  ```json
  {
    "title": "New Task Title",
    "status": "In Progress"
  }
  ```

- **Update all fields**:
  ```json
  {
    "title": "Complete the report",
    "description": "Finish the quarterly report and send it to the manager.",
    "status": "Completed",
    "priority": "Medium",
    "due_date": "2024-11-15 17:00"
  }
  ```

- **Update due date only**:
  ```json
  {
    "due_date": "2024-11-20 09:00"
  }
  ```

#### Success Response:
```json
{
  "message": "Updated Successfully",
  "task_id": 1
}
```

#### Error Responses:
- **Task not found**
  ```json
  {
    "error": "Task not found"
  }
  ```
- **Invalid data**
  ```json
  {
    "error": "Invalid data"
  }
  ```

---

### 7. **DELETE** `/tasks/{task_id}`
Delete a specific task.

#### Request:
- **Authorization Header**: Required
  ```http
  Authorization: Bearer <JWT_TOKEN>
  ```

#### Success Response:
```json
{
  "msg": "Task deleted"
}
```

#### Error Response:
- **Task not found**
  ```json
  {
    "error": "Task not found"
  }
  ```

---