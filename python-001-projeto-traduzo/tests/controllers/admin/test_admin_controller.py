from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    user = UserModel({"name": "admin", "token": "token123"}).save()

    h1 = HistoryModel(
        {
            "text_to_translate": "Foo",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()

    before = len(HistoryModel.find())

    response = app_test.delete(
        f"/admin/history/{h1.id}",
        headers={
            "Authorization": user.data["token"],
            "User": user.data["name"],
        },
    )

    assert response.status_code == 204

    after = len(HistoryModel.find())
    assert after == before - 1
