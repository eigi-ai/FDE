# 01 FastAPI Tutorial — Full Documentation

This document explains **everything** used in this project, in plain simple language. No jargon, no fluff.

---

## Table of Contents

1. [What is an API?](#1-what-is-an-api)
2. [What is FastAPI?](#2-what-is-fastapi)
3. [What is Pydantic?](#3-what-is-pydantic)
4. [What is OAuth2 Bearer?](#4-what-is-oauth2-bearer)
5. [What is JWT?](#5-what-is-jwt)
6. [What is Uvicorn?](#6-what-is-uvicorn)
7. [What is Starlette?](#7-what-is-starlette)
8. [What is requirements.txt?](#8-what-is-requirementstxt)
9. [Package-by-Package Breakdown](#9-package-by-package-breakdown)
10. [Project File Breakdown](#10-project-file-breakdown)
11. [How the Auth Flow Works](#11-how-the-auth-flow-works)
12. [In-Memory Store vs Database](#12-in-memory-store-vs-database)
13. [API Flow Diagrams](#13-api-flow-diagrams)
14. [How to Run the Project](#14-how-to-run-the-project)
15. [Exercises](#15-exercises)

---

## 1. What is an API?

An **API (Application Programming Interface)** is like a waiter at a restaurant.

- You (the client) tell the waiter (the API) what you want.
- The waiter goes to the kitchen (the server/database) and gets it.
- The waiter brings the result back to you.

In code terms: your frontend (or another app) sends an HTTP request to an API endpoint (like `/v1/users`), and the API sends back data (usually JSON).

---

## 2. What is FastAPI?

**FastAPI** is a Python framework for building APIs — fast and with very little code.

Think of it as a set of tools that handles the boring parts for you:

- Receives HTTP requests (GET, POST, etc.)
- Validates the incoming data automatically
- Converts Python objects to JSON responses
- Generates interactive API docs at `/docs` (Swagger UI) for free

**Example from this project:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"response": "ping to user dashboard"}
```

When someone visits `http://localhost:8000/`, they get `{"response": "ping to user dashboard"}` back.

**Why FastAPI over Flask or Django?**

- Much faster to write
- Built-in data validation via Pydantic
- Automatic API documentation
- Supports async out of the box

---

## 3. What is Pydantic?

**Pydantic** is the data validation library that FastAPI uses under the hood.

You write a class, define what fields it should have and what types they are, and Pydantic:

- Checks that incoming data matches the types you defined
- Gives a clear error if something is wrong (e.g., email is missing)
- Converts raw JSON into a proper Python object

**Example from this project:**

```python
from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    mobile_number: str
    password: str
```

If someone sends a request without `email`, FastAPI+Pydantic automatically returns a `422 Unprocessable Entity` error explaining what's missing. You don't write that logic yourself.

**`model_dump()`** — converts the Pydantic object into a plain Python dictionary:

```python
request = request.model_dump()
# Now request["email"], request["password"] etc. work like a normal dict
```

**`Field(exclude=True)`** — tells Pydantic to skip a field when serializing (e.g., don't include `password` in API responses):

```python
password: Optional[str] = Field(default=None, exclude=True)
```

---

## 4. What is OAuth2 Bearer?

**OAuth2** is a standard way to handle authorization. The "Bearer" part means:

> "Whoever _bears_ (carries) this token is allowed in."

In this project:

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/login")
```

This does two things:

1. On protected routes, it automatically reads the `Authorization: Bearer <token>` header from incoming requests.
2. It tells Swagger UI (`/docs`) to show an "Authorize" button pointing to `/v1/login` so you can log in and test protected routes directly from the browser.

**How the client uses it:**

After login, the client gets an `access_token`. For every subsequent request to a protected route, it sends:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

If the header is missing → FastAPI returns `401 Unauthorized` automatically.

---

## 5. What is JWT?

**JWT (JSON Web Token)** is the format of the access token we create after login.

It looks like this:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEyMyIsImVtYWlsIjoidGVzdEBleGFtcGxlLmNvbSIsImV4cGlyZXMiOjE3MTk1MDAwMDB9.abc123signature
```

It has 3 parts separated by dots:

- **Header** — which algorithm is used (e.g., HS256)
- **Payload** — the actual data (user id, email, expiry time)
- **Signature** — a hash that proves the token hasn't been tampered with

**The server never stores the token.** It just checks the signature when the token arrives. If the signature is valid and the token hasn't expired, the user is authenticated.

**From `auth.py` in this project:**

```python
def signJWT(id, email, expiry_duration):
    payload = {
        "id": id,
        "email": email,
        "expires": time.time() + expiry_duration,  # current time + 3600 seconds (1 hour)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
```

`JWT_SECRET` is a secret string only the server knows. It's used to sign and verify tokens. Never expose it.

---

## 6. What is Uvicorn?

**Uvicorn** is the server that actually runs your FastAPI app.

Think of FastAPI as the engine of a car — it doesn't move on its own. Uvicorn is the driver that starts it and handles traffic.

```bash
uvicorn main:app --reload
```

- `main` → the filename (`main.py`)
- `app` → the FastAPI instance inside that file (`app = FastAPI()`)
- `--reload` → restarts automatically when you save a file (only for development)

**`[standard]` extra** (in `uvicorn[standard]`): installs extra packages for better performance — like `httptools` for faster HTTP parsing and `uvloop` for faster async event loop.

---

## 7. What is Starlette?

**Starlette** is the foundation that FastAPI is built on top of.

You don't interact with it directly — FastAPI wraps it. But it handles:

- Routing (matching URLs to your functions)
- Middleware (code that runs on every request)
- Request and response objects
- WebSockets, background tasks, static files

FastAPI adds Pydantic validation, auto-docs, and dependency injection on top of Starlette.

---

## 8. What is `requirements.txt`?

`requirements.txt` is a plain text file that lists all the Python packages your project needs.

When someone clones your project and runs:

```bash
pip install -r requirements.txt
```

Python installs exactly those packages at exactly those versions. This ensures everyone on the team (and your production server) runs the same code.

**Version pinning:**

- `==0.39.0` → exact version, no surprises
- `>=0.129.0` → any version at or above this (useful when you want security updates)

---

## 9. Package-by-Package Breakdown

| Package             | What it does in this project                                                  |
| ------------------- | ----------------------------------------------------------------------------- |
| `fastapi`           | The web framework — defines routes, handles HTTP, generates docs              |
| `uvicorn[standard]` | The ASGI server that runs FastAPI; `[standard]` adds performance extras       |
| `starlette`         | The low-level toolkit FastAPI is built on (routing, middleware, etc.)         |
| `httpx`             | HTTP client for making requests to _other_ APIs from Python code (async-safe) |
| `pydantic`          | Validates and structures request/response data using Python type hints        |
| `cryptography`      | Low-level crypto library; required by `PyJWT` and `passlib` internally        |
| `PyJWT`             | Creates and decodes JWT tokens for authentication                             |
| `passlib[bcrypt]`   | Handles password hashing; `[bcrypt]` enables the bcrypt algorithm             |
| `bcrypt`            | The actual bcrypt hashing algorithm used by passlib to hash passwords         |
| `python-dotenv`     | Loads environment variables from the `.env` file into `os.environ`            |

---

## 10. Project File Breakdown

### `main.py`

The core of the app. Contains:

- The `FastAPI` app instance
- All Pydantic models (data shapes)
- All route handlers (the actual API endpoints)
- In-memory `users = []` list acting as a temporary database

**Routes:**
| Method | Path | Auth Required | What it does |
|--------|------|--------------|--------------|
| `GET` | `/` | No | Health check / ping |
| `GET` | `/v1/users` | Yes | List all users (paginated) |
| `GET` | `/v1/users/{user_id}` | Yes | Get one user by ID |
| `POST` | `/v1/users` | No | Register a new user |
| `POST` | `/v1/login` | No | Login and get a token |
| `POST` | `/v1/reset-password` | Yes | Change password |

### `auth.py`

All authentication logic in one place:

- `encrypt_password(password)` — hashes a plain password using bcrypt before storing
- `verify_hash_password(plain, hashed)` — checks if a login password matches the stored hash
- `signJWT(id, email, expiry)` — creates a JWT token for a user after login
- `decodeJWT(token)` — decodes and validates a JWT, returns `None` if invalid/expired
- `encodePayload(payload)` — generic JWT encoder for any payload

### `requirements.txt`

Lists all Python packages the project depends on (see Section 9).

### `.env`

Stores secret config values that should NOT be hardcoded in code:

```
secret=your-jwt-secret-key
algorithm=HS256
```

These are loaded by `python-dotenv` and read with `os.environ.get("secret")`.

### `index.html`

A simple frontend UI to interact with the API from the browser without needing Postman or curl.

---

## 11. In-Memory Store vs Database

### What is an In-Memory Store?

In this project, all users are stored in a plain Python list:

```python
users = []  # lives in RAM while the server is running
```

When you call `POST /v1/users`, the new user is appended to this list. When you call `GET /v1/users`, it reads from this list. That's it — no database, no files, no disk.

This is called an **in-memory store** because the data lives only in the computer's memory (RAM).

---

### What is a Database Store?

A **database** (like PostgreSQL, MySQL, MongoDB, SQLite) stores data on disk permanently. The data survives:

- Server restarts
- Crashes
- Deployments

To use a database with FastAPI you would typically add:

- `SQLAlchemy` or `SQLModel` — to talk to a SQL database from Python
- `databases` or `asyncpg` — for async database queries
- A real DB like PostgreSQL running separately

Instead of `users.append(...)` you would do:

```python
db.add(new_user)
db.commit()
```

---

### Side-by-Side Comparison

|                                  | In-Memory (`users = []`)              | Real Database (e.g. PostgreSQL)            |
| -------------------------------- | ------------------------------------- | ------------------------------------------ |
| **Setup**                        | Zero — just a Python list             | Needs installation, connection config      |
| **Speed**                        | Extremely fast (RAM access)           | Fast, but slightly slower (disk + network) |
| **Data survives restart?**       | ❌ No — wiped on every restart        | ✅ Yes — persisted to disk                 |
| **Multiple servers?**            | ❌ No — each server has its own copy  | ✅ Yes — all servers share one DB          |
| **Scales to millions of users?** | ❌ No — RAM is limited                | ✅ Yes — designed for this                 |
| **Good for learning?**           | ✅ Yes — no setup, easy to understand | Adds complexity early on                   |
| **Good for production?**         | ❌ Never                              | ✅ Always                                  |

---

### Why We Use It Here

For this tutorial the in-memory list is intentional:

1. **Zero setup** — you don't need to install Postgres or configure anything to run the project.
2. **Focus on FastAPI** — the goal is to learn routing, Pydantic, auth, and JWT — not database ORM syntax.
3. **Easy to inspect** — you can `print(users)` at any time and see exactly what's stored.
4. **Fast feedback** — restart the server and you start with a clean slate, which is useful during development.

---

### The Big Catch

> **Every time you restart the server, all users are gone.**

This means:

- You can't persist login sessions across restarts
- You can't deploy this to production and keep user data
- Two running instances of the app would have completely separate user lists

This is 100% fine for a tutorial. In a real app you would swap `users = []` for a database table.

---

### What the Migration Would Look Like

```python
# In-memory (current)
users = []
users.append(user_dict)                          # create
next(u for u in users if u["id"] == id)          # read
user["password"] = new_hash                      # update

# With a real DB (SQLAlchemy example)
db.add(UserModel(**user_dict))                   # create
db.query(UserModel).filter_by(id=id).first()     # read
db.query(UserModel).filter_by(id=id).update(...) # update
db.commit()                                      # save to disk
```

The FastAPI route logic stays almost identical — only the storage layer changes.

---

## 12. How the Auth Flow Works

```
1. Register
   POST /v1/users  →  password gets hashed and stored  →  returns access_token

2. Login
   POST /v1/login  →  password verified against hash  →  returns access_token

3. Access protected route
   GET /v1/users
   Header: Authorization: Bearer <access_token>
   →  FastAPI extracts token via oauth2_scheme
   →  decodeJWT() validates it
   →  if valid: returns data
   →  if invalid/missing: 401 Unauthorized

4. Reset Password
   POST /v1/reset-password
   Header: Authorization: Bearer <access_token>
   Body: { old_password, new_password }
   →  token identifies the user
   →  old password verified
   →  new password hashed and stored
```

---

## 13. API Flow Diagrams

### Overall API Map

```mermaid
flowchart TD
    Client([Client / Browser])

    Client -->|GET /| PING["`**GET /**
    Health Check
    No auth needed`"]

    Client -->|POST /v1/users| REGISTER
    Client -->|POST /v1/login| LOGIN

    Client -->|GET /v1/users| GUARD1{Valid JWT?}
    Client -->|GET /v1/users/:id| GUARD2{Valid JWT?}
    Client -->|POST /v1/reset-password| GUARD3{Valid JWT?}

    GUARD1 -->|No| E401_1[401 Unauthorized]
    GUARD1 -->|Yes| LISTUSERS["`Return paginated
    users list`"]

    GUARD2 -->|No| E401_2[401 Unauthorized]
    GUARD2 -->|Yes| GETUSER{User exists?}
    GETUSER -->|No| E404[404 Not Found]
    GETUSER -->|Yes| RETURNUSER[Return user object]

    GUARD3 -->|No| E401_3[401 Unauthorized]
    GUARD3 -->|Yes| RESETPW[Reset Password flow]

    style E401_1 fill:#ff4d4d,color:#fff
    style E401_2 fill:#ff4d4d,color:#fff
    style E401_3 fill:#ff4d4d,color:#fff
    style E404 fill:#ff944d,color:#fff
    style PING fill:#4da6ff,color:#fff
    style LISTUSERS fill:#4dbb6e,color:#fff
    style RETURNUSER fill:#4dbb6e,color:#fff
```

---

### POST /v1/users — Register a New User

```mermaid
sequenceDiagram
    participant C as Client
    participant F as FastAPI
    participant P as Pydantic
    participant A as auth.py
    participant DB as users[] list

    C->>F: POST /v1/users<br/>{first_name, last_name, email, mobile_number, password}
    F->>P: Validate request body
    alt Validation fails
        P-->>C: 422 Unprocessable Entity
    end
    F->>DB: Check if email already exists
    alt Email taken
        F-->>C: 400 Bad Request — "User already exists"
    end
    F->>A: encrypt_password(password)
    A-->>F: bcrypt hashed password
    F->>DB: Append new user dict
    F->>A: signJWT(user_id, email, 3600)
    A-->>F: access_token (JWT)
    F-->>C: 200 OK — UserResponse + access_token
```

---

### POST /v1/login — Login

```mermaid
sequenceDiagram
    participant C as Client
    participant F as FastAPI
    participant A as auth.py
    participant DB as users[] list

    C->>F: POST /v1/login<br/>{email, password}
    F->>DB: Find user by email
    alt User not found
        F-->>C: 404 Not Found
    end
    F->>A: verify_hash_password(plain, hashed)
    alt Password wrong
        F-->>C: 401 Unauthorized — "Invalid Credentials"
    end
    F->>A: signJWT(user_id, email, 3600)
    A-->>F: access_token (JWT)
    F-->>C: 200 OK — UserResponse + access_token
```

---

### GET /v1/users — List Users (Protected)

```mermaid
sequenceDiagram
    participant C as Client
    participant F as FastAPI
    participant O as oauth2_scheme
    participant A as auth.py
    participant DB as users[] list

    C->>F: GET /v1/users?page=1&page_size=10<br/>Authorization: Bearer <token>
    F->>O: Extract token from header
    alt Header missing
        O-->>C: 401 Unauthorized (automatic)
    end
    F->>A: decodeJWT(token)
    alt Token invalid or expired
        F-->>C: 401 Unauthorized
    end
    F->>DB: Slice users[start:end] for pagination
    F-->>C: 200 OK — list of users
```

---

### GET /v1/users/{user_id} — Get One User (Protected)

```mermaid
sequenceDiagram
    participant C as Client
    participant F as FastAPI
    participant A as auth.py
    participant DB as users[] list

    C->>F: GET /v1/users/abc-123<br/>Authorization: Bearer <token>
    F->>A: decodeJWT(token)
    alt Token invalid
        F-->>C: 401 Unauthorized
    end
    F->>DB: Find user where id == "abc-123"
    alt Not found
        F-->>C: 404 Not Found
    end
    F-->>C: 200 OK — user object
```

---

### POST /v1/reset-password — Reset Password (Protected)

```mermaid
sequenceDiagram
    participant C as Client
    participant F as FastAPI
    participant A as auth.py
    participant DB as users[] list

    C->>F: POST /v1/reset-password<br/>Authorization: Bearer <token><br/>{old_password, new_password}
    F->>A: decodeJWT(token)
    alt Token invalid
        F-->>C: 401 Unauthorized
    end
    F->>DB: Find user by id from token payload
    alt User not found
        F-->>C: 404 Not Found
    end
    F->>A: verify_hash_password(old_password, stored_hash)
    alt Wrong old password
        F-->>C: 401 — "Invalid Credentials"
    end
    F->>A: encrypt_password(new_password)
    A-->>F: new bcrypt hash
    F->>DB: Update user password + updated_at
    F-->>C: 200 OK — {message: "Password reset successful."}
```

---

## 14. How to Run the Project

```bash
# 1. Create and activate venv with Python 3.13
python3.13 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables (edit .env file)
# secret=your-secret-key
# algorithm=HS256

# 4. Start the server
uvicorn main:app --reload

# 5. Open in browser
# API docs (Swagger):  http://127.0.0.1:8000/docs
# Frontend UI:         open index.html in your browser
```

---

> **Key Takeaway:** FastAPI + Pydantic handle the HTTP and validation layer. PyJWT + Passlib handle the security layer. Uvicorn is what actually runs it all. They are separate tools that work together.

---

## 15. Exercises

These exercises extend what you built in `main.py`. You have all the building blocks — apply them.

---

### Exercise 1 — Forgot Password (OTP via Email)

A user forgot their password. They should be able to request a one-time password (OTP) sent to their email, then use it to set a new password.

**You need to build two APIs:**

#### API 1 — `POST /v1/forgot-password`

**What it does:** Receives an email, generates an OTP, and "sends" it to the user.

**Request body:**

```json
{
  "email": "user@example.com"
}
```

**Steps to implement:**

1. Check if a user with that email exists in the `users` list. If not → `404`.
2. Generate a 6-digit OTP (hint: use `random.randint(100000, 999999)`).
3. Store the OTP temporarily — add an `otp` and `otp_expires` field on the user dict.
4. Set `otp_expires` to `time.time() + 300` (valid for 5 minutes).
5. For now, instead of a real email, just return the OTP in the response (simulate sending).

**Expected response:**

```json
{
  "message": "OTP sent to your email.",
  "otp": 482910
}
```

> In a real app you would send the OTP via an email service (e.g. SendGrid, AWS SES) and NOT return it in the response. Returning it here is only for testing.

---

#### API 2 — `POST /v1/forgot-password/verify`

**What it does:** Receives the email, OTP, and new password. If OTP is correct and not expired, updates the password.

**Request body:**

```json
{
  "email": "user@example.com",
  "otp": 482910,
  "new_password": "myNewPassword123"
}
```

**Steps to implement:**

1. Find the user by email → `404` if not found.
2. Check that `user["otp"]` matches the submitted OTP → `401` if wrong.
3. Check that `time.time() < user["otp_expires"]` → `400 OTP expired` if too late.
4. Hash the new password using `encrypt_password()`.
5. Update `user["password"]`, clear `user["otp"]` and `user["otp_expires"]`, update `updated_at`.
6. Return a success message.

**Expected response:**

```json
{
  "message": "Password updated successfully."
}
```

**Flow diagram:**

```mermaid
sequenceDiagram
    participant C as Client
    participant F as FastAPI
    participant DB as users[] list
    participant A as auth.py

    C->>F: POST /v1/forgot-password {email}
    F->>DB: Find user by email
    alt Not found
        F-->>C: 404 Not Found
    end
    F->>F: Generate 6-digit OTP
    F->>DB: Store OTP + otp_expires on user
    F-->>C: 200 OK — {message, otp}

    C->>F: POST /v1/forgot-password/verify {email, otp, new_password}
    F->>DB: Find user by email
    F->>F: Check OTP matches
    alt Wrong OTP
        F-->>C: 401 Unauthorized
    end
    F->>F: Check OTP not expired
    alt Expired
        F-->>C: 400 Bad Request — OTP expired
    end
    F->>A: encrypt_password(new_password)
    F->>DB: Update password, clear OTP
    F-->>C: 200 OK — Password updated
```

---

### Exercise 2 — Login with OTP

Instead of a password, the user gets a one-time code sent to their email and uses that to log in.

**You need to build two APIs:**

#### API 1 — `POST /v1/otp-login/request`

**What it does:** Receives an email and sends an OTP to it.

**Request body:**

```json
{
  "email": "user@example.com"
}
```

**Steps to implement:**

1. Find the user by email → `404` if not found.
2. Generate a 6-digit OTP.
3. Store `otp` and `otp_expires` (5-minute expiry) on the user dict.
4. Return a success message (and the OTP for testing purposes).

**Expected response:**

```json
{
  "message": "OTP sent to your email.",
  "otp": 719234
}
```

---

#### API 2 — `POST /v1/otp-login/verify`

**What it does:** Receives the email and OTP. If valid, logs the user in and returns a JWT token.

**Request body:**

```json
{
  "email": "user@example.com",
  "otp": 719234
}
```

**Steps to implement:**

1. Find the user by email → `404` if not found.
2. Check OTP matches → `401` if wrong.
3. Check OTP is not expired → `400` if expired.
4. Clear the OTP fields from the user dict.
5. Call `signJWT(user["id"], user["email"], 3600)` to issue a token.
6. Return the user details and the access token (same shape as the login response).

**Expected response:**

```json
{
  "id": "uuid-here",
  "first_name": "John",
  "email": "user@example.com",
  "access_token": "eyJ..."
}
```

**Flow diagram:**

```mermaid
sequenceDiagram
    participant C as Client
    participant F as FastAPI
    participant DB as users[] list
    participant A as auth.py

    C->>F: POST /v1/otp-login/request {email}
    F->>DB: Find user by email
    alt Not found
        F-->>C: 404 Not Found
    end
    F->>F: Generate 6-digit OTP
    F->>DB: Store OTP + otp_expires on user
    F-->>C: 200 OK — {message, otp}

    C->>F: POST /v1/otp-login/verify {email, otp}
    F->>DB: Find user by email
    F->>F: Check OTP matches
    alt Wrong OTP
        F-->>C: 401 Unauthorized
    end
    F->>F: Check OTP not expired
    alt Expired
        F-->>C: 400 Bad Request — OTP expired
    end
    F->>DB: Clear OTP fields
    F->>A: signJWT(id, email, 3600)
    A-->>F: access_token
    F-->>C: 200 OK — UserResponse + access_token
```

---

### Hints & Tips

| Task                   | Hint                                                                         |
| ---------------------- | ---------------------------------------------------------------------------- |
| Generate OTP           | `import random` → `random.randint(100000, 999999)`                           |
| OTP expiry             | `time.time() + 300` stores a Unix timestamp 5 min in the future              |
| Check expiry           | `if time.time() > user["otp_expires"]:` → expired                            |
| Clear OTP after use    | `user["otp"] = None` and `user["otp_expires"] = None`                        |
| New Pydantic models    | Create `ForgotPasswordRequest`, `VerifyOTPRequest`, `OTPLoginRequest` models |
| Reuse existing helpers | `encrypt_password()`, `signJWT()`, `UserResponse` are already in your code   |
