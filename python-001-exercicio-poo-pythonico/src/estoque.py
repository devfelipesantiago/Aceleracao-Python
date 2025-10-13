from typing import Dict


class Estoque:
    def __init__(self, produtos: Dict[str, int]) -> None:
        self.produtos = produtos

    def adicionar_produto_no_estoque(self, nome: str, quantidade: int) -> None:
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa")

        self.produtos[nome] = self.produtos.get(nome, 0) + quantidade

    def remover_produto_do_estoque(self, nome: str, quantidade: int) -> None:
        if nome not in self.produtos:
            raise ValueError("Produto não existe no estoque")
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa")
        if self.produtos.get(nome, 0) < quantidade:
            raise ValueError("Quantidade insuficiente no estoque")

        self.produtos[nome] = self.produtos.get(nome, 0) - quantidade

    def atualizar_produto_no_estoque(
        self, nome: str, nova_quantidade: int
    ) -> None:
        if nome not in self.produtos:
            raise ValueError("Produto não existe no estoque")
        if nova_quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa")

        self.produtos[nome] = nova_quantidade

    def visualizar_estoque(self) -> None:
        for nome, quantidade in self.produtos.items():
            print(f"{nome}: {quantidade}")
