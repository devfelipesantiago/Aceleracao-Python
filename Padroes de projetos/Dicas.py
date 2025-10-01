from operator import add, sub
import sys


FUNCS = {"soma": add, "subtrai": sub}

try:
    _, func, n1, n2 = sys.argv
    n1, n2 = int(n1), int(n2)
    result = FUNCS[func](n1, n2)
except ValueError:
    print(
        "argumentos incorretos de entrada, experimente python arquivo.py " "soma 2 2",
        file=sys.stderr,
    )
except KeyError:
    available_functions = ", ".join(FUNCS.keys())
    print(f"Função indisponível, tente uma destas: {available_functions}")
else:
    print(f"O resultado da operação {func} foi {result}")


opcao = 1
while opcao != 0:
    n1 = int(input("Digite um numero:"))
    n2 = int(input("Digite outro numero:"))
    opcao = int(
        input(
            """
Escolha uma opcao:
1 - soma
2 - subtrair
0 - sair
"""
        )
    )
    if opcao == 1:
        print(n1 + n2)
    elif opcao == 2:
        print(n1 - n2)
