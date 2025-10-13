from unittest.mock import patch
from pytest_dependency import build_mocked_assets
import pytest
from tests.livro import mocks, test_livro
from src.livro.livro import Livro


mocking = build_mocked_assets(mocks, Livro, test_livro.test_cria_livro)


@pytest.fixture(autouse=True, params=mocking)
def mock_it(request):
    with patch("tests.livro.test_livro.Livro", request.param):
        yield
