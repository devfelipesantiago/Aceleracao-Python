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
