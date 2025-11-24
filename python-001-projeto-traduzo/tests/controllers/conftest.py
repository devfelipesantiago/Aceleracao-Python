import pytest

from src.app import app
from src.models.language_model import LanguageModel


@pytest.fixture(autouse=True)
def app_test():
    app.testing = True
    return app.test_client()


@pytest.fixture(autouse=True)
def add_countries():
    list_of_languages = [
        {"name": "Afrikaans", "acronym": "af"},
        {"name": "english", "acronym": "en"},
        {"name": "Portugues", "acronym": "pt"},
    ]

    for language in list_of_languages:
        LanguageModel(language).save()
