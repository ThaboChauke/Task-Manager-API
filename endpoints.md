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

#### UnSuccessful Response

- Invalid Password
```json
    {
        "error": "Incorrect password"
    }
```
- Username doesn't exist
```json
    {
        "error": "Username doesnt exist"
    }
```
