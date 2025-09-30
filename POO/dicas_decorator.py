from dataclasses import dataclass
from functools import cache


# O cache salva o valor temporariamente
@cache
def fibonacci(n):
    if n <= 1:
        print("ativou")
        return n
    else:
        print("ativou")
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))


@dataclass
class Pessoa:
    nome: str
    sobremone: str


felipe = Pessoa("Felipe", "Santos")
felipe.sobremone = "Santiago"
print(felipe)
