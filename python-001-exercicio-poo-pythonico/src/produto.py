class Produto:

    def __init__(
        self, nome: str, codigo: str, preco: float, quantidade: int
    ) -> None:
        self.__nome = nome
        self.__codigo = codigo
        self.__preco = preco
        self.__quantidade = quantidade

    def get_preco(self) -> float:
        return self.__preco

    def get_quantidade(self) -> int:
        return self.__quantidade

    def atualizar_preco_do_produto(self, novo_preco: float) -> None:
        if self.valida_preco(novo_preco):
            self.__preco = novo_preco

    def adicionar_estoque_do_produto(self, quantidade: int) -> None:
        self.__quantidade += quantidade

    def remover_estoque_do_produto(self, quantidade: int) -> None:
        if quantidade > self.__quantidade:
            raise ValueError("Quantidade indisponível em estoque.")
        self.__quantidade -= quantidade

    def valida_preco(self, preco: float) -> bool:
        if preco <= 0:
            self.__preco = 0.0
            raise ValueError("O preço deve ser maior que zero.")
        return preco > 0
