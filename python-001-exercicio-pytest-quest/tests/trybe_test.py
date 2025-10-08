import inspect
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


# * Pré requisito do teste do exercício 1
@pytest.mark.dependency()
def test_expecting_a_fixture(custom_fixture):
    assert custom_fixture.pop() == 10
    assert custom_fixture.pop() == 9


# * teste do exercício 1
@pytest.mark.dependency(depends=["test_expecting_a_fixture"])
def test_expecting_the_same_fixture(custom_fixture):
    assert custom_fixture.pop() == 8
    assert custom_fixture.pop() == 7
    assert custom_fixture.pop() == 6
    assert custom_fixture.pop() == 5
    assert custom_fixture.pop() == 4
    assert custom_fixture.pop() == 3
    assert custom_fixture.pop() == 2
    assert custom_fixture.pop() == 1
    assert custom_fixture == []


# * teste do exercício 2
@pytest.mark.dependency(
    depends=["tests/marker_test.py::test_dependency_mark"],
    scope="session",
)
def test_marker_dependency_mark():
    pass


# * teste do exercício 3
@pytest.mark.dependency(
    depends=[
        "tests/parametrized_test.py::test_converter[8-8]",
        "tests/parametrized_test.py::test_converter[9-9]",
        "tests/parametrized_test.py::test_converter[a-10]",
        "tests/parametrized_test.py::test_converter[b-11]",
        "tests/parametrized_test.py::test_converter[c-12]",
        "tests/parametrized_test.py::test_converter[e-14]",
        "tests/parametrized_test.py::test_converter[f-15]",
    ],
    scope="session",
)
def test_parametrized():
    from src.hex_converter import hexadecimal_to_decimal  # noqa
    from tests.parametrized_test import test_converter  # noqa

    with patch(
        "tests.parametrized_test.hexadecimal_to_decimal",
        wraps=hexadecimal_to_decimal,
    ) as mocked:
        test_converter("a", 10)
        mocked.assert_called_once_with("a")

        with pytest.raises(AssertionError):
            test_converter("a", 11)


# * teste do exercício 4
@pytest.mark.dependency(
    depends=["tests/built_in_fixtures_test.py::test_monkeypatch"],
    scope="session",
)
def test_use_of_monkeypatch():
    from tests.built_in_fixtures_test import test_monkeypatch  # noqa

    assert "monkeypatch" in inspect.signature(test_monkeypatch).parameters
    with patch("src.hex_converter.hexadecimal_to_decimal") as mocked:
        mocked.return_value = 10
        test_monkeypatch(monkeypatch=pytest.MonkeyPatch())
        mocked.assert_called_once_with("a")


# * teste do exercício 5
@pytest.mark.dependency(
    depends=["tests/built_in_fixtures_test.py::test_capsys"], scope="session"
)
def test_use_of_capsys():
    from tests.built_in_fixtures_test import test_capsys  # noqa

    assert "capsys" in inspect.signature(test_capsys).parameters

    mock_capsys = MagicMock()
    with pytest.raises(AssertionError):
        test_capsys(mock_capsys)

    mock_capsys.readouterr.return_value.out = "INVALID"
    mock_capsys.readouterr.return_value.err = "INVALID"
    with pytest.raises(AssertionError):
        test_capsys(mock_capsys)

    mock_capsys.readouterr.return_value.out = "10\n"
    with pytest.raises(AssertionError):
        test_capsys(mock_capsys)

    mock_capsys.readouterr.return_value.err = ""
    test_capsys(mock_capsys)


# * teste do exercício 6
@pytest.mark.dependency(
    depends=["tests/built_in_fixtures_test.py::test_tmp_path"], scope="session"
)
def test_use_of_tmp_path():
    from src.hex_converter import write_hexadecimal_to_decimal  # noqa
    from tests.built_in_fixtures_test import test_tmp_path  # noqa

    assert "tmp_path" in inspect.signature(test_tmp_path).parameters
    with pytest.raises(TypeError):
        test_tmp_path(1)

    def _mock_write_hexadecimal_to_decimal(hex_digit, output_file):
        if hex_digit != "a":
            raise ValueError(
                "Você deve testar a função `write_hexadecimal_to_decimal`"
                'com o argumento "a" para o parâmetro `hex_digit`'
            )

        if not isinstance(output_file, Path):
            raise TypeError(
                "Você deve testar a função `write_hexadecimal_to_decimal` "
                "com o argumento `output_file` sendo um objeto do tipo `Path`"
            )
        if not output_file.as_posix().endswith("/output.txt"):
            raise ValueError(
                "Você deve testar a função `write_hexadecimal_to_decimal` com "
                'o argumento terminado em "/output.txt" para o parâmetro '
                "`output_file`"
            )
        write_hexadecimal_to_decimal(hex_digit, output_file)

    with patch(
        "tests.built_in_fixtures_test.write_hexadecimal_to_decimal",
        _mock_write_hexadecimal_to_decimal,
    ):
        code = pytest.main(
            [
                "-qq",
                "--no-header",
                "--no-summary",
                "--capture=fd",
                "-k",
                "test_tmp_path",
            ]
        )

        assert code == 0
