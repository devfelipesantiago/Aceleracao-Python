from unittest.mock import patch
from pytest_dependency import build_mocked_assets
import pytest
from tests.descricao_livro import mocks, test_descricao_livro
from src.livro.livro import Livro

mocking = build_mocked_assets(
    mocks, Livro, test_descricao_livro.test_descricao_livro
)


@pytest.fixture(autouse=True, params=mocking)
def mock_it(request):
    with patch(
        "tests.descricao_livro.test_descricao_livro.Livro", request.param
    ):
        yield
