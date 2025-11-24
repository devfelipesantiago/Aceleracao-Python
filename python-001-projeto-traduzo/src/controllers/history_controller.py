from flask import Blueprint, jsonify
import json
from models.history_model import HistoryModel

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/history/", methods=["GET"])
def list_history():
    data_json = HistoryModel.list_as_json()
    try:
        data = json.loads(data_json)
    except Exception:
        data = []
    return jsonify(data), 200
