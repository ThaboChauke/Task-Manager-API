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
{
    "error": "Username already exists"
}

