import json
import os


# Sim, é só receber `capsys` como parâmetro em qualquer função de teste que o
# pytest faz o resto da magia acontecer
def test_print_to_stdout(capsys):
    print("Hello, world!")
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"  # print coloca \n automaticamente


def test_error_to_stderr(capsys):
    import sys

    sys.stderr.write("Error message\n")
    captured = capsys.readouterr()
    assert captured.err == "Error message\n"


# A monkeypatch permite simular condições especificas para testes.
# o setattr substitui o input().
def my_function():
    return f"Você digitou {input('Digite algo: ')}!"


def test_my_function(monkeypatch):
    # Input recebe um parâmetro que mock_input não usa, por isso o _
    def mock_input(_):
        return "Python"

    # Trocamos a input do sistema pela nossa mock_input
    monkeypatch.setattr("builtins.input", mock_input)
    output = my_function()

    assert output == "Você digitou Python!"


# A fixture tmp_path do pytest é usada para criar um diretório
# temporário em que um teste pode criar e manipular arquivos.
# tmp_path retorna um objeto pathlib.Path, que pode ser utilizado
# como uma string de caminho para um diretório,
# bem como pode fazer mais coisas.


def generate_output(content, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(json.dumps(content))


def test_generate_output(tmp_path):
    content = {"a": 1}
    output_path = tmp_path / "out.json"
    # O operador '/' funciona na linha anterior pois temp_path não é uma
    # string comum, mas sim um objeto Path

    generate_output(content, output_path)

    assert os.path.isfile(output_path)
    with open(output_path) as file:
        assert file.read() == '{"a": 1}'
