import json
from src.models.history_model import HistoryModel


def test_request_history():
    data_json = HistoryModel.list_as_json()
    assert isinstance(data_json, str)

    data = json.loads(data_json)
    assert isinstance(data, list)

    texts = [h.get("text_to_translate") for h in data]
    assert "Hello, I like videogame" in texts
    assert "Do you love music?" in texts

    for item in data:
        assert "translate_from" in item
        assert "translate_to" in item
        assert "text_to_translate" in item
