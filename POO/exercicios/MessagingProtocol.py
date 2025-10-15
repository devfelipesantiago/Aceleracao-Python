from queue import Queue
from typing import Tuple, Union, Protocol


class MessagingProtocol(Protocol):
    """Protocolo de um sistema de mensagens"""

    def send_message(self, to: str, message: str) -> bool:
        """Envia uma mensagem para um destinatário"""
        ...

    def receive_message(self) -> Union[Tuple[str, str], None]:
        """Recebe uma mensagem"""
        ...


class InMemoryMessaging(MessagingProtocol):
    def __init__(self) -> None:
        self.messages: Queue[Tuple[str, str]] = Queue()

    def send_message(self, to: str, message: str) -> bool:
        self.messages.put((to, message))
        return True

    def receive_message(self) -> Union[Tuple[str, str], None]:
        if self.messages.empty():
            return None
        return self.messages.get()


class FileMessaging(MessagingProtocol):
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def send_message(self, to: str, message: str) -> bool:
        with open(self.filename, "a") as file:
            file.write(f"{to}:{message}\n")
        return True

    def receive_message(self) -> Union[Tuple[str, str], None]:
        with open(self.filename, "r") as file:
            lines = file.readlines()
        if not lines:
            return None
        first_line = lines[0]
        with open(self.filename, "w") as file:
            file.writelines(first_line[1:])
        return first_line.split(":")[0], first_line.split(":")[1]


def main():
    in_memory_messaging = InMemoryMessaging()
    file_messaging = FileMessaging("messages.txt")

    in_memory_messaging.send_message("Julia", "Oi, tudo bem?")
    in_memory_messaging.send_message("Julia", "Como foi o seu dia?")
    in_memory_messaging.send_message("Julia", "Desejo um bom final de semana!")

    file_messaging.send_message("Paulo", "Como tá?")
    file_messaging.send_message("Paulo", "Muito obrigado!")
    file_messaging.send_message("Paulo", "Tenha um ótimo dia!")

    print(in_memory_messaging.receive_message())
    print(in_memory_messaging.receive_message())
    print(in_memory_messaging.receive_message())

    print(file_messaging.receive_message())
    print(file_messaging.receive_message())
    print(file_messaging.receive_message())


if __name__ == "__main__":
    main()
