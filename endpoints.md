# Endpoints for the Task Manager Api


## Post `/register`

- hit this endpoint to register new users

#### Request:

```json
    {
      "name": "John Doe",
      "email": "johndoe@email.com",
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
    "due_date": "2024-12-01",
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

## Get `/tasks`
- hit this endpoint to get all tasks

#### Request:
- Authorization token is required for this endpoint

```http request
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
```

#### Response:
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