import random
from .abstract_model import AbstractModel
from .db import db


class MusicModel(AbstractModel):
    _collection = db["musics"]

    def __init__(self, json_data):
        super().__init__(json_data)

    @classmethod
    def get_ramdom(cls):
        data = cls.find()
        if not data:
            return
        return random.choice(data)

    def to_dict(self):
        return {
            "_id": str(self.data["_id"]),
            "title": self.data["title"],
            "artist": self.data["artist"],
            "album": self.data["album"],
            "year": self.data["year"],
        }
