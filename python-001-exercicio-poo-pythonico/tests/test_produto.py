import pytest
from src.produto import Produto

pytestmark = pytest.mark.dependency()


def test_criar_produto():
    p = Produto("Camiseta", "C001", 29.99, 50)
    assert p._Produto__nome == "Camiseta"
    assert p._Produto__codigo == "C001"
    assert p._Produto__preco == 29.99
    assert p._Produto__quantidade == 50


def test_atualizar_preco():
    p = Produto("Camiseta", "C001", 29.99, 50)
    p.atualizar_preco_do_produto(39.99)
    assert p.get_preco() == 39.99


def test_adicionar_estoque_do_produto():
    p = Produto("Camiseta", "C001", 29.99, 50)
    p.adicionar_estoque_do_produto(10)
    assert p.get_quantidade() == 60


def test_remover_estoque_do_produto():
    p = Produto("Camiseta", "C001", 29.99, 50)
    p.remover_estoque_do_produto(10)
    assert p.get_quantidade() == 40


def test_remover_estoque_valueerror():
    p1 = Produto("Camiseta", "001", 29.99, 10)
    with pytest.raises(ValueError):
        p1.remover_estoque_do_produto(15)


@pytest.mark.dependency(
    depends=[
        "test_criar_produto",
        "test_atualizar_preco",
        "test_adicionar_estoque_do_produto",
        "test_remover_estoque_do_produto",
        "test_remover_estoque_valueerror",
    ]
)
def test_produto_final():
    pass
