# Endpoints for the Task Manager Api


## Post `/register`

- hit this endpoint to register new users

#### Request:

```json
    {
      "name": "John Doe",
      "email": "johndoe@email.com",
      "username": "johnny",
      "password": "password123"
    }
```

#### Successful Response

```json
    {
      "success": "Registration successful"
    }
```
#### Unsuccessful Response

- Email already registered
```json
    {
      "error": "Email already registered"
    }
```
- Username already taken
```json
    {
        "error": "Username already exists"
    }
```

## Post `/login`
- hit this endpoint to login

#### Request:

```json
    {
      "password": "password123",
      "username": "johnny"
    }
```

#### Successful Response

```json
    {
        "success": "Login successful",
        "token": "token..."
    }
```

#### Unsuccessful Response

- Invalid Password
```json
    {
        "error": "Incorrect password"
    }
```
- Username doesn't exist{
    "msg": "token successfully revoked"
}
```json
    {
        "error": "Username doesnt exist"
    }
```

## Delete `/logout`

- hit this endpoint to logout

#### Request
- Authorization token is required for this endpoint

```http request
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
```

#### Response
```json
    {
        "msg": "token successfully revoked"
    }
```

## Post `/tasks`
- hit this endpoint to create a task

#### Request:
- Authorization token is required for this endpoint

```http request
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
```

```json
{
    "title": "Finish Flask Project",
    "description": "Complete all remaining routes and test cases",
    "due_date": "2024-12-01 18:00",
    "priority(optional)" : "low, medium(default), high"
}
```

#### Successful Response:

```json
    {
        "msg": "Task created"
    }
```

#### Unsuccessful Response
- No Auth header
```json
    {
        "msg": "Missing Authorization Header"
    }
```

- Invalid token/key
```json
{
    "msg": "Signature verification failed"
}
```

- Expired token
```json
    {
        "msg": "Token has expired"
    }
```

## Get `/tasks`
- hit this endpoint to get all tasks

#### Request:
- Authorization token is required for this endpoint

```http request
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
```

#### Successful Response:
```json
{
    "tasks": [
        {
            "description": "Complete all remaining routes and test cases",
            "due_date": "2024-12-01T08:00:00",
            "id": 1,
            "priority": "Medium",
            "status": "Pending",
            "title": "Finish Flask Project",
            "user_id": 1
        }
    ]
}
```

#### Unsuccessful Response
- No Auth header
```json
    {
        "msg": "Missing Authorization Header"
    }
```

- Invalid token/key
```json
{
    "msg": "Signature verification failed"
}
```

- Expired token
```json
    {
        "msg": "Token has expired"
    }
```

## Put `/tasks/{task_id}`

- hit this endpoint to update task

#### Request:

- Authorization token is required for this endpoint

```http request
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
```

- title & status
```json
    {
    "title": "New Task Title",
    "status": "In Progress"
    }
```

- all fields

```json
    {
        "title": "Complete the report",
        "description": "Finish the quarterly report and send it to the manager.",
        "status": "Completed",
        "priority": "Medium",
        "due_date": "2024-11-15 17:00"
    }
```

- due date only

```json
    {
        "due_date": "2024-11-20 09:00"
    }
```

#### Successful Response

```json
    {
        "message": "Updated Successfully",
        "task_id": 1
    }
```

#### Unsuccessful Response

- Task not found

```json
  {
      "error": "Task not found"
  }
```

- Empty request body

```json
    {
        "error": "Invalid data"
    }
```

## Delete `/tasks/{task_id}`

- hit this endpoint to delete a task

#### Request:

- Authorization token is required for this endpoint

```http request
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
```

#### Successful Response

```json
    {
        "msg": "Task deleted"
    }
```
#### Unsuccessful Response

```json
    {
        "error": "Task not found"
    }
```