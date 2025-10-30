# Conhecendo o unittest

> 🎬 Caso você prefira consumir este conteúdo em vídeo, ele está disponível no final do tópico. Lembre-se de que os códigos apresentados no vídeo foram construídos ao longo do conteúdo escrito e que reproduzir os passos demonstrados durante o estudo é importante para o aprendizado. 😉

O `unittest` é um módulo de teste em Python que faz parte da biblioteca padrão. Ele fornece uma estrutura para escrever e executar testes automatizados, a fim de verificar a correção do código. O `unittest` permite que você defina testes unitários, que são testes focados em verificar a funcionalidade individual de partes isoladas do seu código.

Com o `unittest`, você pode criar classes de teste que herdam da classe `unittest.TestCase`. Dentro dessas classes de teste, você pode definir métodos de teste, que são funções que verificam se um determinado comportamento do código está de acordo com o esperado. Esses métodos de teste podem conter chamadas a várias asserções fornecidas pelo `unittest`, que verificam se determinadas condições são verdadeiras.

Além disso, o `unittest` também fornece recursos para configurar e limpar o ambiente de teste, lidar com exceções e erros esperados, e executar testes em vários contextos.

## Como criar testes com o unittest

O `unittest` utiliza quatro conceitos cruciais para construir a estrutura de testes: `test fixture` (ambiente de teste), `test case` (casos de teste), `test suite` (conjuntos de teste) e `test runner` (executor de teste).

- `Test fixture` - refere-se a funções que são executadas antes e/ou depois dos testes, geralmente criando um contexto necessário para a execução dos testes ou realizando tarefas de limpeza após a conclusão dos mesmos. É comum utilizar fixtures para criar dados que serão utilizados por vários testes.

- `Test case` - representa um caso de teste específico que verifica uma resposta particular para uma determinada execução de uma função ou fluxo.

- `Test suite` - consiste em coleções de casos de teste, podendo incluir outras suites de teste ou uma combinação de ambas. As suites são utilizadas para agrupar testes que devem ser executados em conjunto ou que possuem uma relação lógica entre si.

- `Test runner` - é um componente responsável por orquestrar a execução dos testes e fornecer os resultados ao usuário. O executor pode utilizar uma interface gráfica, uma interface textual ou retornar um valor especial para indicar os resultados da execução dos testes.

Vamos a um exemplo, digamos que nós temos uma função básica de divisão, passamos 2 números como argumentos para essa função e ela divide o primeiro pelo segundo:

> divisao.py

Copiar

```python
def divide(a, b):
    return a / b
```

Vamos testar a funcionalidade dessa aplicação a partir no `unittest`:

> test_divisao.py

Copiar

```python
import unittest

from divisao import divide


class TestOperations(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(5, 2), 2.5)


if __name__ == '__main__':
    unittest.main()
```

Primeiramente importamos o modulo `unittest` e, em seguida, importamos a função `divide` do módulo `divisao`. Em seguida, criamos a classe `TestOperations` (que poderia ter qualquer nome) que herda da classe `unittest.TestCase`. Essa herança permite que a classe `TestOperations` tenha acesso a todos os métodos e propriedades fornecidos pelo `unittest.TestCase`.

Dentro da classe `TestOperations`, definimos o método `test_divide`, que recebe o parâmetro `self`. Esse parâmetro permite o acesso aos métodos de asserção fornecidos pelo `unittest` por meio da herança de classe. Nesse caso, utilizamos o método `assertEqual`, que verifica se o primeiro parâmetro (`divide(5, 2)`) é igual ao segundo parâmetro (`2.5`), indicando assim se a função `divide(5, 2)` retorna o resultado esperado.

Para executar esse teste, basta rodar o seguinte comando:

Copiar

```bash
python3 -m unittest test_divisao.py
```

Saída esperada:

|![teste divide sem detalhes sucesso](https://content-assets.betrybe.com/prod/7d17a303-4111-4f9c-a460-1f42bd0054fd-teste%20divide%20sem%20detalhes%20sucesso.png)|
|---|
|Teste sem detalhes|

Você pode rodar os testes com mais detalhes passando a flag `-v`:

Copiar

```bash
python3 -m unittest -v test_divisao.py
```

Saída esperada:

|![teste divide com detalhes sucesso](https://content-assets.betrybe.com/prod/7d17a303-4111-4f9c-a460-1f42bd0054fd-teste%20divide%20com%20detalhes%20sucesso.png)|
|---|
|Teste com detalhes|

Existem outras assertions que podemos utilizar nos nossos testes, dentre elas existe a `assertRaises()` que espera que uma exceção seja lançada.

> test_divisao.py

Copiar

```python
# ...
    # def test_divide(self):
    #     self.assertEqual(divide(5, 2), 2.5)

    def test_divide_by_0(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
# ...
```

Copiar

```bash
python3 -m unittest -v test_divisao.py
```

Saída esperada:

|![teste divide com 0](https://content-assets.betrybe.com/prod/7d17a303-4111-4f9c-a460-1f42bd0054fd-teste%20divide%20com%200.png)|
|---|
|Teste divisão por 0 com detalhes|

Quando tentamos dividir um número por 0, o Python lança a exceção `ZeroDivisionError`, usando o `assertRaises` garantimos que o lançamento de uma exceção será testado da forma correta.

Como podemos ver, nossos testes funcionaram da forma certa, mas o que acontece se algum caso teste der errado? Vamos alterar o resultado esperado de um dos nossos testes para ver o que acontece:

> test_divisao.py

Copiar

```python
# ...
    # def test_divide(self):
        self.assertEqual(divide(5, 2), 2.4)
# ...
```

Copiar

```bash
python3 -m unittest -v test_divisao.py
```

Saída esperada:

|![teste divide com detalhes falha](https://content-assets.betrybe.com/prod/7d17a303-4111-4f9c-a460-1f42bd0054fd-teste%20divide%20com%20detalhes%20falha.png)|
|---|
|Teste de falha com detalhes|

Na execução do teste `test_divide`, ocorre um `AssertionError`. No entanto, esse erro não impede a execução do teste `test_divide_by_0`. Os erros em um caso de teste não interferem nos outros casos de teste. Em um cenário de testes, quando um teste falha e lança uma exceção, não é necessário tratá-la com `try/except`. Em vez disso, o erro deve ser corrigido na implementação do teste ou no código sendo testado. No nosso caso, o teste em si está com um problema, não o código sendo testado. Voltando o resultado esperado para `2.5` o teste deve funcionar da forma esperada.

## Testando Flask com unittest

Agora que você já sabe os fundamentos de testes com o `unittest`, vamos aplicar esse conhecimento em uma aplicação Flask. Para isso, vamos utilizar uma aplicação de exemplo que está disponível no seguinte repositório: [tryber/python-conteudo-flask-project-manager](https://github.com/tryber/python-conteudo-flask-project-manager). Faça o clone desse repositório e siga as instruções no `README.md` para deixar a aplicação funcional!

A aplicação deste repositório mostra tarefas de alguns projetos, atualmente a aplicação só mostra as tarefas e projetos já cadastrados no nosso banco de dados. Sinta-se a vontade para criar novas features e usar os conhecimentos de hoje para testá-las! 😉

Nós vamos utilizar o `unittest` para testar o retorno da nossa requisição, ou seja, vamos testar o que está sendo renderizado no _front-end_.

Vamos começar pela tela inicial, a tela `home`, que pode ser acessada pelas rotas `/` e `/projects`, vamos começar fazendo a preparação para os testes. Vamos criar um arquivo chamado `test_home_unittest.py` e adicionar o seguinte código a ele:

Copiar

```bash
mkdir src/tests && touch src/tests/test_home_unittest.py
```

> src/tests/test_home_unittest.py

Copiar

```python
import unittest
from app import app


class TestHome(unittest.TestCase):
    def setUp(self):
        test_app = app.test_client()
        self.response = test_app.get('/')
```

No código acima definimos a classe `TestHome`, que herda da classe `unittest.TestCase`, como vimos anteriormente.

Dentro da classe `TestHome`, há um método chamado `setUp()`. Esse método é executado antes de cada caso de teste e é usado para configurar o ambiente de teste. Dentro do método `setUp()`, criamos uma instância de `app.test_client()`, essa instância nos permite simular requisições à aplicação. Em seguida, fazemos uma solicitação `GET` à rota principal (`/`) da aplicação através da instância de `app.test_client()`, armazenando a resposta retornada em `self.response`. Essa linha simula o acesso à página inicial da aplicação e captura a resposta retornada pelo servidor.

Vamos criar nosso primeiro teste e verificar o status da resposta da nossa requisição:

> src/tests/test_home_unittest.py

Copiar

```python
# ...
    # def setUp(self):
    #     test_app = app.test_client()
    #     self.response = test_app.get('/')

    def test_status_response(self):
        self.assertEqual(self.response.status_code, 200)
```

Execute os testes:

Copiar

```bash
docker compose exec flask-api python3 -m unittest -v tests/test_home_unittest.py -b
```

Saída esperada:

|![Test status response](https://content-assets.betrybe.com/prod/997505fc-d4ce-46fc-a3c5-ed9a1cb59193-Test%20status%20response.png)|
|---|
|Test status response|

Vamos verificar se foram criados containers para cada um dos nossos 3 projetos, para isso vamos criar um diretório chamado `mocks` e um arquivo chamado `home.py`:

Copiar

```bash
mkdir src/tests/mocks && touch src/tests/mocks/home.py
```

> src/tests/mocks/home.py

Copiar

```python
project_cards = '<section class="project-home">'
```

> src/tests/test_home_unittest.py

Copiar

```python
# import unittest
# from app import app
from tests.mocks.home import project_cards
# ...
    # def test_status_response(self):
    #     self.assertEqual(self.response.status_code, 200)

    def test_quantity_of_projects(self):
        self.assertEqual(self.response.text.count(project_cards), 3)
```

Execute os testes:

Copiar

```bash
docker compose exec flask-api python3 -m unittest -v tests/test_home_unittest.py -b
```

Saída esperada:

|![Test quantity of projects](https://content-assets.betrybe.com/prod/997505fc-d4ce-46fc-a3c5-ed9a1cb59193-Test%20quantity%20of%20projects.png)|
|---|
|Test quantity of projects|

Vamos agora testar se os títulos dos 3 projetos estão sendo renderizados, criaremos um dicionário para guardar as informações dos títulos dos 3 projetos que queremos testar:

> src/mocks/home.py

Copiar

```python
# ...

project_titles = {
    1: "<h1>Aplicação Web para Gerenciamento de Tarefas</h1>",
    2: "<h1>Aplicativo móvel para rastreamento de exercícios físicos</h1>",
    3: "<h1>Sistema de gestão de vendas online</h1>"
}
```

> src/tests/test_home_unittest.py

Copiar

```python
# ...
from tests.mocks.home import project_cards, project_titles
# ...
    # def test_status_response(self):
    #     self.assertEqual(self.response.status_code, 200)

    def test_projects_titles(self):
        self.assertTrue(project_titles[1] in self.response.text)
        self.assertTrue(project_titles[2] in self.response.text)
        self.assertTrue(project_titles[3] in self.response.text)
```

Execute os testes:

Copiar

```bash
docker compose exec flask-api python3 -m unittest -v tests/test_home_unittest.py -b
```

Saída esperada:

![Test projects titles](https://content-assets.betrybe.com/prod/997505fc-d4ce-46fc-a3c5-ed9a1cb59193-Test%20projects%20titles.png)|:–:| |Test projects titles|

Vamos testar uma rota desconhecida e qual será o seu retorno:

> src/tests/mocks/home.py

Copiar

```python
# ...

unknown_page = {
    'title': '<h1>Not Found</h1>',
    'text': '<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>'
}
```

> src/tests/test_home_unittest.py

Copiar

```python
# ...
from tests.mocks.home import project_cards, project_titles, unknown_page
# ...
    # def test_projects_titles(self):
    #     self.assertTrue(project_titles[1] in self.response.text)
    #     self.assertTrue(project_titles[2] in self.response.text)
    #     self.assertTrue(project_titles[3] in self.response.text)

    def test_unknown_route(self):
        response = app.test_client().get("/unknown")
        self.assertEqual(response.status_code, 404)
        self.assertTrue(unknown_page['title'] in response.text)
        self.assertTrue(unknown_page['text'] in response.text)
```

Execute os testes:

Copiar

```bash
docker compose exec flask-api python3 -m unittest -v tests/test_home_unittest.py -b
```

Saída esperada:

|![Test unknown route](https://content-assets.betrybe.com/prod/997505fc-d4ce-46fc-a3c5-ed9a1cb59193-Test%20unknown%20route.png)|
|---|
