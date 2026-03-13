from app import db
from datetime import datetime, timezone


class MaintenanceRecord(db.Model):
    __tablename__ = "maintenance_records"

    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey("assets.id"), nullable=False)
    maintenance_date = db.Column(db.Date, nullable=False)
    technician = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    cost = db.Column(db.Numeric(10, 2), default=0.00)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            "id": self.id,
            "asset_id": self.asset_id,
            "asset": self.asset.to_dict() if self.asset else None,
            "maintenance_date": self.maintenance_date.isoformat() if self.maintenance_date else None,
            "technician": self.technician,
            "description": self.description,
            "cost": float(self.cost) if self.cost is not None else 0.0,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
