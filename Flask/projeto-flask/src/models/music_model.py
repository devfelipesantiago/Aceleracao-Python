from pymongo.collection import Collection
from .abstract_model import AbstractModel
from .db import db


class MusicModel(AbstractModel):
    _collection: Collection = db["musics"]

    def __init__(self, json_data):
        super().__init__(json_data)

    def to_dict(self):
        return {
            "_id": str(self.data["_id"]),
            "music_name": self.data["music_name"],
        }
