from app import db
from datetime import datetime, timezone


class Issue(db.Model):
    __tablename__ = "issues"

    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey("assets.id"), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    status = db.Column(
        db.Enum("open", "in_progress", "resolved", "closed", name="issue_status"),
        nullable=False,
        default="open",
    )
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "asset_id": self.asset_id,
            "asset": self.asset.to_dict() if self.asset else None,
            "employee_id": self.employee_id,
            "reporter": self.reporter.to_dict() if self.reporter else None,
            "issue_description": self.issue_description,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
