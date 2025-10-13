class _testMockBookWithoutPages:
    def __init__(self, titulo: str, autor: str, paginas: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.paginas = ""


class _testMockFailBook:
    def __init__(self, titulo: str, autor: str, paginas: int) -> None:
        self.titulo = autor
        self.autor = autor
        self.paginas = paginas
