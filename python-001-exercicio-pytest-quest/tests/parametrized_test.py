import pytest

from src.hex_converter import hexadecimal_to_decimal  # noqa: F401


@pytest.mark.parametrize(
    "hexadecimal, expected",
    [
        ("8", 8),
        ("9", 9),
        ("a", 10, AssertionError),
        ("b", 11, AssertionError),
        ("c", 12, AssertionError),
        ("e", 14, AssertionError),
        ("f", 15, AssertionError),
    ],
)
def test_converter(hexadecimal, expected):
    assert hexadecimal_to_decimal(hexadecimal) == expected


# aplica o marcador de dependency para todos os testes do arquivo
pytestmark = pytest.mark.dependency  # NÃO REMOVA ESSA LINHA
