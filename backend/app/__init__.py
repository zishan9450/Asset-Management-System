from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import verify_jwt_in_request
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask import g, request
from datetime import datetime, timezone
from uuid import uuid4

from config import config, validate_runtime_config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    validate_runtime_config(app.config, config_name)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)
    CORS(
        app,
        resources={
            r"/api/*": {
                "origins": app.config["CORS_ORIGINS"],
                "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
            }
        },
    )

    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.users import users_bp
    from app.routes.assets import assets_bp
    from app.routes.assignments import assignments_bp
    from app.routes.issues import issues_bp
    from app.routes.maintenance import maintenance_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.activity_logs import logs_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(users_bp, url_prefix="/api/users")
    app.register_blueprint(assets_bp, url_prefix="/api/assets")
    app.register_blueprint(assignments_bp, url_prefix="/api/assignments")
    app.register_blueprint(issues_bp, url_prefix="/api/issues")
    app.register_blueprint(maintenance_bp, url_prefix="/api/maintenance")
    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")
    app.register_blueprint(logs_bp, url_prefix="/api/logs")

    @app.before_request
    def before_request_logging():
        g.request_id = str(uuid4())
        g.request_started_at = datetime.now(timezone.utc)

    @app.after_request
    def after_request_logging(response):
        # Add baseline API hardening headers.
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "no-referrer")

        if request.path.startswith("/api/"):
            user_id = None
            try:
                verify_jwt_in_request(optional=True)
                user_id = get_jwt_identity()
            except Exception:
                user_id = None

            started_at = getattr(g, "request_started_at", datetime.now(timezone.utc))
            duration_ms = int((datetime.now(timezone.utc) - started_at).total_seconds() * 1000)

            app.logger.info(
                "request",
                extra={
                    "request_id": getattr(g, "request_id", "unknown"),
                    "method": request.method,
                    "path": request.path,
                    "status": response.status_code,
                    "duration_ms": duration_ms,
                    "user_id": user_id,
                    "ip": request.headers.get("X-Forwarded-For", request.remote_addr),
                },
            )

        return response

    return app
