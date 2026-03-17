# 🏢 AssetHub — Enterprise Asset Management System

A full-stack **Enterprise Asset Management** web application with a premium dark SaaS dashboard UI. Built with **React + Vite** (frontend) and **Flask + MySQL** (backend), featuring role-based access control, real-time search, glassmorphism design, and comprehensive asset lifecycle management.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Role-Based Dashboard** | Admin/IT Manager see system-wide analytics; Employees see only their own assets & issues |
| **Asset Management** | Full CRUD with categories, status tracking, serial numbers, warranty dates |
| **Assignment Tracking** | Assign/return assets to employees with history |
| **Issue Reporting** | Employees report issues, managers update status (open → in progress → resolved → closed) |
| **Maintenance Records** | Schedule and track asset maintenance with cost tracking |
| **User Management** | Admin can manage users, assign roles, activate/deactivate accounts |
| **Live Global Search** | Real-time search across assets, users, and issues with categorized results |
| **Role-Based Notifications** | Dynamic notifications based on user role from real system data |
| **User Registration** | Self-registration with admin role assignment |
| **Activity Logs** | Full audit trail of all system actions |
| **Premium Dark UI** | Glassmorphism cards, gradient accents, micro-animations |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React 18, Vite, React Router v6, Axios, Recharts, Lucide Icons |
| **Backend** | Python Flask, Flask-SQLAlchemy, Flask-JWT-Extended, Flask-Bcrypt, Flask-CORS |
| **Database** | MySQL (local) / Railway MySQL (production) |
| **Deployment** | Vercel (frontend), Render (backend), Railway (database) |

---

## 📁 Project Structure

```
Asset Management System/
├── backend/
│   ├── app.py                 # Flask app entry point
│   ├── config.py              # Database & JWT configuration
│   ├── models.py              # SQLAlchemy models
│   ├── requirements.txt       # Python dependencies
│   ├── routes/
│   │   ├── auth.py            # Login & registration
│   │   ├── users.py           # User CRUD
│   │   ├── assets.py          # Asset CRUD
│   │   ├── assignments.py     # Asset assignments
│   │   ├── issues.py          # Issue tracking
│   │   ├── maintenance.py     # Maintenance records
│   │   ├── dashboard.py       # Role-based dashboard stats
│   │   ├── search.py          # Global search
│   │   ├── notifications.py   # Role-based notifications
│   │   └── activity_logs.py   # Audit logs
│   └── seed.py                # Database seeder
│
├── frontend/
│   ├── src/
│   │   ├── api/client.js      # Axios instance
│   │   ├── context/AuthContext.jsx
│   │   ├── components/
│   │   │   ├── Layout.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   └── TopNav.jsx
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Assets.jsx
│   │   │   ├── Assignments.jsx
│   │   │   ├── Issues.jsx
│   │   │   ├── Maintenance.jsx
│   │   │   ├── Users.jsx
│   │   │   ├── Settings.jsx
│   │   │   ├── ActivityLogs.jsx
│   │   │   ├── MyAssets.jsx
│   │   │   ├── Login.jsx
│   │   │   └── Register.jsx
│   │   ├── App.jsx
│   │   └── index.css
│   ├── vercel.json
│   └── package.json
│
├── .gitignore
└── README.md
```

---

## 🚀 Local Development Setup

### Prerequisites

- **Node.js** 18+ and **npm**
- **Python** 3.9+
- **MySQL** 8.0+

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/asset-management-system.git
cd asset-management-system
```

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

Create the MySQL database:

```sql
CREATE DATABASE asset_management;
```

Update `config.py` with your MySQL credentials if needed:

```python
'mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/asset_management'
```

Start the backend:

```bash
python app.py
```

The API will run at `http://localhost:5000`.

### 3. Seed the Database (Optional)

```bash
python seed.py
```

### 4. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The app will run at `http://localhost:5173`.

---

## 👥 Demo Credentials

| Role | Email | Password |
|---|---|---|
| Admin | admin@company.com | admin123 |
| IT Manager | rahul@company.com | password123 |
| Employee | priya@company.com | password123 |

---

## 🌐 Deployment Guide

### Database → Railway MySQL

1. Go to [railway.app](https://railway.app) and create a new project
2. Click **"New"** → **"Database"** → **"MySQL"**
3. Once provisioned, go to **Settings** → **Variables** and copy:
   - `MYSQL_URL` (format: `mysql://user:pass@host:port/dbname`)
4. Convert to PyMySQL format for Flask:
   - Change `mysql://` to `mysql+pymysql://`
   - This becomes your `DATABASE_URL`

### Backend → Render

1. Go to [render.com](https://render.com) and create a **New Web Service**
2. Connect your GitHub repo
3. Configure:
   - **Root Directory**: `backend`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
4. Add **Environment Variables**:
   - `DATABASE_URL` = your Railway MySQL URL (with `mysql+pymysql://`)
   - `SECRET_KEY` = a random secret string
   - `JWT_SECRET_KEY` = another random secret string
   - `FLASK_ENV` = production
5. Deploy. Note the Render URL (e.g., `https://your-app.onrender.com`)

### Frontend → Vercel

1. Go to [vercel.com](https://vercel.com) and import your GitHub repo
2. Configure:
   - **Root Directory**: `frontend`
   - **Framework Preset**: Vite
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
3. Add **Environment Variable**:
   - `VITE_API_URL` = your Render backend URL (e.g., `https://your-app.onrender.com`)
4. Deploy

---

## 🔒 Role-Based Access

| Feature | Admin | IT Manager | Employee |
|---|---|---|---|
| Dashboard (Full Stats) | ✅ | ✅ | ❌ |
| Dashboard (Personal) | ❌ | ❌ | ✅ |
| Manage Assets | ✅ | ✅ | ❌ |
| View My Assets | ❌ | ❌ | ✅ |
| Manage Assignments | ✅ | ✅ | ❌ |
| Report Issues | ✅ | ✅ | ✅ |
| Update Issue Status | ✅ | ✅ | ❌ |
| Maintenance Records | ✅ | ✅ | ❌ |
| Manage Users | ✅ | ❌ | ❌ |
| Activity Logs | ✅ | ✅ | ❌ |
| Settings | ✅ | ✅ | ✅ |

---

## 📡 API Endpoints

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | `/auth/login` | User login | ❌ |
| POST | `/auth/register` | User registration | ❌ |
| GET | `/dashboard-stats` | Role-based dashboard data | ✅ |
| GET | `/search?q=` | Global search | ✅ |
| GET | `/notifications` | Role-based notifications | ✅ |
| GET/POST | `/assets` | List/Create assets | ✅ |
| PUT/DELETE | `/assets/:id` | Update/Delete asset | ✅ |
| GET/POST | `/assignments` | List/Create assignments | ✅ |
| GET/POST | `/issues` | List/Create issues | ✅ |
| PUT | `/issues/:id` | Update issue status | ✅ |
| GET/POST | `/maintenance` | List/Create maintenance | ✅ |
| GET/POST/PUT/DELETE | `/users` | User management | ✅ |
| GET | `/activity-logs` | Audit logs | ✅ |

---

## 📄 License

This project is built for educational and portfolio purposes.
