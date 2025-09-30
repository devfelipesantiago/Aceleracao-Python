from Eletrodomestico import Eletrodomestico


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.eletrodomesticos = []

    # Permite a aquisição de qualquer eletrodoméstico
    def comprar_eletrodomestico(self, eletrodomestico):
        if eletrodomestico.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= eletrodomestico.preco
            self.eletrodomesticos.append(eletrodomestico)

        def __str__(self):
            return f"{self.nome} - possui {self.saldo_na_conta} reais em sua conta."


pessoa_cozinheira = Pessoa("Jacquin", 1000)
# pessoa_cozinheira.comprar_liquidificador(liquidificador_vermelho)
print(pessoa_cozinheira)
# retorno: Pessoa object at 0x7f53bbe1b580>


class Ventilador(Eletrodomestico):
    def __init__(self, cor, potencia, tensao, preco, quantidade_de_portas=1):
        # Chamada ao construtor da superclasse
        super().__init__(cor, potencia, tensao, preco)

        # Faz outras coisas específicas dessa subclasse
        self.quantidade_de_portas = quantidade_de_portas
