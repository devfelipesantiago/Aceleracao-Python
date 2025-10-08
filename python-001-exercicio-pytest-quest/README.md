# Pytest Quest

Boas-vindas ao repositório do exercício `Pytest Quest`!

Para realizar o exercício, atente-se a cada passo descrito a seguir! #vqv 🚀

Aqui, você vai encontrar os detalhes de como estruturar o desenvolvimento do seu exercício a partir desse repositório, utilizando uma branch específica e um _Pull Request_ para colocar seus códigos.

## Termos e acordos

Ao iniciar este exercício, você concorda com as diretrizes do [Código de Conduta e do Manual da Pessoa Estudante da Trybe](https://app.betrybe.com/learn/student-manual/codigo-de-conduta-da-pessoa-estudante).

## Entregáveis

<details>
<summary><strong>🤷🏽‍♀️ Como entregar</strong></summary>

Para entregar o seu exercício, você deverá criar um _Pull Request_ neste repositório.

Lembre-se que você pode consultar nosso conteúdo sobre [Git & GitHub](https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/fc998c60-386e-46bc-83ca-4269beb17e17/section/fe827a71-3222-4b4d-a66f-ed98e09961af/day/1a530297-e176-4c79-8ed9-291ae2950540/lesson/2b2edce7-9c49-4907-92a2-aa571f823b79) e nosso [Blog - Git & GitHub](https://blog.betrybe.com/tecnologia/git-e-github/) sempre que precisar!

</details>
  
<details>
<summary><strong>🧑‍💻 O que deverá ser desenvolvido</strong></summary>

Vamos fazer alguns exercícios para consolidar o uso do Pytest e suas funcionalidades.
Aqui, você vai praticar a criação de fixtures, o uso de marcadores, a criação de testes parametrizados e o uso de fixtures builtin, do Pytest.
Para isso, você vai trabalhar com um conversor de números hexadecimais para decimais cujo código já está implementado, servindo apenas como base para a prática do Pytest.

</details>
  
<details>
  <summary><strong>📝 Habilidades a serem trabalhadas</strong></summary>

  Neste exercício, verificamos se você é capaz de:

- Criar seus próprios testes automatizados por meio do módulo `pytest`.
- Executar conjuntos de testes de forma automática.
- Criar suas próprias _fixtures_ de teste.
- Utilizar _fixtures_ de testes do `pytest`.
- Criar testes parametrizados.

</details>

## Orientações
  
<details>

   <summary><strong>‼ Antes de começar a desenvolver </strong></summary>

1. Clone o repositório

- Use o comando: `git clone git@github.com:tryber/python-001-exercicio-pytest-quest.git`
- Entre na pasta do repositório que você acabou de clonar:
    - `cd exercise-pytest-quest`

1. Instale as dependências

    - Siga os passos do tópico [**🏕️ Ambiente Virtual**]

2. Crie uma branch a partir da branch `main`

- Verifique que você está na branch `main`
    - Exemplo: `git branch`
- Se você não estiver, mude para a branch `main`
    - Exemplo: `git checkout main`
- Agora, crie uma branch à qual você vai submeter os `commits` do seu exercício:
    - Você deve criar uma branch no seguinte formato: `nome-sobrenome-nome-do-exercício`;
    - Exemplo: `git checkout -b maria-soares-pytest-quest`

4. Crie na raiz do exercício os arquivos que você precisará desenvolver:

- Verifique que você está na raiz do exercício:
    - Exemplo: `pwd` -> o retorno vai ser algo tipo `/Users/maria/trybe/exercicio-pytest-quest`
- Crie ou edite algum arquivo necessário ao exercício

1. Adicione as mudanças ao _stage_ do Git e faça um `commit`

- Verifique que as mudanças ainda não estão no _stage_:
    - Exemplo: `git status` (devem aparecer listados os novos arquivos em vermelho)
- Adicione o novo arquivo ao _stage_ do Git:
    - Exemplo:
        - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
        - `git status` (devem aparecer listados os arquivos em verde)
- Faça o `commit` inicial:
    - Exemplo:
        - `git commit -m 'iniciando o exercício. VAMOS COM TUDO :rocket:'` (fazendo o primeiro commit)
        - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

6. Adicione a sua branch com o novo `commit` ao repositório remoto

- Usando o exemplo anterior: `git push -u origin maria-soares-pytest-quest`

7. Crie um novo `Pull Request` _(PR)_

- Vá até a página de _Pull Requests_ do repositório no GitHub em `<url_do_repositório>/pulls`:
    - Clique no botão verde _"New pull request"_
    - Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
- Coloque um título para o seu _Pull Request_
    - Exemplo: _"Cria tela de busca"_
- Clique no botão verde _"Create pull request"_

- Adicione uma descrição para o _Pull Request_, um título nítido que o identifique, e clique no botão verde _"Create pull request"_

 <img width="1335" alt="Exemplo de pull request" src="https://user-images.githubusercontent.com/42356399/166255109-b95e6eb4-2503-45e5-8fb3-cf7caa0436e5.png">

- Volte até a página de _Pull Requests_ do repositório no GitHub em `<url_do_repositório>/pulls` e confira que o seu _Pull Request_ está criado

</details>

<details>

<summary><strong>⌨️ Durante o desenvolvimento</strong></summary>

Faça `commits` das alterações que você fizer no código regularmente, pois assim você garante visibilidade para o time da Trybe e treina essa prática para o mercado de trabalho :) ;

- Lembre-se de sempre após um (ou alguns) `commits` atualizar o repositório remoto;
- Os comandos que você utilizará com mais frequência são:
    - `git status` _(para verificar o que está em vermelho - fora do stage - e o que está em verde - no stage)_;
    - `git add` _(para adicionar arquivos ao stage do Git)_;
    - `git commit` _(para criar um commit com os arquivos que estão no stage do Git)_;
    - `git push -u origin nome-da-branch` _(para enviar o commit para o repositório remoto na primeira vez que fizer o `push` de uma nova branch)_;
    - `git push` _(para enviar o commit para o repositório remoto após o passo anterior)_.

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary>
  O Python oferece um recurso chamado de ambiente virtual, que permite sua máquina rodar sem conflitos diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **Criar o ambiente virtual**

  ```bash
  python3 -m venv .venv
  ```

  2. **Ativar o ambiente virtual**

  ```bash
  source .venv/bin/activate
  ```

  3. **Instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  
  Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no exercício.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no exercício, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.

  Se o VS Code não reconhecer as dependências instaladas no ambiente virtual criado, será necessário informar o caminho do interpretador Python. Para isso, abra o VS Code e pressione `Ctrl + Shift + P` (no Mac, `Cmd + Shift + P`) e digite `Python: Select Interpreter`. Selecione o interpretador que possui o caminho `./.venv/bin/python` no nome.
</details>

<details>
<summary><strong>🎛 Linter</strong></summary>

Para garantir a qualidade do código, vamos utilizar nesses exercícios o linter `Flake8`. Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível e de fácil manutenção! Para poder executar o `Flake8`, certifique-se de ter seguido os passos do tópico [**🏕️ Ambiente Virtual**] dentro do repositório.

Para rodá-lo localmente no repositório, execute o comando a seguir:

```bash
python3 -m flake8
```

Se a análise do `Flake8` encontrar problemas no seu código, tais problemas serão mostrados no seu terminal. Se não houver problema no seu código, nada será impresso no seu terminal.

Você pode também pode contar com a ajuda do `Flake8` no `VSCode`. Para isso, basta instalar a [extensão oficial do VS Code para a linguagem Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

Em caso de dúvidas, confira o material na plataforma sobre [configuração do ambiente Python](https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/f04cdb21-382e-4588-8950-3b1a29afd2dd/section/aa76abc8-b842-40d9-b5cc-baa960952129/lesson/dd80466d-31d4-4b35-bacf-d789e261fa7d).

⚠️ **PULL REQUESTS COM ISSUES NO LINTER NÃO SERÃO AVALIADAS. ATENTE-SE PARA RESOLVÊ-LAS ANTES DE FINALIZAR O DESENVOLVIMENTO!** ⚠️

</details>

<details>
  <summary><strong>🛠 Testes</strong></summary>

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o Pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  O `pytest` possui diversos parâmetros que podem ser utilizados para executar os testes de diferentes formas. Alguns exemplos são:

  ```bash
  python3 -m pytest tests/test_nome_do_arquivo.py  # Executa todos os testes do arquivo de testes especificado
  python3 -m pytest tests/test_nome_do_arquivo.py::test_nome_do_teste  # Executa apenas o teste especificado
  python3 -m pytest -k expressão  # Executa apenas os testes que contém a expressão informada como substring
  python3 -m pytest -x  # Executa os testes até encontrar o primeiro erro
  ```

  Você pode combinar os parâmetros para executar os testes da forma que desejar! Para mais informações, consulte a [documentação do Pytest](https://docs.pytest.org/en/6.2.x/contents.html).
</details>

## Exercícios

### 1. Crie uma fixture

Neste primeiro exercício, você vai praticar a criação de uma fixture simples.

<details>

<summary> O que você deve fazer </summary>

Crie o arquivo `tests/conftest.py`.
Em seguida, crie neste arquivo a fixture `custom_fixture`, com o escopo de módulo (ou mais abrangente, como sessão) e que retorna uma lista Python com os números de 1 a 10, incluindo o 1 e o 10.

**O que será testado:**

 - Se a fixture `custom_fixture` pode ser acessada por uma função de teste em um arquivo de teste que não pode ser modificado.
 - Se a fixture `custom_fixture` retorna uma lista Python com os números de 1 a 10, incluindo o 1 e o 10, sendo que os testes fazem a remoção do 1 e do 10 da lista retornada pela fixture.
 - Se a fixture `custom_fixture` tem escopo de módulo, pacote ou sessão, sendo que um segundo teste tenta remover os itens da lista de onde parou o primeiro teste.

</details>

### 2. Use um marcador

Neste segundo exercício, você vai praticar o uso de marcadores do Pytest.

<details>

<summary> O que você deverá fazer </summary>

Crie um arquivo `tests/marker_test.py`. Em seguida crie neste arquivo a função de teste `test_dependency_mark`, cujo resultado do teste deve sempre passar. Marque o teste com o marcador `dependency`.

**O que será testado:**

  - Se uma função de teste identificada como `tests/marker_test.py::test_dependency_mark` está marcada com o marcador `dependency`.
  - Se a mesma função citada acima roda com sucesso.

</details>

### 3. Crie testes parametrizados

Agora chegou a hora de praticar a criação de testes parametrizados, evitando a repetição de código.

<details>

<summary> O que você deverá fazer </summary>

No arquivo previamente criado `tests/parametrized_test.py`, crie uma função de teste parametrizada chamada `test_converter` para testar a função `src.hex_converter.hexadecimal_to_decimal`.

A função de teste deve receber dois parâmetros, sendo o primeiro o número hexadecimal na forma de uma string e o segundo o número decimal inteiro equivalente.

O conjunto de valores passados para o marcador de parametrização deve ser o seguinte:

- Hexadecimal `"8"`, inteiro na saída `8`.
- Hexadecimal `"9"`, inteiro na saída `9`.
- Hexadecimal `"a"`, inteiro na saída `10`.
- Hexadecimal `"b"`, inteiro na saída `11`.
- Hexadecimal `"c"`, inteiro na saída `12`.
- Hexadecimal `"e"`, inteiro na saída `14`.
- Hexadecimal `"f"`, inteiro na saída `15`.

Importante ressaltar que o valor hexadecimal `"d"` e seu correspondente inteiro `13` foram deliberadamente omitidos da lista de parâmetros.

O corpo do teste deve verificar se passar o número hexadecimal como parâmetro para a função `hexadecimal_to_decimal` retorna o número decimal esperado.

**O que será testado:**

  - Se o teste `test_converter` existe e está marcado com o marcador `dependency` (o arquivo do teste já deixa o marcador aplicado em todas as funções de teste, basta não remover a linha que faz isso).
  - Se o teste `test_converter` é um teste parametrizado com os valores citados acima.
  - Se o teste `test_converter` verifica o correto funcionamento da função `hexadecimal_to_decimal` para cada parâmetro passado.
    - Se a função `hexadecimal_to_decimal` é chamada pelo teste `test_converter` com o parâmetro correto.
    - Se o teste `test_converter` falha com um `AssertionError` quando chamado com parâmetros cuja conversão não retorna o valor esperado.

</details>

### 4. Use fixtures builtin - `monkeypatch`

Neste exercício, você vai praticar o uso de fixtures builtin, do Pytest, mais especificamente a `monkeypatch`.

<details>

<summary> O que você deverá fazer </summary>

No arquivo previamente criado `tests/built_in_fixtures_test.py`, crie uma função de teste chamada `test_monkeypatch`.
Esta função deve utilizar a fixture `monkeypatch` para validar se a chamada a `src.hex_converter.main` retorna `10` quando a pessoa que usa a aplicação digitar a string `"a"`.

**O que será testado:**

  - Se o teste `test_monkeypatch` passa.
  - Se o teste `test_monkeypatch` recebe a fixture `monkeypatch`.
  - Se o teste `test_monkeypatch` utiliza a fixture `monkeypatch` para simular a entrada do valor "a".
  - Se a função `src.hex_converter.hexadecimal_to_decimal` é chamada, indiretamente, com o valor "a" como parâmetro.
  - Se o teste `test_monkeypatch` faz uma asserção do resultado da passagem indireta do valor "a" para a função `src.hex_converter.hexadecimal_to_decimal`.
  - **Observação:** não importe nem chame diretamente a função `src.hex_converter.hexadecimal_to_decimal` no teste `test_monkeypatch`.

</details>

### 5. Use fixtures builtin - `capsys`

Neste exercício, você vai praticar o uso de fixtures builtin, do Pytest, mais especificamente a `capsys`.

<details>

<summary> O que você deverá fazer </summary>

No arquivo previamente criado `tests/built_in_fixtures_test.py`, crie uma função de teste chamada `test_capsys`.
Esta função deve utilizar a fixture `capsys` para validar se a função `src.hex_converter.print_hexadecimal_to_decimal` imprime `10\n` na saída padrão e uma string vazia na saída de erro padrão quando chamada com a string `"a"`.

**O que será testado:**

  - Se o teste `test_capsys` passa.
  - Se o teste `test_capsys` utiliza a fixture `capsys` para ler a saída padrão e a saída de erro padrão.
  - Se o teste `test_capsys` chama a função `print_hexadecimal_to_decimal` com o parâmetro "a" e verifica se:
      - a saída padrão é igual a string `10\n`;
      - a saída de erro padrão é uma string vazia.

</details>

### 6. Use fixtures builtin - `tmp_path`

Neste exercício, você vai praticar o uso de fixtures builtin, do Pytest, mais especificamente a `tmp_path`.

<details>

<summary> O que você deverá fazer </summary>

No arquivo previamente criado `tests/built_in_fixtures_test.py`, crie uma função de teste chamada `test_tmp_path`. Esta função deve utilizar a fixture `tmp_path` para criar um arquivo temporário chamado "output.txt" dentro de um diretório temporário.

Em seguida, este diretório deve ser passado como segundo parâmetro da função `write_hexadecimal_to_decimal`, sendo o primeiro parâmetro a string `"a"`.

Por fim, o teste deve verificar se o conteúdo do arquivo "output.txt" é igual a string `"10"`.

Dica: utilize o método `pathlib.Path().read_text()`.

Dica: o teste não traz um retorno devidamente descritivo quando falha. Ative o debugger e ative o breakpoint `User Uncaught Exceptions` na aba `Breakpoints` no menu do debugger.

**O que será testado:**

  - Se o teste `test_tmp_path` existe e está marcado com o marcador `dependency` (o arquivo do teste já deixa o marcador aplicado em todas as funções de teste, basta não remover a linha que faz isso).
  - Se o teste `test_tmp_path` passa.
  - Se o teste `test_tmp_path` recebe a fixture `tmp_path`.
  - Se o teste `test_tmp_path` utiliza a fixture `tmp_path` para criar um arquivo temporário chamado "output.txt" dentro de um diretório temporário.
  - Se o teste `test_tmp_path` chama a função `write_hexadecimal_to_decimal` com o parâmetro "a" e o caminho do arquivo temporário criado.
      - O parâmetro do caminho do arquivo temporário deve ser passado como um objeto `pathlib.Path`.
      - O parâmetro do caminho do arquivo temporário deve terminar com "/output.txt".
  - Se o teste `test_tmp_path` verifica se o conteúdo do arquivo "output.txt" é igual a string `"10"`.
  - Se o teste `test_tmp_path` falha com um `TypeError` quando a fixture `tmp_path` é substituída por número inteiro.
  - Observação: O teste roda programaticamente o Pytest, criando uma execução dentro do próprio Pytest.
    Isso é feito para que o teste possa verificar se o arquivo "output.txt" foi criado dentro do diretório temporário,
    visto que se fosse feito de outra forma, o teste criaria um arquivo em um diretório não temporário.

</details>

---

<details>
<summary><strong> 🗣 Nos dê feedbacks sobre o exercício!</strong></summary>

Ao finalizar e submeter o exercício, não se esqueça de avaliar sua experiência preenchendo o [formulário](https://be-trybe.typeform.com/to/ZTeR4IbH#cohort_hidden=CH1&template=betrybe/python-0x-exercicio-pytest-quest).
**Leva menos de 3 minutos!**

</details>

<!-- mdi versão 1.0 exercício como projeto python ⚠️ não exclua esse comentário -->
