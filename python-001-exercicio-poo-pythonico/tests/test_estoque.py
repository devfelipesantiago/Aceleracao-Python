import pytest

from src.estoque import Estoque

pytestmark = pytest.mark.dependency()


@pytest.fixture
def estoque():
    produtos = {"produto1": 10, "produto2": 5, "produto3": 20}
    return Estoque(produtos)


def test_init(estoque):
    assert estoque.produtos == {"produto1": 10, "produto2": 5, "produto3": 20}


def test_adicionar_produto_no_estoque(estoque):
    estoque.adicionar_produto_no_estoque("produto4", 15)
    assert estoque.produtos == {
        "produto1": 10,
        "produto2": 5,
        "produto3": 20,
        "produto4": 15,
    }

    estoque.adicionar_produto_no_estoque("produto3", 10)
    assert estoque.produtos == {
        "produto1": 10,
        "produto2": 5,
        "produto3": 30,
        "produto4": 15,
    }


def test_remover_produto_do_estoque(estoque):
    estoque.remover_produto_do_estoque("produto2", 2)
    assert estoque.produtos == {"produto1": 10, "produto2": 3, "produto3": 20}

    with pytest.raises(ValueError):
        estoque.remover_produto_do_estoque("produto3", 30)


def test_atualizar_produto_no_estoque(estoque):
    estoque.atualizar_produto_no_estoque("produto2", 8)
    assert estoque.produtos == {"produto1": 10, "produto2": 8, "produto3": 20}

    with pytest.raises(ValueError):
        estoque.atualizar_produto_no_estoque("produto4", 5)


def test_visualizar_estoque(capfd, estoque):
    estoque.visualizar_estoque()
    out, _ = capfd.readouterr()
    assert out.strip() == "produto1: 10\nproduto2: 5\nproduto3: 20"


@pytest.mark.dependency(
    depends=[
        "test_init",
        "test_adicionar_produto_no_estoque",
        "test_remover_produto_do_estoque",
        "test_atualizar_produto_no_estoque",
        "test_visualizar_estoque",
    ]
)
def test_estoque_final():
    pass
