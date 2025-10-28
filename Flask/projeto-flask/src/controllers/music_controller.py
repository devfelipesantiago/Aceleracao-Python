from enum import IntEnum
from models.music_model import MusicModel
from flask import Blueprint


class HTTPSTATUS(IntEnum):
    OK = 200
    Created = 201
    NoContent = 204
    NotFound = 404


musics_controller = Blueprint("music", __name__)


@musics_controller.route("/", methods=["POST"])
def _save_music(music):
    new_music = MusicModel(music)
    new_music.save()
    return jsonify(new_music.to_dict()), HTTPSTATUS.Created


@musics_controller.route("/random", methods=["GET"])
def music_random():
    music = MusicModel.get_ramdom()
    if music is None:
        return jsonify({"error": "No musics available"}), HTTPSTATUS.NotFound

    return jsonify(music.to_dict()), HTTPSTATUS.OK


@musics_controller.route("/", methods=["GET"])
def get_all_musics():
    musics = MusicModel.find()
    musics_list = [music.to_dict() for music in musics]
    return jsonify(musics_list), HTTPSTATUS.OK


@musics_controller.route("/<id>", methods=["GET"])
def get_music_by_id(id: str):
    music = MusicModel.find_one({"_id": ObjectId(id)})
    if music is None:
        return jsonify({"error": "Music not found"}), HTTPSTATUS.NotFound
    return jsonify(music.to_dict()), HTTPSTATUS.OK
