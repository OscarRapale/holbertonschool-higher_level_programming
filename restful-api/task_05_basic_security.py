from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    """
    Verify the provided username and password against the stored users.
    """
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
    

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    A route protected by basic authentication.
    """
    return "Basic Auth: Access Granted"

app.config["JWT_SECRET_KEY"] = "super_secret_key"
jwt = JWTManager(app)

@app.route("/login", methods=["POST"])
def login():
    """
    A route where users can log in and receive a JWT token.
    """
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username in users and check_password_hash(users.get(username), password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    A route protected by JWT authentication.
    """
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    A route that is only accessible to users with the 'admin' role.
    """
    current_user = get_jwt_identity()
    if users.get(current_user)['role'] != 'admin':
        return jsonify({"msg": "Access forbidden"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
