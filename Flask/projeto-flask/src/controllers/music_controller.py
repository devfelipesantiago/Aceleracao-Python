from enum import IntEnum
from models.music_model import MusicModel
from flask import Blueprint, jsonify, request


class HTTPSTATUS(IntEnum):
    OK = 200
    Created = 201
    No_Content = 204
    Not_Found = 404


musics_controller = Blueprint("music", __name__)


@musics_controller.route("/", methods=["POST"])
def music_post():
    new_music = MusicModel(request.json)
    new_music.save()
    return jsonify(new_music.to_dict()), HTTPSTATUS.Created


@musics_controller.route("/random", methods=["GET"])
def music_random():
    music = MusicModel.get_random()
    return jsonify(music.to_dict()), HTTPSTATUS.OK
