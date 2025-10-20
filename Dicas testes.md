# Testes com pytest

O pytest é um framework de teste maduro e popular em Python. Ele torna a escrita de testes simples, legível e escalável.

**O Básico: Criando e Executando Testes**

**Convenção de Nomes**: O pytest automaticamente descobre testes em arquivos que começam ou terminam com `test_`(ex: test_minha_funcao.py) e em funções que começam com test_(ex: def test_soma_simples():).

Execução: Para executar, basta navegar até o diretório do projeto no terminal e digitar pytest.

```Python

## Arquivo: test_matematica.py

## A função a ser testada (assumimos que está em outro módulo, mas aqui é só para o exemplo)

def soma(a, b):
    return a + b

# Funções de teste devem começar com 'test_'
def test_soma_positivos():
    # O comando 'assert' é o coração de qualquer teste.
    # Se a expressão for False, o teste falha.
    assert soma(2, 3) == 5

def test_soma_negativos():
    assert soma(-1, -5) == -6

def test_simular_bug_divisao_por_zero():
    import pytest
    
    # Simular cenários de bugs (ex: exceções esperadas)
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

## 🛠️ Utilizando Fixtures do Pytest

Fixtures são funções que preparam o "ambiente" necessário para seus testes. Pense nelas como a infraestrutura: elas podem fornecer dados, criar conexões com o banco de dados, ou, como nas suas anotações, simular caminhos de arquivo.

### 1. Fixture `tmp_path` (Diretórios Temporários)

O `tmp_path` é perfeito para simular caminhos de arquivos ou diretórios que você precisa criar, escrever ou ler durante o teste, sem afetar seu sistema de arquivos real. Ele cria um diretório temporário exclusivo para cada teste e o limpa automaticamente depois.

```Python
# Passamos 'tmp_path' como argumento para a função de teste
def test_criacao_de_arquivo_temporario(tmp_path):
    # 1. Definir o caminho mockado dentro do diretório temporário
    # O operador '/' do 'pathlib.Path' é usado para unir caminhos
    mock_data_path = tmp_path / 'configuracao_temp.json'
    
    # 2. Criar o arquivo de fato para que a aplicação possa acessá-lo
    # O método 'touch()' cria um arquivo vazio
    mock_data_path.touch()

    # 3. Verificar se o arquivo foi criado
    assert mock_data_path.exists()
    
    # 4. Escrever algum conteúdo nele (opcional, mas comum)
    mock_data_path.write_text('{"user": "aluno"}')
    
    # 5. Ler e verificar o conteúdo
    assert mock_data_path.read_text() == '{"user": "aluno"}'
```

### 2. Fixture `monkeypatch` (Substituindo Objetos/Caminhos)

O `monkeypatch` permite que você substitua temporariamente atributos, funções ou valores de módulos, classes ou dicionários. É o mecanismo ideal para "mockar" ou simular que um arquivo está em um lugar diferente ou que uma função demorada já retornou um valor.

Combinação `tmp_path` e `monkeypatch`
Você usa o `tmp_path` para criar o arquivo falso e o `monkeypatch` para redirecionar seu código para usar esse arquivo falso.

```Python

import os
# Importação da função que vamos "mockar" o caminho.
# Exemplo: settings.py tem uma variável ARQUIVO_PADRAO
# Importante: O caminho deve ser o do *objeto* (variável) que você quer mudar.
# Neste exemplo, estamos substituindo os.getcwd() para simular que estamos em outro dir.

def minha_funcao_que_usa_o_caminho_atual():
    # Isso simula uma função do seu app que depende do caminho de trabalho
    return os.getcwd()

def test_monkeypatch_caminho_atual(tmp_path, monkeypatch):
    # O 'tmp_path' cria o caminho falso
    novo_caminho = str(tmp_path)
    
    # O 'monkeypatch.setattr' substitui temporariamente a função 'os.getcwd'
    # pelo novo caminho criado por 'tmp_path'.
    monkeypatch.setattr(os, 'getcwd', lambda: novo_caminho)
    
    # Agora, quando chamamos a função, ela usa o caminho falso.
    caminho_retornado = minha_funcao_que_usa_o_caminho_atual()
    
    # Verificamos se a substituição funcionou
    assert caminho_retornado == novo_caminho
```

### 3. Criando Suas Próprias Fixtures (e `conftest.py`)

Se você tem uma configuração complexa que precisa ser usada em vários testes, você deve criar uma Fixture personalizada.

O arquivo `conftest.py` é o arquivo de configuração do pytest.

* Visibilidade: Quaisquer fixtures definidas no `conftest.py` são automaticamente descobertas e podem ser usadas por qualquer teste em qualquer arquivo no mesmo diretório ou em subdiretórios, sem precisar de importação.
* Reutilização: Ele ajuda a manter os testes "secos" (Don't Repeat Yourself), centralizando a lógica de configuração.

```Python

# Arquivo: `conftest.py`

import pytest

# Uma fixture simples que fornece um dado (ex: um usuário de teste)
@pytest.fixture
def usuario_padrao():
    """Retorna um dicionário de um usuário de teste."""
    return {"nome": "Teacher Python", "ativo": True}

# Uma fixture com 'autouse=True' é executada automaticamente para TODOS os testes
@pytest.fixture(autouse=True)
def configuracao_global_exemplo():
    # Isso pode ser usado, por exemplo, para limpar um banco de dados
    # antes de cada teste, ou, como na sua dica, para mockar um caminho global.
    print("\n[SETUP GLOBAL EXECUTADO]")
    yield # O código após 'yield' é o 'teardown' (limpeza)
    print("\n[TEARDOWN GLOBAL EXECUTADO]")
```

```Python

# Arquivo: test_exemplo.py (no mesmo diretório)

# O pytest injeta automaticamente a fixture 'usuario_padrao'
def test_usando_fixture_personalizada(usuario_padrao):
    # Usamos o dado fornecido pela fixture
    assert usuario_padrao["nome"] == "Teacher Python"
    assert usuario_padrao["ativo"] is True
```

### 4. Testes Parametrizados

Testes parametrizados (usando `@pytest.mark.parametrize`) permitem que você execute o mesmo código de teste várias vezes com diferentes conjuntos de dados (parâmetros). Isso é ótimo para testar muitos casos de uso (como entrada e saída esperada) com menos código repetitivo.

```Python
import pytest

# 1. Definimos o decorador @pytest.mark.parametrize
# O primeiro argumento é uma string com os nomes das variáveis que serão injetadas no teste.
# O segundo argumento é uma lista de tuplas, onde cada tupla é um conjunto de valores
# correspondente às variáveis.

@pytest.mark.parametrize("input_a, input_b, expected_output", [
    (1, 2, 3),      # Caso 1: Positivos
    (0, 0, 0),      # Caso 2: Zeros
    (-5, 5, 0),     # Caso 3: Positivo e Negativo
    (-10, -5, -15)  # Caso 4: Negativos
])
def test_soma_com_parametros(input_a, input_b, expected_output):
    """Testa a função 'soma' com vários inputs diferentes."""
    # A função é executada 4 vezes, uma para cada tupla.
    assert (input_a + input_b) == expected_output
```

### 5. Ferramentas de Depuração com Testes

Para depurar (debugar) o código do seu teste ou o código que ele está chamando, você pode usar a função pytest.set_trace() em qualquer lugar do seu código de teste.

```Python

def test_depurando_o_fluxo():
    a = 10
    b = 20
    
    # Quando o pytest atingir esta linha, ele abrirá um prompt de depuração interativo (pdb).
    pytest.set_trace() 
    
    c = a + b
    
    assert c == 30
    
# Comandos úteis no PDB:
# - n (next): Executa a próxima linha.
# - s (step): Entra em uma função.
# - c (continue): Continua a execução até o próximo breakpoint ou fim do teste.
# - p (print): Imprime o valor de uma variável.
```
