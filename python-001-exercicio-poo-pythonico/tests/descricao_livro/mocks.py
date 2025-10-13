class _testMockBookDescriptionWithoutTitlePart:
    """Caso em que a descrição do livro não possui a parte do título"""

    def __init__(self, titulo: str, autor: str, paginas: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f" de {self.autor}" f" possui {self.paginas} páginas."


class _testMockBookDescriptionWrongMetadata:
    """Caso em que os metadados do livro estão apresentados em ordem errada"""

    def __init__(self, titulo: str, autor: str, paginas: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return (
            f"O livro {self.autor}"
            f" de {self.autor}"
            f" possui {self.paginas} páginas."
        )
