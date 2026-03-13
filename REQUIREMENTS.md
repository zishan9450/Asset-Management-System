# Asset Management System — Requirements

> Full-stack enterprise application enabling administrators to manage company assets while employees track assigned assets and report issues.

---

## Tech Stack

| Layer    | Technology        |
|----------|-------------------|
| Frontend | Next.js (React)   |
| Backend  | Flask (Python)    |
| Database | PostgreSQL / SQLite (dev) |
| Auth     | JWT               |

---

## 1. User Authentication and Role Management

### Roles
| Role        | Description                          |
|-------------|--------------------------------------|
| Admin       | Full system access                   |
| IT Manager  | Manage assets, issues, maintenance   |
| Employee    | View own assets, report issues       |

### Permissions Matrix

| Feature        | Admin | IT Manager | Employee |
|----------------|-------|------------|----------|
| Add asset      | ✅    | ✅         | ❌       |
| Assign asset   | ✅    | ✅         | ❌       |
| View own assets| ✅    | ✅         | ✅       |
| Report issue   | ✅    | ✅         | ✅       |

### Requirements
- Users can register and log in.
- Role-based access control (RBAC) restricts features by role.
- Admins can view all users in the system.
- Admins can update user roles.

---

## 2. Asset Inventory Management

### Requirements
- Add new assets to the inventory.
- Update asset information.
- Delete assets.
- View all assets in a table.
- Search assets by name or serial number.
- Filter assets by status.

### Asset Fields

| Field           | Type     |
|-----------------|----------|
| id              | UUID/Int |
| asset_name      | String   |
| category        | String   |
| brand           | String   |
| model           | String   |
| serial_number   | String   |
| purchase_date   | Date     |
| warranty_expiry | Date     |
| status          | Enum     |

### Asset Statuses
- `Available`
- `Assigned`
- `Under Maintenance`
- `Retired`

---

## 3. Asset Assignment Module

### Requirements
1. Assign an asset to an employee.
2. Record assignment date automatically.
3. Track asset return date.
4. View assets assigned to each employee.
5. Prevent assigning already-assigned assets.
6. Employees can view assets assigned to them.

### Asset Assignment Fields

| Field         | Type     |
|---------------|----------|
| id            | UUID/Int |
| asset_id      | FK       |
| employee_id   | FK       |
| assigned_date | Date     |
| return_date   | Date     |

---

## 4. Issue Reporting and Maintenance Module

### Requirements
- Employees can submit an issue for an assigned asset.
- Each issue must contain: issue description, asset information, date reported.
- IT Managers can update issue status.

### Issue Fields

| Field             | Type     |
|-------------------|----------|
| id                | UUID/Int |
| asset_id          | FK       |
| employee_id       | FK       |
| issue_description | Text     |
| status            | Enum     |
| created_at        | DateTime |

### Issue Statuses
- `Open`
- `In Progress`
- `Resolved`
- `Closed`

---

## 5. Maintenance History

### Requirements
- Record maintenance activities.
- Link maintenance to a specific asset.
- Track repair costs.
- View maintenance history for each asset.

### Maintenance Record Fields

| Field            | Type     |
|------------------|----------|
| id               | UUID/Int |
| asset_id         | FK       |
| maintenance_date | Date     |
| technician       | String   |
| description      | Text     |
| cost             | Decimal  |

---

## 6. Dashboard and Analytics

The dashboard displays:
- Total assets
- Assigned assets
- Available assets
- Assets under maintenance
- Open issues

---

## 7. Activity Logging

The system records all user actions for auditing.

### Logged Actions (examples)
- Asset creation
- Asset assignment
- Issue reporting
- Issue resolution

### Activity Log Fields

| Field     | Type     |
|-----------|----------|
| id        | UUID/Int |
| user_id   | FK       |
| action    | String   |
| timestamp | DateTime |

---

## Database Schema Summary

### Users
| Field      | Type   |
|------------|--------|
| id         | PK     |
| name       | String |
| email      | String |
| password   | Hash   |
| role       | Enum   |
| department | String |

### Assets
| Field           | Type   |
|-----------------|--------|
| id              | PK     |
| asset_name      | String |
| category        | String |
| brand           | String |
| model           | String |
| serial_number   | String |
| purchase_date   | Date   |
| warranty_expiry | Date   |
| status          | Enum   |

### Asset Assignments
| Field         | Type |
|---------------|------|
| id            | PK   |
| asset_id      | FK   |
| employee_id   | FK   |
| assigned_date | Date |
| return_date   | Date |

### Issues
| Field             | Type     |
|-------------------|----------|
| id                | PK       |
| asset_id          | FK       |
| employee_id       | FK       |
| issue_description | Text     |
| status            | Enum     |
| created_at        | DateTime |

### Maintenance Records
| Field            | Type    |
|------------------|---------|
| id               | PK      |
| asset_id         | FK      |
| maintenance_date | Date    |
| technician       | String  |
| description      | Text    |
| cost             | Decimal |

### Activity Logs
| Field     | Type     |
|-----------|----------|
| id        | PK       |
| user_id   | FK       |
| action    | String   |
| timestamp | DateTime |

---

## Frontend Pages

| # | Page                  | Route                  | Access         |
|---|-----------------------|------------------------|----------------|
| 1 | Login                 | `/login`               | Public         |
| 2 | Dashboard             | `/dashboard`           | All roles      |
| 3 | Asset Inventory       | `/assets`              | Admin, IT Mgr  |
| 4 | Asset Assignment      | `/assignments`         | Admin, IT Mgr  |
| 5 | Employee Asset View   | `/my-assets`           | All roles      |
| 6 | Issue Reporting       | `/issues/report`       | All roles      |
| 7 | Issue Management      | `/issues`              | Admin, IT Mgr  |
| 8 | User Management       | `/users`               | Admin only     |

---

## Project Structure

```
Asset-Management-System/
├── REQUIREMENTS.md
├── frontend/          # Next.js application
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   └── lib/
│   └── package.json
└── backend/           # Flask application
    ├── app/
    │   ├── models/
    │   ├── routes/
    │   └── __init__.py
    ├── requirements.txt
    └── run.py
```
