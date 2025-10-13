# Resumo

- **Anotação de tipo | Dica de tipo | Type annotation | Type hint**: forma explícita de tipar valores em Python. Usando uma ferramenta externa conseguimos usá-los para ter tipagem estática em Python

- **Atributo**: características que definem uma classe. A classe os define e os objetos dão seus valores.
Checagem de tipos
  - ***Estática***: define o tipo explicitamente, permitindo sua checagem em tempo de execução
  - ***Dinâmica***: ‘descobre-se’ o tipo durante a execução do código somente, sem necessidade de se definir nada explicitamente
  - ***Estrutural***: infere-se o tipo de um valor baseado nos comportamentos que ele tem
  - ***Nominal***: infere-se o tipo de um valor com base no nome do mesmo, ainda que outros tipos tenham comportamentos 100% idênticos
- **Classe**: entidade, que pode se basear em algo real ou num conceito abstrato, que possui atributos e comportamentos no seu código
Inferência de tipo
- **Instância**: se a classe é o molde, a instância é a coisa que o molde faz. Uma classe pode gerar N instâncias, cada uma com seus valores em atributos.
- **Método**: comportamento de uma classe - funções dela, que podem acessar seus atributos
- **mypy**: ferramenta que permite tipagem estática em Python
- **Objeto**: instância de uma classe. Se Car é a classe,my_car é o objeto.
- **Self**: entidade que permite, no Python, uma classe acessar os valores dos atributos de quem a invocou, como o this do JavaScript.
- **Método construtor**: invocado sempre que se cria uma instância, ele coloca valores em atributos.
- **Classes como tipos**: se a instância de uma classe é esperada como valor, ela pode ser usada para fazer tipagem estática.
