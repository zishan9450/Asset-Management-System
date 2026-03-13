from app import db
from datetime import datetime, timezone


class Asset(db.Model):
    __tablename__ = "assets"

    id = db.Column(db.Integer, primary_key=True)
    asset_name = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    serial_number = db.Column(db.String(100), unique=True, nullable=False)
    purchase_date = db.Column(db.Date)
    warranty_expiry = db.Column(db.Date)
    status = db.Column(
        db.Enum(
            "available",
            "assigned",
            "under_maintenance",
            "retired",
            name="asset_status",
        ),
        nullable=False,
        default="available",
    )
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    assignments = db.relationship("AssetAssignment", backref="asset", lazy=True)
    issues = db.relationship("Issue", backref="asset", lazy=True)
    maintenance_records = db.relationship(
        "MaintenanceRecord", backref="asset", lazy=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "asset_name": self.asset_name,
            "category": self.category,
            "brand": self.brand,
            "model": self.model,
            "serial_number": self.serial_number,
            "purchase_date": self.purchase_date.isoformat() if self.purchase_date else None,
            "warranty_expiry": self.warranty_expiry.isoformat() if self.warranty_expiry else None,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
