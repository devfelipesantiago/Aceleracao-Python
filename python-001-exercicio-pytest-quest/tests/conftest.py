import pytest


@pytest.fixture(scope="module")
def custom_fixture():
    return list(range(1, 11))
