from src.livro.livro import Livro


def test_descricao_livro():
    livro = Livro("pequenos jangadeiros", "Aristides Fraga Lima", 96)
    assert (
        repr(livro)
        == "O livro pequenos jangadeiros de Aristides Fraga Lima possui 96 páginas."
    )
