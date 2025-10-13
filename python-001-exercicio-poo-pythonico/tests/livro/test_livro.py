from src.livro.livro import Livro


def test_cria_livro():
    livro = Livro("Python 101", "John Doe", 10)
    assert isinstance(livro, Livro)
    assert livro.titulo == "Python 101"
    assert livro.autor == "John Doe"
    assert livro.paginas == 10
