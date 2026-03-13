from app.routes.auth import auth_bp
from app.routes.users import users_bp
from app.routes.assets import assets_bp
from app.routes.assignments import assignments_bp
from app.routes.issues import issues_bp
from app.routes.maintenance import maintenance_bp
from app.routes.dashboard import dashboard_bp
from app.routes.activity_logs import logs_bp

__all__ = [
    "auth_bp",
    "users_bp",
    "assets_bp",
    "assignments_bp",
    "issues_bp",
    "maintenance_bp",
    "dashboard_bp",
    "logs_bp",
]
