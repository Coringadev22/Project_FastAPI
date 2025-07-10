# Project FastAPI

A sample backend written with **FastAPI** + **SQLAlchemy** that manages:

* Users & authentication
* Orders and order items
* Delivery men & motorcycles
* Customers & stores

SQLite is used for persistence and **Alembic** handles migrations.

---

## 📂 Project structure (high-level)

```
Project_FastAPI/
├── main.py              # Application entry-point (FastAPI instance)
├── models.py            # SQLAlchemy ORM models
├── auth_routes.py       # Auth demo endpoint
├── order_routes.py      # CRUD routes for orders
├── delivery_man.py      # CRUD routes for delivery men
├── alembic/             # Alembic migrations folder
├── database.db          # SQLite database file (generated at runtime)
└── README.md            # ← you are here
```

---

## ⚙️  Requirements

| Package        | Role                          |
| -------------- | ----------------------------- |
| fastapi        | Web framework                 |
| uvicorn        | ASGI server                   |
| sqlalchemy     | ORM & database toolkit        |
| alembic        | Schema migrations             |
| pydantic       | Request/response validation   |
| passlib[bcrypt]| Password hashing (auth)       |
| python-dotenv  | Optional env-file support     |

> Python 3.10+ recommended.

---

## 🚀 Quick start

```bash
# 1. Clone repository & cd into it
$ git clone <repo-url>
$ cd Project_FastAPI

# 2. Create & activate virtual environment (Windows PowerShell example)
$ python -m venv venv
$ .\venv\Scripts\Activate.ps1

# 3. Install dependencies
(venv) $ pip install fastapi uvicorn sqlalchemy alembic pydantic "passlib[bcrypt]" python-dotenv

# 4. Run migrations (SQLite DB will be created if absent)
(venv) $ alembic upgrade head

# 5. Start API server (auto-reload)
(venv) $ uvicorn main:app --reload
# or
(venv) $ python main.py             # thanks to __main__ block
```

Server is available at `http://127.0.0.1:8000`.

Interactive docs:
* Swagger UI → `http://127.0.0.1:8000/docs`
* ReDoc → `http://127.0.0.1:8000/redoc`

---

## 🌐 API overview

| Method | Path                          | Description                     |
| ------ | ----------------------------- | ------------------------------- |
| GET    | `/`                           | Health check – "Hello, World!" |
| GET    | `/auth/`                      | Auth demo endpoint              |
| GET    | `/orders/`                    | List orders                     |
| POST   | `/orders/`                    | Create order (body `OrderCreate`)|
| PUT    | `/orders/{id}`                | Update order                    |
| DELETE | `/orders/{id}`                | Delete order                    |
| GET    | `/deliveryman/`               | List delivery men               |
| GET    | `/deliveryman/{id}`           | Retrieve delivery man           |
| POST   | `/deliveryman/`               | Create delivery man             |
| PUT    | `/deliveryman/{id}`           | Update delivery man             |
| DELETE | `/deliveryman/{id}`           | Delete delivery man             |

> Endpoints return JSON and use Pydantic schemas for validation wherever applicable.

---

## 🗄️  Database & migrations

The default database URL is hard-coded to SQLite file `database.db` in the project root (see `models.py`).

* **Create new migration**: `alembic revision --autogenerate -m "message"`
* **Apply migrations**: `alembic upgrade head`
* **Downgrade**: `alembic downgrade -1`

> Configure `alembic.ini` / `alembic/env.py` if you change the DB URL.

---

## 🛠️  Development notes

* Use `black` / `isort` / `flake8` for code quality (optional).
* Environment variables (e.g., `DATABASE_URL`) can be loaded via `.env` when `python-dotenv` is installed.
* To add more resources, create new Pydantic schemas and route modules, then include them in `main.py` with `app.include_router(...)`.

---

## 📄 License

MIT – use freely, no warranty. 