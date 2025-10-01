from abc import ABC, abstractmethod


class DebitoAutomatico:
    @classmethod
    def debitar1(cls, conta, valor, banco):
        if banco == "itau":
            # Codigo específico do Itaú (exemplo)
            # connect_server_udp(itau_line)
            # itau_line.check_system()
            # itau_zig_zag(valor, 'Token 454')
            print("Débito realizado pelo Itau")
        elif banco == "Santander":
            # Codigo específico do Santander (exemplo)
            # connect_server_tcp(santander_line)
            # santander_line.check_ping()
            # metodo_106(valor)
            print("Santander, Débito efetuado!")
        elif banco == "Bradesco":
            # Codigo específico do Bradesco (exemplo)
            print("Sucesso!")
        # ... + 150 bancos...
        elif banco == "Caixa":
            # Codigo específico da Caixa (exemplo)
            print("Efetuado com sucesso, Caixa Agradece!")


DebitoAutomatico.debitar1(120, 123, "itau")
DebitoAutomatico.debitar1(110, 456, "Santander")
DebitoAutomatico.debitar1(120, 789, "Bradesco")


class BancoStrategy(ABC):  # Interface
    @classmethod
    @abstractmethod
    def debitar(cls, conta, valor):
        raise NotImplementedError


class ItauStrategy(BancoStrategy):
    @classmethod
    def debitar(cls, conta, valor):
        # Codigos específico do Itau (exemplo)
        print("Débito realizado pelo Itau")


class SantanderStrategy(BancoStrategy):
    @classmethod
    def debitar(cls, conta, valor):
        # Codigos específico do Santander (exemplo)
        print("Santander, Débito efetuado!")


class BradescoStrategy(BancoStrategy):
    @classmethod
    def debitar(cls, conta, valor):
        # Codigos específico do Bradesco (exemplo)
        print("Sucesso!")


# ... métodos para todos os bancos
