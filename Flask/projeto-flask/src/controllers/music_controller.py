from enum import IntEnum
from models.music_model import MusicModel
from flask import Blueprint, jsonify, request


class HTTPSTATUS(IntEnum):
    OK = 200
    Created = 201
    NoContent = 204
    NotFound = 404


musics_controller = Blueprint("music", __name__)


@musics_controller.route("/", methods=["POST"])
def _save_music():
    new_music = MusicModel(request.json)
    new_music.save()
    return jsonify(new_music.to_dict()), HTTPSTATUS.Created
