def sum_two_numbers(a, b):
    """Retorna a soma de dois números recebidos por parâmetro.

    Exemplos
    --------
    >>> sum_two_numbers(0, 0)
    0
    >>> sum_two_numbers(2, 2)
    4
    """
    return a + b


def test_soma_dois_inteiros():
    # arranjo
    a = 3
    b = 6

    # acao
    soma = sum_two_numbers(a, b)

    # Aferição
    assert soma == 9
    assert sum_two_numbers(a, b) == 9
