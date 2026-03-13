import os

from app import create_app, db
from app.models import User, Asset, AssetAssignment, Issue, MaintenanceRecord, ActivityLog  # noqa: F401 – ensure models are imported so Flask-Migrate discovers them

app = create_app("development")


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "Asset": Asset,
        "AssetAssignment": AssetAssignment,
        "Issue": Issue,
        "MaintenanceRecord": MaintenanceRecord,
        "ActivityLog": ActivityLog,
    }


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("FLASK_RUN_PORT", "5050")))
