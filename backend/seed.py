from datetime import date, timedelta

from app import bcrypt, create_app, db
from app.models import Asset, AssetAssignment, Issue, MaintenanceRecord, User

app = create_app("development")


def ensure_user(name, email, password, role, department):
    user = User.query.filter_by(email=email).first()
    if user:
        return user

    user = User(
        name=name,
        email=email,
        password=bcrypt.generate_password_hash(password).decode("utf-8"),
        role=role,
        department=department,
    )
    db.session.add(user)
    db.session.flush()
    return user


def ensure_asset(**kwargs):
    asset = Asset.query.filter_by(serial_number=kwargs["serial_number"]).first()
    if asset:
        return asset
    asset = Asset(**kwargs)
    db.session.add(asset)
    db.session.flush()
    return asset


with app.app_context():
    admin = ensure_user("Admin User", "admin@omsc.edu.ph", "admin123", "admin", "Administration")
    manager = ensure_user("IT Manager", "it.manager@omsc.edu.ph", "manager123", "it_manager", "ICT")
    employee = ensure_user("John Doe", "john.doe@omsc.edu.ph", "employee123", "employee", "Registrar")
    accountant = ensure_user("Jane Smith", "jane.smith@omsc.edu.ph", "employee123", "employee", "Accounting")

    laptop = ensure_asset(
        asset_name="Dell Latitude 7420",
        category="Laptop",
        brand="Dell",
        model="7420",
        serial_number="DL-0001",
        purchase_date=date(2024, 1, 15),
        warranty_expiry=date(2027, 1, 15),
        status="assigned",
    )
    printer = ensure_asset(
        asset_name="HP LaserJet Pro",
        category="Printer",
        brand="HP",
        model="M404dn",
        serial_number="HP-0102",
        purchase_date=date(2023, 6, 1),
        warranty_expiry=date(2026, 6, 1),
        status="assigned",
    )
    router = ensure_asset(
        asset_name="Cisco Router 2911",
        category="Network",
        brand="Cisco",
        model="2911",
        serial_number="CS-9211",
        purchase_date=date(2022, 9, 12),
        warranty_expiry=date(2025, 9, 12),
        status="under_maintenance",
    )
    monitor = ensure_asset(
        asset_name="Samsung Monitor 24 inch",
        category="Monitor",
        brand="Samsung",
        model="S24R350",
        serial_number="SM-4450",
        purchase_date=date(2024, 2, 10),
        warranty_expiry=date(2027, 2, 10),
        status="assigned",
    )
    projector = ensure_asset(
        asset_name="Epson Projector X19",
        category="Projector",
        brand="Epson",
        model="X19",
        serial_number="EP-9910",
        purchase_date=date(2021, 8, 20),
        warranty_expiry=date(2024, 8, 20),
        status="retired",
    )

    if not AssetAssignment.query.filter_by(asset_id=laptop.id, employee_id=employee.id, return_date=None).first():
        db.session.add(AssetAssignment(asset_id=laptop.id, employee_id=employee.id, assigned_date=date.today() - timedelta(days=30)))
    if not AssetAssignment.query.filter_by(asset_id=printer.id, employee_id=accountant.id, return_date=None).first():
        db.session.add(AssetAssignment(asset_id=printer.id, employee_id=accountant.id, assigned_date=date.today() - timedelta(days=60)))
    if not AssetAssignment.query.filter_by(asset_id=monitor.id, employee_id=employee.id, return_date=None).first():
        db.session.add(AssetAssignment(asset_id=monitor.id, employee_id=employee.id, assigned_date=date.today() - timedelta(days=30)))

    if not Issue.query.filter_by(asset_id=laptop.id, employee_id=employee.id, issue_description="Battery drains quickly.").first():
        db.session.add(Issue(asset_id=laptop.id, employee_id=employee.id, issue_description="Battery drains quickly.", status="open"))
    if not Issue.query.filter_by(asset_id=printer.id, employee_id=accountant.id, issue_description="Paper jam in tray 2.").first():
        db.session.add(Issue(asset_id=printer.id, employee_id=accountant.id, issue_description="Paper jam in tray 2.", status="in_progress"))

    if not MaintenanceRecord.query.filter_by(asset_id=router.id, technician="Network Team").first():
        db.session.add(MaintenanceRecord(asset_id=router.id, maintenance_date=date.today() - timedelta(days=7), technician="Network Team", description="Replaced failing WAN interface module.", cost=4500.00))

    db.session.commit()
    print("Seed complete.")
    print("Admin: admin@omsc.edu.ph / admin123")
    print("IT Manager: it.manager@omsc.edu.ph / manager123")
    print("Employee: john.doe@omsc.edu.ph / employee123")
