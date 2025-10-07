import pytest


@pytest.fixture(scope="session", autouse=True)
def faker_locale():
    return "pt_BR"


@pytest.fixture(scope="session", autouse=True)
def faker_seed():
    return "BR"
