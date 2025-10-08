# Testes com mocks e diretorios temporarios

## Fixture **tmp_path**

> O ditetório temporário serve para simular/substituir caminhos de arquivos que queremos testar.

A sintaxe do uso do `tmp_path` é:

```py
# O tmp_path é passado como parâmetro da funcao do teste.
def test_function(tmp_path):
  # Aqui substitimos o caminho relativo do arquivo pelo tmp_path.
  mock_data_path = tmp_path / 'arquivo.json'
  # para usar a variavel devemos criar o arquivo de fato com touch()
  mock_data_path.touch()
```

> Tambem há a Fixture `monkeypatch` para substituir o arquivo original.

```py
# Passa o monkeypatch como parametro.
def test_function(tmp_path, monkeypatch):
    mock_data_path = tmp_path / 'arquivo.json'
    mock_data_path.touch()

    # Usa a função setattr() para identificar o que será substituido
    monkeypatch.setattr('.../arquivo.json', mock_data_path)
```

> Essa funcao pode ser uma `Fixture` própria.

```py
# Fixture com autouse True para ser usada por qualquer teste
@pytest.fixture(autouse=True)
def patch_arq_path(tmp_path, monkeypatch):
    mock_data_path = tmp_path / 'arquivo.json'
    mock_data_path.touch()
    monkeypatch.setattr('.../arquivo.json', mock_data_path)


# Funçao do teste
def test_function():
  content = arq.read()
  assert content == []
```

## Conftest

O `consftest.py` é o arquivo de configuração do teste.
> Você pode colocar as Fixtures que criar neste conftest e todos os arquivos de testes que voce criar pode usar sua fixture.

## Unnittest

Para usar o mock do `unnittest` tem que importar o `patch` e `Mock()` do unnittest.

```py
from unittest.mock import Mock, patch

def test_function():
  mock_db_read = Mock()
  with patch('caminho da funçao read', mock_db_read):
      res = services.get_task()
  
  assert res == mock_db_read.return_once() # retorna ...
  mock_db_read.assert_called_once() # verifica se a finçao foi chamada

