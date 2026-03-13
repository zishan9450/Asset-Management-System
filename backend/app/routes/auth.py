from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app import db, bcrypt
from app.models.user import User
from app.utils.helpers import log_action
from app.utils.http import error_response

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    required = ["name", "email", "password"]
    if not all(k in data for k in required):
        return error_response("Missing required fields", 400, "VALIDATION_ERROR")

    if User.query.filter_by(email=data["email"]).first():
        return error_response("Email already registered", 409, "CONFLICT")

    hashed = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    user = User(
        name=data["name"],
        email=data["email"],
        password=hashed,
        role=data.get("role", "employee"),
        department=data.get("department"),
    )
    db.session.add(user)
    db.session.commit()
    log_action(user.id, f"User registered: {user.email}")
    return jsonify({"message": "User registered successfully", "user": user.to_dict()}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("password"):
        return error_response("Email and password required", 400, "VALIDATION_ERROR")

    user = User.query.filter_by(email=data["email"]).first()
    if not user or not bcrypt.check_password_hash(user.password, data["password"]):
        return error_response("Invalid credentials", 401, "UNAUTHORIZED")

    token = create_access_token(identity=str(user.id))
    log_action(user.id, f"User logged in: {user.email}")
    return jsonify({"access_token": token, "user": user.to_dict()}), 200
