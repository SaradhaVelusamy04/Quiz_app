Absolutely! Here's a professional, beginner-friendly `README.md` for your Quiz App project using FastAPI and SQLAlchemy:

---

# Quiz App API

A simple **Quiz Application backend** built with **FastAPI**, **SQLAlchemy**, and **SQLite**. This API allows users to **register, login, create questions, fetch questions, and save quiz results**.

---

## Features

* User registration & authentication
* Create, fetch, and delete quiz questions
* Save and view quiz results
* FastAPI Swagger UI for testing endpoints
* SQLite database for storage
* Passwords securely hashed with **bcrypt**

---

## Technologies Used

* **Python 3.11+**
* **FastAPI** – API framework
* **SQLAlchemy** – ORM for database management
* **SQLite** – Lightweight database
* **Passlib (bcrypt)** – Secure password hashing

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <https://github.com/SaradhaVelusamy04/Quiz_app>
cd Quiz_app
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy pydantic passlib
```

### 4. Initialize the database

In your main application (`main.py` or `crud.py`):

```python
from models import Base
from database import engine

Base.metadata.create_all(bind=engine)
```

> This will create the tables: `User`, `Question`, and `Result`.

### 5. Run the application

```bash
uvicorn main:app --reload
```

* Open **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Open **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

### 1. **Register a User**

* **POST** `/register`
* **Request Body**:

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

### 2. **Login**

* **POST** `/login`
* **Request Body**:

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

### 3. **Create a Question**

* **POST** `/questions`
* **Request Body**:

```json
{
  "question": "What is 2 + 2?",
  "option1": "3",
  "option2": "4",
  "option3": "5",
  "answer": "4"
}
```

### 4. **Get All Questions**

* **GET** `/questions`

### 5. **Save Quiz Result**

* **POST** `/results`
* **Request Body**:

```json
{
  "user_id": 1,
  "score": 8
}
```

### 6. **Get User Results**

* **GET** `/results/{user_id}`

---

## Notes

* **Password hashing**: Only the hashed password is stored in the database.
* **CORS**: If testing from a browser frontend, make sure to enable CORS in FastAPI:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Folder Structure

```
Quiz_app/
├─ main.py          # FastAPI endpoints
├─ crud.py          # Database CRUD operations
├─ models.py        # SQLAlchemy models
├─ schemas.py       # Pydantic schemas
├─ database.py      # Database engine & session
└─ README.md        # Project documentation
---
