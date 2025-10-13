# Boas-vindas ao repositório do exercício Loja Virtual Pythonica

Para realizar o exercício, atente-se a cada passo descrito a seguir! #vqv 🚀

Aqui, você vai encontrar os detalhes de como estruturar o desenvolvimento do seu exercício a partir desse repositório, utilizando uma branch específica e um _Pull Request_ para colocar seus códigos.

Nesse exercício prático, vamos desenvolver um sistema de gerenciamento de estoque para uma loja virtual utilizando "Programação Orientada a Objetos (POO)" em Python. Você será desafiado a criar classes e métodos que permitirão o controle eficiente do estoque. Vamos lá?

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

Neste exercício, você vai praticar os seus conhecimentos de POO em Python. Você vai criar um programa que simula uma loja virtual elaborando códigos que façam o uso de _tipagem estática_ em Python.

</details>
  
<details>
  <summary><strong>📝 Habilidades a serem trabalhadas</strong></summary><br />

Neste exercício, verificamos se você é capaz de:

- Elaborar códigos que façam o uso de _tipagem estática_ em Python.
- Elaborar códigos utilizando a linguagem Python que utilizam _Classes_, _Construtores_, _Instâncias_, _Atributos_ e _Métodos_.
- Examinar um projeto em Python que utiliza o paradigma de _Programação Orientada a Objetos_.
- Escrever código Python que passa em testes de integração.

</details>

# Orientações específicas deste projeto

<details>
  <summary>
    📌 <strong>Como seu teste é avaliado</strong>
  </summary>
  O <strong>teste da Trybe</strong> irá avaliar se o <strong>seu teste</strong> está passando conforme seu objetivo, e confirmará se ele está falhando em alguns casos que deve falhar.
  Para estes testes que esperemos que falhe, o requisito será considerado atendindo quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code>, ao invés de <code>PASS</code> ou <code>FAIL</code>.
</details>

# Orientações que você já conhece 😉

<details>

   <summary><strong>‼ Antes de começar a desenvolver </strong></summary><br />

<!-- [HS] Aqui, deve-se adicionar os comandos mais utilizados e orientações de como preparar o repositório. Atualize o nome do repositório do exercício nas instruções a seguir -->

1. Clone o repositório

- Use o comando: `git clone git@github.com:tryber/python-001-exercicio-poo-pythonico.git`
- Entre na pasta do repositório que você acabou de clonar:
  - `cd python-001-exercicio-poo-pythonico`

2. Crie uma branch a partir da branch `main`

- Verifique que você está na branch `main`
  - Exemplo: `git branch`
- Se você não estiver, mude para a branch `main`
  - Exemplo: `git checkout main`
- Agora, crie uma branch à qual você vai submeter os `commits` do seu exercício:
  - Você deve criar uma branch no seguinte formato: `nome-sobrenome-nome-do-exercício`;
  - Exemplo: `git checkout -b maria-soares-lessons-learned`

3. Crie / altere os arquivos que precisar para desenvolver os requisitos

4. Adicione as mudanças ao _stage_ do Git e faça um `commit`

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

5. Adicione a sua branch com o novo `commit` ao repositório remoto

- Usando o exemplo anterior: `git push -u origin maria-soares-lessons-learned`

6. Crie um novo `Pull Request` _(PR)_

- Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/tryber/sd-0x-project-lessons-learned/pulls)
  - Clique no botão verde _"New pull request"_
  - Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
- Coloque um título para o seu _Pull Request_
  - Exemplo: _"Cria tela de busca"_
- Clique no botão verde _"Create pull request"_

- Adicione uma descrição para o _Pull Request_, um título nítido que o identifique, e clique no botão verde _"Create pull request"_

 <img width="1335" alt="Exemplo de pull request" src="https://user-images.githubusercontent.com/42356399/166255109-b95e6eb4-2503-45e5-8fb3-cf7caa0436e5.png">

- Volte até a [página de _Pull Requests_ do repositório](https://github.com/tryber/sd-0x-project-lessons-learned/pulls) e confira que o seu _Pull Request_ está criado

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

Para garantir a qualidade do código, vamos utilizar nesses exercícios o linter `Flake8`. Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comandos abaixo:

```bash
python3 -m flake8
```

⚠️ **PULL REQUESTS COM ISSUES DE LINTER NÃO SERÃO AVALIADAS.
ATENTE-SE PARA RESOLVÊ-LAS ANTES DE FINALIZAR O DESENVOLVIMENTO!** ⚠️

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  
O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

1. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

2. Ativar o ambiente virtual

```bash
source .venv/bin/activate
```

3. Instalar as dependências no ambiente virtual

```bash
python3 -m pip install -r dev-requirements.txt
```

Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.

</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

<strong>Executar os testes</strong>

```bash
python3 -m pytest
```

O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

```bash
python3 -m pytest -s -vv
```

Caso precise executar apenas um arquivo de testes basta executar o comando:

```bash
python3 -m pytest tests/nomedoarquivo.py
```

Caso precise executar apenas uma função de testes basta executar o comando:

```bash
python3 -m pytest -k nome_da_func_de_tests
```

Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

```bash
python3 -m pytest -x tests/test_jobs.py
```

Para executar um teste específico de um arquivo, basta executar o comando:

```bash
python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
```

Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

</details>

## Quando finalizar o projeto não esquecer

<details>
<summary><strong>🗂 Compartilhe seu portfólio!</strong></summary>
  <br />

Você sabia que o LinkedIn é a principal rede social profissional e compartilhar o seu aprendizado lá é muito importante para quem deseja construir uma carreira de sucesso? Compartilhe esse projeto no seu LinkedIn, marque o perfil da Trybe (@trybe) e mostre para a sua rede toda a sua evolução.

</details>

<details>
<summary><strong>🗣 Nos dê feedbacks sobre o projeto!</strong></summary>
  <br />

Ao finalizar e submeter o projeto, não se esqueça de avaliar sua experiência preenchendo o formulário.
**Leva menos de 3 minutos!**

[Formulário de avaliação do projeto](https://be-trybe.typeform.com/to/ZTeR4IbH#cohort_hidden=CH1&template=betrybe/python-0x-exercicio-poo-pythonico)

</details>

## Requisitos

### 1 - Desenvolver a classe `Produto`

> **Implemente em:** `src/produto.py`

<details>

<summary><strong>Crie uma classe <code>Produto</code></strong>
</summary><br/>
 
Seu objetivo é implementar uma classe chamada `Produto`, que representa um produto no estoque. Essa classe deve conter as seguintes características:

**Atributos**:

- `nome (string)` - será inicializado com o valor do parâmetro;
- `código (string)` - será inicializado com o valor do parâmetro;
- `preço (float)` - será inicializado com o valor do parâmetro;
- `quantidade (int)` - será inicializado com o valor do parâmetro.

Todos os atributos devem ser privados.

Além disso, a classe deve possuir os seguintes métodos:

**Métodos**:

- `__init__` - construtor que inicializa os atributos da classe.
- `atualizar_preco` - método que atualiza o preço do produto. O preço não pode ser negativo.
- `adicionar_estoque_do_produto` - método que adiciona a quantidade informada ao estoque do produto.
- `remover_estoque_do_produto` - método que remove a quantidade informada do estoque do produto. Deve verificar se existe a possibilidade de remover a quantidade pedida e lançar um `ValueError` caso isso não seja possível.

🤖 **O que será verificado pelo avaliador**

- **1.1** - Será validado se o construtor **init** inicializa os atributos da classe corretamente;

- **1.2** - Será validado o método que atualiza o preço do produto;

- **1.3** - Será validado o método que adiciona a quantidade informada ao estoque do produto;

- **1.4** - Será validado o método que remove a quantidade informada do estoque do produto e;

- **1.5** - Será validado que o método `remove_estoque` deve lançar a exceção (`ValueError`) com a mensagem correspondente quando não existe a possibilidade de remover a quantidade pedida.

</details>

### 2 - Desenvolver a classe `Estoque`

> **Implemente em:** `src/estoque.py`

<details>

<summary><strong>Crie uma classe <code>Estoque</code></strong>
</summary><br/>

Sua tarefa é implementar a classe `Estoque` utilizando tipagem estática. A classe deve permitir a adição, remoção e atualização de produtos no estoque, além de permitir a visualização do estoque atualizado. Essa classe deve conter as seguintes características:

**Atributos**:

- `produtos (dict)` - dicionário que armazena os produtos do estoque e suas quantidades;

Além disso, a classe deve possuir os seguintes métodos:

**Métodos**:

- `__init__ (self, produtos : dict)` - construtor que inicializa o dicionário produtos.
- `adicionar_produto_no_estoque(self, nome: str, quantidade: int)` - método que adiciona um produto ao estoque, juntamente com sua quantidade. Caso o produto já exista no estoque, a quantidade deve ser somada à quantidade já existente.
- `remover_produto_do_estoque(self, nome: str, quantidade: int)` - método que remove um produto do estoque, juntamente com sua quantidade. Caso a quantidade informada seja maior do que a quantidade disponível no estoque, o método deve lançar uma exceção (ValueError).
- `atualizar_produto_no_estoque(self, nome: str, nova_quantidade: int)` - método que atualiza a quantidade de um produto no estoque. Caso o produto não exista no estoque, o método deve lançar uma exceção (ValueError).
- `visualizar_estoque(self)` - método que exibe o estoque atualizado.

🤖 **O que será verificado pelo avaliador**

- **2.1** - Será validado se o construtor **init** inicializa os atributos da classe corretamente;

- **2.2** - Será validado o método que adiciona um produto ao estoque;

- **2.3** - Será validado o método que remove um produto do estoque;

- **2.4** - Será validado o método que atualiza um produto do estoque. Caso o produto não exista no estoque, o método deve lançar uma exceção (ValueError) e;

- **2.5** - Será validado o método que exibe o estoque atualizado;

</details>

### 3 - Testar o construtor/inicializador da classe Livro

> **Crie o teste em:** tests/livro/test_livro.py

<details>

<summary><strong>Crie o teste do construtor/inicializador para a classe <code>Livro</code></strong>
</summary><br/>

Dentro do arquivo `src/livro/livro.py` você encontrará a classe `Livro` já criada.

Agora você precisa implementar um teste que certifica se o método `__init__` da classe `Livro` esta funcionando corretamente.

O nome deste teste deve ser `test_cria_livro`, e ele deve verificar se é possível criar um objeto do tipo Livro com os seguintes atributos:

- `titulo (string)`
- `autor (string)`
- `paginas (int)`

  🤖 **O que será verificado pelo avaliador**

- **3.1** - Seu teste teste deve garantir que a classe cria um novo livro com todos os atributos corretamente preenchidos.

</details>

### 4 - Testar a descrição do Livro

> **Crie o teste em:** tests/descricao_livro/test_descricao_livro.py

<details>

<summary><strong>Crie o teste para o método que traz a descrição do <code>Livro</code></strong>
</summary><br/>

Agora precisamos testar se a descrição do livro está sendo retornada corretamente.

Para desenvolver este relatório, utilizamos o recurso `__repr__` do Python, que permite alterar a representatividade do objeto, para que sempre que usarmos um print nele, no lugar de endereço de memória, teremos uma String personalizada.

Exemplo de frase:

> O livro pequenos jangadeiros, de Aristides Fraga Lima, possui 96 páginas.

O nome deste teste deve ser `test_descricao_livro`, e ele deve instanciar um objeto Livro e verificar se é retornada a frase correta.

🤖 **O que será verificado pelo avaliador**

- **3.2** - Se seu código testa que o retorno padrão (**repr**) de um objeto `Livro` deve possuir a descrição que esperamos dele.

</details>
