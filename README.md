# 📚 Library Management API

A modern, RESTful API for managing library operations including books, members, and borrowing records. Built with FastAPI and SQLAlchemy for high performance and reliability.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🚀 Features

- ✅ **Book Management** - Create, read, update, and delete books with quantity tracking
- ✅ **Member Management** - Register and manage library members with email validation
- ✅ **Borrow System** - Track book borrowing and returns with automatic quantity updates
- ✅ **Borrow History** - View complete borrow history by member or book
- ✅ **Data Validation** - Input validation using Pydantic with email verification
- ✅ **RESTful API** - Clean, intuitive endpoints following REST conventions
- ✅ **Database Persistence** - SQLite with SQLAlchemy ORM for reliable data storage
- ✅ **API Documentation** - Interactive Swagger UI and ReDoc documentation

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | [FastAPI](https://fastapi.tiangolo.com/) |
| **ORM** | [SQLAlchemy](https://www.sqlalchemy.org/) |
| **Database** | SQLite |
| **Validation** | Pydantic |
| **Server** | Uvicorn |
| **Language** | Python 3.9+ |

## 📋 Project Structure

```
app/
├── main.py              # Application entry point
├── database.py          # Database configuration & session management
├── models.py            # SQLAlchemy ORM models
├── schemas.py           # Pydantic request/response schemas
├── routes/
│   ├── __init__.py
│   ├── books.py         # Books endpoints
│   ├── members.py       # Members endpoints
│   └── borrows.py       # Borrow/Return endpoints
└── __init__.py
```

## ⚙️ Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/mattmhk/Library-Management-API.git
cd Library-Management-API
```

2. **Create a virtual environment**
```bash
python -m venv .venv
```

3. **Activate the virtual environment**

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Run the server**
```bash
cd app
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## 📚 API Endpoints

### Books
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books` | Get all books |
| POST | `/books` | Add a new book |
| GET | `/books/{book_id}` | Get book details |
| PUT | `/books/{book_id}` | Update book quantity |
| DELETE | `/books/{book_id}` | Delete a book |

### Members
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/members` | Get all members |
| POST | `/members` | Register a new member |
| GET | `/members/{member_id}` | Get member details |
| PUT | `/members/{member_id}` | Update member email |
| DELETE | `/members/{member_id}` | Delete a member |

### Borrows
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/borrow` | Borrow a book |
| PUT | `/borrow/return/{borrow_id}` | Return a book |
| GET | `/borrow` | Get all borrow records |
| GET | `/borrow/{borrow_id}` | Get borrow details |
| GET | `/borrow/member/{member_id}` | Get member's borrow history |
| GET | `/borrow/book/{book_id}` | Get book's borrow history |

## 🧪 API Documentation

Once the server is running, visit:

- **Swagger UI** - http://localhost:8000/docs
- **ReDoc** - http://localhost:8000/redoc
- **OpenAPI Schema** - http://localhost:8000/openapi.json

## 📝 Example Requests

### Add a Book
```bash
curl -X POST "http://localhost:8000/books" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "quantity": 5
  }'
```

### Register a Member
```bash
curl -X POST "http://localhost:8000/members" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com"
  }'
```

### Borrow a Book
```bash
curl -X POST "http://localhost:8000/borrow" \
  -H "Content-Type: application/json" \
  -d '{
    "book_id": 1,
    "member_id": 1
  }'
```

