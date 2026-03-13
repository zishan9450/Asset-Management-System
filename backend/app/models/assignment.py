from app import db
from datetime import datetime, timezone


class AssetAssignment(db.Model):
    __tablename__ = "asset_assignments"

    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey("assets.id"), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    assigned_date = db.Column(db.Date, nullable=False, default=lambda: datetime.now(timezone.utc).date())
    return_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            "id": self.id,
            "asset_id": self.asset_id,
            "asset": self.asset.to_dict() if self.asset else None,
            "employee_id": self.employee_id,
            "employee": self.employee.to_dict() if self.employee else None,
            "assigned_date": self.assigned_date.isoformat() if self.assigned_date else None,
            "return_date": self.return_date.isoformat() if self.return_date else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
