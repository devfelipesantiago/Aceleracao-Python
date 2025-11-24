from bson import ObjectId
from flask import Blueprint, jsonify, request
from models.history_model import HistoryModel
from models.user_model import UserModel

admin_controller = Blueprint("admin_controller", __name__)


def _check_admin_auth():
    auth_token = request.headers.get("Authorization")
    user_name = request.headers.get("User")

    if not auth_token or not user_name:
        return jsonify({"error": "Unauthorized"}), 401

    try:
        user = UserModel.find_one({"name": user_name, "token": auth_token})

        if not user or user.data.get("name") != "admin":
            return jsonify({"error": "Unauthorized"}), 401

        return user, 200
    except Exception:

        return jsonify({"error": "Unauthorized"}), 401


@admin_controller.route("/history/<history_id>", methods=["DELETE"])
def delete_history_entry(history_id):

    auth_response, status_code = _check_admin_auth()
    if status_code != 200:
        return auth_response, status_code

    try:
        history = HistoryModel.find_one({"_id": ObjectId(history_id)})

        if not history:
            return "", 204

        history.delete()
        return "", 204

    except Exception:

        return jsonify({"error": "Unauthorized"}), 401
