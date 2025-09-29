from functools import partial


def soma(x, y, z):
    return x + y


incrementa = partial(soma, 2, 3)
print(incrementa(4))
