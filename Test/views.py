from flask import Blueprint, request, jsonify
from controllers import verify_user

user_views = Blueprint("user_views", __name__)

@user_views.route("/login", methods=["POST"])
def login():
    data = request.json
    if not data or "username" not in data or "password" not in data:
        return jsonify({"message":"Missing fields"}), 400
    
    result = verify_user(data["username"], data["password"])
    return jsonify(result)
