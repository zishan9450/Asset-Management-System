# Asset Management System

Full-stack enterprise application for managing company assets.

| Layer    | Technology        |
|----------|-------------------|
| Frontend | Next.js + TypeScript + Tailwind CSS |
| Backend  | Flask + SQLAlchemy + JWT |
| Database | SQLite (dev) / PostgreSQL (prod) |

---

## Project Structure

```
Asset-Management-System/
├── REQUIREMENTS.md        # Full feature specification
├── README.md
├── frontend/              # Next.js application (port 3000)
│   └── src/app/
└── backend/               # Flask REST API (port 5000)
    ├── app/
    │   ├── models/        # SQLAlchemy models
    │   ├── routes/        # Blueprint route handlers
    │   └── utils/         # Helpers & decorators
    ├── migrations/        # Alembic DB migrations
    ├── config.py
    ├── requirements.txt
    └── run.py
```

---

## Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env              # edit SECRET_KEY / JWT_SECRET_KEY

flask --app run.py db upgrade     # apply migrations
python run.py                     # start dev server on :5000
```

### API Base URL
`http://localhost:5000/api`

| Prefix            | Description          |
|-------------------|----------------------|
| `/auth`           | Register / Login     |
| `/users`          | User management      |
| `/assets`         | Asset inventory      |
| `/assignments`    | Asset assignments    |
| `/issues`         | Issue reporting      |
| `/maintenance`    | Maintenance records  |
| `/dashboard`      | Analytics stats      |
| `/logs`           | Activity audit logs  |

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev                        # start dev server on :3000
```

---

## Roles

| Role        | Add Asset | Assign Asset | View Own Assets | Report Issue |
|-------------|-----------|--------------|-----------------|--------------|
| Admin       | ✅        | ✅           | ✅              | ✅           |
| IT Manager  | ✅        | ✅           | ✅              | ✅           |
| Employee    | ❌        | ❌           | ✅              | ✅           |
