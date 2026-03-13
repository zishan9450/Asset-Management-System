import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


DEV_SECRET_FALLBACK = "dev-secret-key"
DEV_JWT_SECRET_FALLBACK = "jwt-dev-secret"
MIN_SECRET_LENGTH = 32


def _parse_cors_origins():
    origins = os.environ.get(
        "CORS_ORIGINS",
        "http://localhost:3000,http://127.0.0.1:3000",
    )
    return [origin.strip() for origin in origins.split(",") if origin.strip()]


def _parse_jwt_expiry_seconds():
    raw = os.environ.get("JWT_ACCESS_TOKEN_EXPIRES_SECONDS", "86400")
    try:
        value = int(raw)
    except ValueError:
        return 86400

    return max(300, value)


def _is_weak_secret(secret_value: Optional[str], fallback: str):
    if not secret_value:
        return True

    if secret_value == fallback:
        return True

    if secret_value in {"your-secret-key-here", "your-jwt-secret-key-here"}:
        return True

    return len(secret_value) < MIN_SECRET_LENGTH


def validate_runtime_config(app_config, config_name: str):
    if config_name != "production":
        return

    secret_key = app_config.get("SECRET_KEY")
    jwt_secret_key = app_config.get("JWT_SECRET_KEY")
    cors_origins = app_config.get("CORS_ORIGINS", [])

    if _is_weak_secret(secret_key, DEV_SECRET_FALLBACK):
        raise RuntimeError("Production SECRET_KEY must be set to a strong value (min 32 chars)")

    if _is_weak_secret(jwt_secret_key, DEV_JWT_SECRET_FALLBACK):
        raise RuntimeError("Production JWT_SECRET_KEY must be set to a strong value (min 32 chars)")

    if not cors_origins:
        raise RuntimeError("Production CORS_ORIGINS cannot be empty")

    if any(origin == "*" for origin in cors_origins):
        raise RuntimeError("Production CORS_ORIGINS cannot include wildcard '*'")

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", DEV_SECRET_FALLBACK)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///asset_management.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", DEV_JWT_SECRET_FALLBACK)
    JWT_ACCESS_TOKEN_EXPIRES = _parse_jwt_expiry_seconds()
    JWT_TOKEN_LOCATION = ["headers"]
    CORS_ORIGINS = _parse_cors_origins()


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
