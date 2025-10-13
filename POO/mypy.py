def add_two_numbers(num1: int, num2: int):
    return num1 + num2


print(add_two_numbers(1, 2.0))

# Caso você queira que o mypy exiba as linhas que deveriam ter anotações de
# tipo mas não têm, você pode executá-lo no modo estrito: mypy app.py --strict

# tipo int é inferido sem que eu precise deixar explícito
var1 = 1

# não faça isso, é verboso e desnecessário
var2: int = 1

# importante deixar explícito que começa como int, mas pode mudar para float
var3: int | float = 1


class Person:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height
