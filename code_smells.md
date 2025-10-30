## Code smells

- **Long Method**: métodos grandes geralmente significam mais de uma responsabilidade em um mesmo trecho de código. Por isso, como regra geral, métodos não devem ser muito longos;

- **Large Class**: classes grandes geralmente significam mais de uma responsabilidade. Por isso, como regra geral, classes não devem ser muito grandes;

- **Duplicate Code**: uma aplicação não deve ter trechos de código duplicados;
códigos duplicados geralmente significam falta de abstração, ou seja, lógica repetida que poderia estar centralizada em uma única entidade compartilhada.

- **Dead Code**: se um código não está mais sendo utilizado, por que ainda está lá? Não devemos ter código morto na aplicação.

- **Speculative Generality**: quem nunca tentou adivinhar o futuro e tornou uma implementação mais complicada do que precisava ao generalizar um comportamento apenas por achar que vai utilizá-lo novamente no futuro? Essa aqui é extremamente comum de fazermos sem perceber!

#### Exemplos de Middle Man:

Temos uma plataforma onde a pessoa jogadora (`Player`) participa de torneios (`Tournament`) de jogos (`Game`). Nesta plataforma, temos um código cliente que precisa consultar os torneios de poker de uma pessoa jogadora.
A classe `Game`, especificamente neste exemplo onde ela não possui mais métodos ou atributos, tem pouco ou nenhum impacto sobre as regras de negócio.

```py
class Player:
    # ...

    def tournaments(self, game_id):
        """Retorna os torneios de um jogo da pessoa"""
        return Game(game_id).tournaments()


class Game:
    """Classe que só possui o método de filtrar os torneios"""
    def __init__(self, game_id):
        self.game_id = game_id

    def tournaments(self):
        return Tournament.query.filter(game_id=self.game_id).all()


class Tournament:
    """Classe contendo vários métodos e que herda de algum banco de dados"""


# Código cliente
player = Player(id=1)
print(player.tournaments(1))

```

#### Solução

Se uma classe somente delega uma ação para outra, por que deveria existir? Remova o que fica no meio!

```py
class Player:
    # ...

    def tournaments(self, game_id):
        """Retorna os torneios de um jogo da pessoa"""
        return Tournament.query.filter(game_id=game_id, user_id=self.id).all()


class Tournament:
    """Classe contendo vários métodos e que herda de algum banco de dados"""

# Código cliente
player = Player(id=1)
print(player.tournaments(1))
```

#### Data Clumps

Imagine que você tem um aplicativo que possui as funcionalidades de cadastro de pessoas e de empresas. Tanto as pessoas quanto as empresas possuem endereços.

```py
class User:
    def __init__(self, name, age, street, number, district):
        self.name = name
        self.age = age
        self.address_street = street
        self.address_number = number
        self.address_district = district

    # ...


# Em algum outro lugar do código
class Company:
    def __init__(self, name, street, number, district):
        self.name = name
        self.address_street = street
        self.address_number = number
        self.address_district = district

    # ...

```

#### Soluções
Uma possível solução para esse problema é criar uma classe somente para representar a entidade endereço:

```py
class Address:
    def __init__(self, street, number, district):
        self.street = street
        self.number = number
        self.district = district


class User:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address
```