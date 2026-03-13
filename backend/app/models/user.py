from app import db
from datetime import datetime, timezone


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(
        db.Enum("admin", "it_manager", "employee", name="user_roles"),
        nullable=False,
        default="employee",
    )
    department = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    assignments = db.relationship("AssetAssignment", backref="employee", lazy=True)
    issues = db.relationship("Issue", backref="reporter", lazy=True)
    activity_logs = db.relationship("ActivityLog", backref="user", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "department": self.department,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
