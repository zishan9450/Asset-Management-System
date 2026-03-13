from functools import wraps
from typing import Optional
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from app.models.user import User
from app import db
from app.models.activity_log import ActivityLog
from datetime import datetime, timezone


def get_current_user_id() -> Optional[int]:
    identity = get_jwt_identity()
    try:
        return int(identity) if identity is not None else None
    except (TypeError, ValueError):
        return None


def role_required(*roles):
    """Decorator to restrict route access by user role."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            current_user_id = get_current_user_id()
            user = db.session.get(User, current_user_id)
            if not user or user.role not in roles:
                return jsonify({"error": "Access forbidden: insufficient permissions"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator


def log_action(user_id: int, action: str):
    """Record an activity log entry."""
    log = ActivityLog(user_id=user_id, action=action, timestamp=datetime.now(timezone.utc))
    db.session.add(log)
    db.session.commit()
