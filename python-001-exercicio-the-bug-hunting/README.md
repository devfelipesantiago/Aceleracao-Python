# The Bug Hunting

Boas-vindas ao repositório do exercício `The Bug Hunting`!

Para realizar o exercício, atente-se a cada passo descrito a seguir! #vqv 🚀

Aqui, você vai encontrar os detalhes de como estruturar o desenvolvimento do seu exercício a partir desse repositório, utilizando uma branch específica e um _Pull Request_ para colocar seus códigos.

<br />

# Termos e acordos

Ao iniciar este exercício, você concorda com as diretrizes do [Código de Conduta e do Manual da Pessoa Estudante da Trybe](https://app.betrybe.com/learn/student-manual/codigo-de-conduta-da-pessoa-estudante).

<br />

# Entregáveis

<details>
<summary><strong>🤷🏽‍♀️ Como entregar</strong></summary><br />

Para entregar o seu exercício, você deverá criar um _Pull Request_ neste repositório.

Lembre-se que você pode consultar nosso conteúdo sobre [Git & GitHub](https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/fc998c60-386e-46bc-83ca-4269beb17e17/section/fe827a71-3222-4b4d-a66f-ed98e09961af/day/1a530297-e176-4c79-8ed9-291ae2950540/lesson/2b2edce7-9c49-4907-92a2-aa571f823b79) e nosso [Blog - Git & GitHub](https://blog.betrybe.com/tecnologia/git-e-github/) sempre que precisar!

</details>
  
<details>
<summary><strong>🧑‍💻 O que deverá ser desenvolvido</strong></summary><br />

Neste exercício, você vai praticar os seus conhecimentos em Python e a habilidade de debugar código.

Para isso, você vai receber algumas pequenas aplicações em Python que possuem alguns erros no código que impedem que ele funcione corretamente. Seu trabalho será identificar e corrigir esses erros!

<br />

</details>
  
<details>
  <summary><strong>:memo: Habilidades a serem trabalhadas</strong></summary><br />

Neste exercício, verificamos se você é capaz de:

- Identificar erros em código Python
- Corrigir erros em código Python
- Utilizar a ferramenta de debug integrada ao VS Code
- Escrever código Python que passa em testes de integração

</details>

<br/>

# Orientações
  
<details>

   <summary><strong>‼ Antes de começar a desenvolver </strong></summary><br />

1. Clone o repositório

- Use o comando: `git clone git@github.com:tryber/python-001-exercicio-the-bug-hunting.git`
- Entre na pasta do repositório que você acabou de clonar:
  - `cd python-001-exercicio-the-bug-hunting`

2. Instale as dependências

- Siga os passos do tópico [**🏕️ Ambiente Virtual**]

3. Crie uma branch a partir da branch `main`

- Verifique que você está na branch `main`
  - Exemplo: `git branch`
- Se você não estiver, mude para a branch `main`
  - Exemplo: `git checkout main`
- Agora, crie uma branch à qual você vai submeter os `commits` do seu exercício:
  - Você deve criar uma branch no seguinte formato: `nome-sobrenome-nome-do-exercício`;
  - Exemplo: `git checkout -b maria-soares-exercicio-the-bug-hunting`

4. Crie na raiz do exercício os arquivos que você precisará desenvolver:

- Verifique que você está na raiz do exercício:
  - Exemplo: `pwd` -> o retorno vai ser algo tipo _/Users/maria/code/**python-001-exercicio-the-bug-hunting**_
- Crie ou edite algum arquivo necessário ao exercício

5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

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

- Usando o exemplo anterior: `git push -u origin maria-soares-exercicio-the-bug-hunting`

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

<summary><strong>⌨️ Durante o desenvolvimento</strong></summary><br />

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
  <summary><strong>🎛 Linter</strong></summary><br />

  Para garantir a qualidade do código, vamos utilizar nesses exercícios o linter `Flake8`.
  Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comandos abaixo:

  ```bash
  python3 -m flake8
  ```

  ⚠️ **PULL REQUESTS COM ISSUES DE LINTER NÃO SERÃO AVALIADAS.
  ATENTE-SE PARA RESOLVÊ-LAS ANTES DE FINALIZAR O DESENVOLVIMENTO!** ⚠️
</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary>
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

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

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no exercício.

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

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  O `pytest` possui diversos parâmetros que podem ser utilizados para executar os testes de diferentes formas. Alguns exemplos são:

  ```bash
  python3 -m pytest tests/test_nome_do_arquivo.py  # Executa todos os testes do arquivo de testes especificado
  python3 -m pytest tests/test_nome_do_arquivo.py::test_nome_do_teste  # Executa apenas o teste especificado
  python3 -m pytest -k expressao  # Executa apenas os testes que contém a expressão informada como substring
  python3 -m pytest -x  # Executa os testes até encontrar o primeiro erro
  ```

  Você pode combinar os parâmetros para executar os testes da forma que desejar! Para mais informações, consulte a [documentação do pytest](https://docs.pytest.org/en/6.2.x/contents.html).
</details>

# Exercícios

📍 **Dica importante:** Os exercícios envolvem a alteração de códigos existentes para que bugs sejam corrigidos, mas não esperamos que você faça grandes alterações.

👎 Você não deve alterar assinaturas de funções (como o nome da função ou os parâmetros que ela recebe), nem removê-las. Você também não deve alterar os testes, apenas o código que está sendo testado.

👍 Você pode adicionar uma nova função, alterar uma condicional, remover uma linha, etc.

## 1. Identifique e corrija os erros no arquivo `src/word_finder.py`

No arquivo `src/word_finder.py` há um código que deveria retornar uma lista de linhas de um arquivo que contém uma determinada palavra. Porém, há 2 erros no código que impedem que ele funcione corretamente.

Seu objetivo é identificar e corrigir os erros no código.

<details>

<summary> Como o código deveria funcionar </code>
</summary><br/>

A aplicação do arquivo `src/word_finder.py` deve ser executada da seguinte forma:

```bash
python3 src/word_finder.py
```

Ao executar o comando acima, a aplicação deveria retornar uma lista de linhas de um arquivo que contém uma determinada palavra. No código atual, a palavra que está sendo buscada é `python` e o arquivo que está sendo lido é o `data/word_finder.txt`.

Nesse caso, a saída esperada é a seguinte:

```txt
[1, 2, 3, 4, 6, 8]
```

</details>

## 2. Identifique e corrija os erros no arquivo `src/spotify.py`

No arquivo `src/spotify.py` há um código que deveria processar as músicas do arquivo `data/spotify.csv` e retornar a análise solicitada na linha de comando.

Porém, há 2 erros no código que impedem que ele funcione corretamente.

Seu objetivo é identificar e corrigir os erros no código.

<details>

<summary> Como o código deveria funcionar </code>
</summary><br/>

As possíveis análises são:

- `1`: retorna as músicas mais instrumentais;
- `2`: retorna as músicas mais dançantes;
- `3`: retorna as músicas mais enérgicas.

A aplicação do arquivo `src/spotify.py` deve ser executada da seguinte forma:

```bash
python3 src/spotify.py 1
```

Ao executar o comando acima, a aplicação deveria retornar a lista das 10 músicas "mais instrumentais", mas você pode escolher qualquer uma das análises disponíveis (`1`, `2` ou `3`).

No nosso caso, a saída esperada é:

```txt
Top 10 músicas mais instrumentais:
 1 - 'Cornfield Chase' de Hans Zimmer
 2 - 'Day One (Interstellar Theme)' de Hans Zimmer
 3 - 'Chevaliers De Sangreal - From The Da Vinci Code Original Motion Picture Soundtrack' de Hans Zimmer
 4 - 'Experience' de Ludovico Einaudi
 5 - 'The Tree' de Ludovico Einaudi
 6 - 'Temple White' de Ludovico Einaudi
 7 - 'Natural Light' de Ludovico Einaudi
 8 - 'First Step' de Hans Zimmer
 9 - 'Veridis Quo' de Daft Punk
10 - 'Goldberg Variations, BWV 988: Aria' de Johann Sebastian Bach
```

</details>

<details>
<summary><strong> 🗣 Nos dê feedbacks sobre o exercício!</strong></summary><br />

Ao finalizar e submeter o exercício, não se esqueça de avaliar sua experiência preenchendo o [formulário](https://be-trybe.typeform.com/to/ZTeR4IbH#cohort_hidden=CH1&template=betrybe/python-0x-exercicio-the-bug-hunting).
**Leva menos de 3 minutos!**

</details>

---
