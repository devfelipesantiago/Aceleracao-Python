## Realizando uma busca por todos os documentos

Antes de tudo, entraremos no terminal do **mongosh** e vamos nos conectar ao banco de dados **trybnb** executando o seguinte comando:

```python
use trybnb
```

Ao executar o comando acima, você receberá uma mensagem dizendo `switched to db trybnb` e o **prompt** do terminal mudará para `trybnb>`. Isso significa que o mongosh está operando a partir desse banco de dados.

Caso desejasse mudar de banco, bastaria digitar `use <nome_do_banco>` para efetivar tal ação.

A primeira pergunta que podemos realizar ao MongoDB sobre os dados do banco trybnb é: _“quais são os imóveis cadastrados no trybnb?”_. Essa pergunta é o equivalente a realizar uma busca por **todos os documentos cadastrados na coleção places**. Logo, podemos escrever o seguinte comando no mongosh:

```python
db.places.find()
```

Como resposta ao comando, será exibido todos os documentos cadastrados na coleção _places_ que é a resposta da nossa pergunta inicial. O comando anterior serve para recuperar dados de uma coleção. Formalmente, ele é composto pelos seguintes elementos:

|![Estrutura do método find](https://content-assets.betrybe.com/prod/5940df7e-37d1-4781-ad46-df2d2868e133-Estrutura%20do%20m%C3%A9todo%20find.svg)|
|---|
|Estrutura do método find|

Baseado na estrutura descrita da figura acima, podemos pesquisar por documentos cadastrados em coleções de um bancos de dados no MongoDB. Em um banco de dados relacional, o correspondente do método `db.places.find()` seria o `SELECT * FROM places`.

> **De olho na dica 👀:** Aproveite que recuperamos todos os documentos para visualizar os campos e valores existentes nos mesmos.

## Realizando a contagem de documentos

Suponha que necessitamos responder a seguinte pergunta: _“Quantos imóveis estão cadastrados no trybnb?”_. Diferente da primeira pergunta que pretendia responder **quais são** os imóveis, a pergunta atual visa responder **quantos são**. Essa pergunta é o mesmo que obter a quantidade de documentos armazenados na coleção _places_ e podemos responde-la utilizando o seguinte comando:

```python
db.places.countDocuments()
```

O método `countDocuments()` realiza a contagem de documentos de uma determinada coleção (no nosso caso, da coleção **places**). Após sua execução, será exibido o valor `12` que é a quantidade de documentos cadastrados na coleção.

## Recuperando documentos baseado em um critério

Também é possível recuperar documentos baseado em algum critério de seleção, similar à cláusula `WHERE` dos banco de dados relacionais.

Não foi comentado antes, mas o método `find()` pode receber dois parâmetros:

- Parâmetro **query**;
- Parâmetro **projection**.

Ambos os parâmetros são opcionais e, quando não informados, o método `find()` realiza a busca de todos os documentos (como mostrado anteriormente).

A Figura a seguir, exibe a estrutura do método `find()` com os parâmetros **query** e **projection**:

|![Estrutura do método find com os parâmetros query e projection](https://content-assets.betrybe.com/prod/5940df7e-37d1-4781-ad46-df2d2868e133-Estrutura%20do%20m%C3%A9todo%20find%20com%20os%20par%C3%A2metros%20query%20e%20projection.svg)|
|---|
|Estrutura do método find com os parâmetros query e projection|

> **Atenção ⚠️:** Se omitirmos os parâmetros **query** e **projection**, ex. `db.places.find()`, ou passarmos objetos vazios como parâmetros representando esses parâmetros, ex. `db.places.find({}, {})`, o resultado será o mesmo, ou seja, serão retornados todos os documentos da coleção. Vamos explorar primeiramente o parâmetro _query_ e, em seguida, o parâmetro _projection_! 👍

### Parâmetro query

Suponha que queremos saber qual imóvel tem o **_id** igual a **7** (uma pergunta a ser respondida pelo banco de dados). Podemos obter essa resposta adicionando o parâmetro _query_ ao método `find()` da seguinte forma:

```python
db.places.find({ '_id': 7 })
```

> **De olho na dica 👀:** Os espaços em branco utilizados entre as chaves para separar os elementos não são obrigatórios e possuem caráter puramente estético, ou seja, se escrevêssemos `db.places.find({'_id':7})`, seria obtido o mesmo resultado. Ao executar o comando acima, receberemos como resultado o documento cujo o campo **_id** é igual a **7**. Em um banco de dados relacional, o correspondente do método `db.places.find({ '_id': 7 })` seria o `SELECT * FROM places WHERE _id = 7`.

O parâmetro _query_ é o objeto `{ '_id': 7 }` e, neste caso, o parâmetro _projection_ foi omitido (mas poderíamos passar um objeto vazio como segundo parâmetro para representa-lo, ficando `db.places.find({ '_id': 7 }, {})`).

> **Atenção ⚠️:** O MongoDB utiliza o campo _id como identificador dos documentos, funcionando de forma similar a coluna id (chave primária) dos bancos de dados relacionais. Agora vamos supor que gostaríamos de saber quais imóveis estão localizados no Brasil, ou seja, uma nova pergunta a ser respondida pelos dados do banco **trybnb**. Existe um campo chamado **country_code** cujo valor é o código do país do imóvel. Este campo está dentro de um objeto chamado **address**, que também é um campo.

Neste caso, como existe um aninhamento de campos (o campo **country_code** é filho do campo **address**) teremos que utilizar um campo composto (em inglês também pode ser chamado de `dotNotation`) para filtrar os dados. Em outras palavras, temos que executar o seguinte comando no terminal do _mongosh_:

```python
db.places.find({ 'address.country_code': 'BR' })
```

Ao executar o comando acima, receberemos como resultado um conjunto de documentos cujo o valor de `address.country_code` é igual a `BR`. Em um banco de dados relacional seria o equivalente realizar uma consulta `SELECT` com um `JOIN`, dado que, pela terceira forma normal, **places** seria uma tabela e **address** seria outra tabela.

O grande barato, e uma das vantagens, dos bancos de dados não relacionais, é que podemos deixar os dados sobre determinada entidade do mundo real (no nosso exemplo imóveis para locação) em um mesmo documento, ou seja, não precisamos normalizar os dados como fazemos nos bancos de dados relacionais. Isso em muitos casos, facilita a escrita de consultas no banco, além de tornar a operação mais rápida!

Para finalizar, quantos imóveis temos disponíveis para locação no Brasil? Temos uma nova pergunta para ser respondida! Diferente do que vimos no início da lição, onde usamos o método `db.places.countDocuments()` para contar o total de documentos da coleção, agora queremos contar quantos documentos o método `find()` retornou após utilizar o parâmetro _query_.

Basicamente, basta escrevermos a consulta do mesmo modo que já fizemos e adicionar o método `count()` ao final, da seguinte forma:

```python
db.places.find({ 'address.country_code': 'BR' }).count()
```

Note, ao final do comando, como é feita a chamada ao método `count()`. Como resultado, será exibido o total de documentos recuperados na consulta do método `find()` que, neste caso, são **6** documentos.

### Parâmetro projection

O parâmetro _projection_ permite especificar quais campos devem ou não ser retornados em uma consulta utilizando o método `find()`.

Para deixar isso mais nítido, vamos trabalhar com a consulta que recupera o imóvel cujo o campo **_id** seja igual a **7**, ou seja:

```python
db.places.find({ '_id': 7 })
```

Ao executar o comando acima, é exibido o documento cujo o valor do campo **_id** é igual a **7**, conforme já foi visto anteriormente. Mas vamos supor que apenas queremos exibir o nome do imóvel e omitir os demais campos.

Para alcançar este objetivo, utilizaremos o parâmetro _projection_ para definir quais campos devem ser exibidos na resposta da consulta. Para isso, devemos executar o método `find()` com o seguinte conteúdo:

```python
db.places.find({ '_id': 7 }, { 'name': true })
```

Como resposta, será exibido o campo **_id** e o campo **name** (nome do imóvel)!

A _projection_ é um objeto que pode conter um ou mais campos com valor `true` (ou `false` como veremos mais adiante), onde apenas os campos especificados na _projection_ como `true` serão exibidos na resposta da consulta.

Agora vamos supor que queremos, além de exibir o nome do imóvel, exibir o endereço do imóvel cujo o campo **_id** seja igual a **7**. Sabemos que existe uma campo **address** que contém os dados do endereço do imóvel. Logo, o comando para atender o esperado seria:

```python
db.places.find({ '_id': 7 }, { 'name': true, 'address': true })
```

Nesse caso, o retorno conterá os campos **_id**, **name** e **address**. Como o valor do campo _address_ é um objeto, os campos internos do objeto _address_ serão exibidos também.

> **De olho na dica 👀**: Quando a projeção contêm campos cujo os valores são iguais a `true`, temos uma **projeção de inclusão**, ou seja, na resposta são incluídos os campos definidos na projeção e as demais são ignoradas. Podemos também, utilizando o parâmetro _projection_, realizar o inverso, ou seja, ao pesquisar um documento, quais campos deseja-se omitir. Para isso, na _projection_ atribuímos o valor **false** ao campo que queremos omitir.

Por exemplo, se escrevermos o seguinte comando no _mongosh_:

```python
db.places.find({ '_id': 7 }, { 'address': false, 'host': false })
```

Será retornado o documento cujo o campo **_id** é igual a **7** mas, nessa resposta, não teremos os campos **address** e **host** na resposta.

> **De olho na dica 👀**: Quando a projeção contêm campos cujos valores são iguais a `false`, temos uma **projeção de exclusão**, ou seja, na resposta são exibidos todos os campos exceto os campos definidos na projeção.

## Ordenando uma resposta

Você deve ter notado que ao fazer uma consulta no banco de dados, os documentos não são recuperados segundo a ordem do atributo **_id**. Caso você deseje que esses dados retornem ordenados baseados no valor de uma chave, podemos utilizar o método `sort()`. Observe o exemplo abaixo:

```python
db.places.find().sort({'_id': 1})
```

Se executarmos o exemplo acima, será retornado todos os documentos da coleção _places_ ordenados pela chave **_id** de forma **crescente**, pois o valor **1** indica que a ordenação se dará dessa forma. Para realizar essa ordenação de forma decrescente, basta mudarmos o valor **1** para **-1**, ou seja:

```python
db.places.find().sort({'_id': -1})
```

Assim os documentos serão ordenados baseado no valor da chave **_id** mas seguindo uma ordem decrescente.

## Conclusão

Recapitulando, estudamos como realizar pesquisas em uma coleção de documentos através do método `find()`, e também como utilizar os parâmetros _query_ (para adicionar critérios na recuperação de documentos baseados em campos simples e compostos) e _projection_ (para selecionar os campos que deverão ser recuperados ou omitidos nos documentos). Também estudamos como contar todos os documentos de uma coleção utilizando o método `countDocuments()` e a contar a quantidade de documentos recuperados de uma pesquisa utilizando o método `count()` em conjunto com o método `find()`. Por último, estudamos como ordenar os documentos, de forma crescente ou decrescente, a partir do valor de uma chave, com o método `sort()`.

# Operadores de Comparação

Quando realizamos consultas em um banco de dados é necessário, em alguns momentos, estabelecer critérios de consulta que retornem documentos baseados em expressões lógicas utilizando **operadores de comparação** em conjunto com **operadores lógicos** (estes serão abordados no próximo conteúdo).

Por exemplo, utilizando a base de dados **trybnb** suponha que queremos saber quais imóveis no Brasil possuem mais do que três quartos. Ainda quais imóveis oferecem espaço para acomodar três pessoas ou mais? Ou até, quais imóveis no Brasil oferecem três quartos ou que consigam acomodar seis pessoas?

Essas são perguntas corriqueiras nesse tipo de aplicação e o _MongoDB_ oferece suporte para obtermos as respostas a essas perguntas (ou consultas). 👍

## Operadores de comparação

O _MongoDB_ fornece vários operadores de comparação para serem utilizados em consultas ao banco de dados, mas iremos estudar os seguintes operadores de comparação:

- `$eq`: Específica uma condição de **igualdade** (_equal_). O operador `$eq` realiza a correspondência de documentos em que o valor de uma chave **é igual** ao valor especificado.

Sintaxe do operador `$eq`:

```python
{<chave> { $eq: <valor> }}
```

- `$ne`: Especifica uma condição de **não igualdade** (_not equal_). O operador `$ne` realiza a correspondência de documentos em que o valor de uma chave **não é igual** ao valor especificado.

Sintaxe do operador `$ne`:

```python
{<chave> { $ne: <valor> }}
```

- `$gt`: Especifica uma condição de **maior que** (_greater than_). O operador `$gt` realiza a correspondência de documentos em que o valor de uma chave **maior que** o valor especificado.

```python
{<chave> { $gt: <valor> }}
```

- `$gte`: Especifica uma condição de **maior ou igual** (_greater than or equal_). O operador `$gte` realiza a correspondência de documentos em que o valor de uma chave **maior ou igual** ao valor especificado.

```python
{<chave> { $gte: <valor> }}
```

- `$lt`: Especifica uma condição de **menor que** (_less than_). O operador `$lt` realiza a correspondência de documentos em que o valor de uma chave **menor que** o valor especificado.

```python
{<chave> { $lt: <valor> }}
```

- `$lte`: Especifica uma condição de **menor ou igual** (_less than or equal_). O operador `$lte` realiza a correspondência de documentos em que o valor de uma chave **menor ou igual** ao valor especificado.

```python
{<chave> { $lte: <valor> }}
```

No geral, conforme pode ser visto na própria [documentação](https://www.mongodb.com/docs/v6.0/reference/operator/query-comparison/) do _MongoDB_, a estrutura dos operadores de comparação seguem uma estrutura geral ilustrada na figura abaixo:

|![Estrutura do operador de comparação](https://content-assets.betrybe.com/prod/969ef140-78d1-4f6f-8261-395e7cfc692c-Estrutura%20do%20operador%20de%20compara%C3%A7%C3%A3o.svg)|
|---|
|Estrutura do operador de comparação

# Inserindo dados

Até aqui estudamos como recuperar dados, agora vamos dar um passo adiante e entender como inserir dados no **MongoDB**. Existem dois métodos para realizar a inserção de dados:

- Método `insertOne()`: Para inserir apenas um documento;
- Método `insertMany()`: Para inserir um `array` de documentos.

> **De olho na dica 👀:** Toda e qualquer manipulação de dados no _MongoDB_ se dá através de documentos, ou seja, na inserção serão inseridos documentos assim como em uma consulta recuperamos documentos. A diferença entre os métodos de inserção está na quantidade de documentos que podem ser inseridos por operação. Enquanto que o método `insertOne()` realiza a inserção de um único documento, o método `insertMany()` realiza a inserção de vários documentos. Independente do método utilizado, os documentos podem ter quantas chaves quanto forem necessárias.

Lembre-se que o **MongoDB**, assim como qualquer banco de dados **NoSQL**, não possuem um **schema**. O que isso quer dizer? 🤔

Isso significa que o documento não possui uma estrutura rígida que deve ser seguida durante a inserção ou uma atualização de documentos. O legal disso tudo, é que os documentos não precisam ter as mesmas chaves, ou seja, alguns documentos podem possuir chaves a mais, outros podem possuir chaves a menos, ou até mesmos a mesma quantidade de chaves mas com nomes diferentes!

Lembra da nossa discussão inicial sobre como representar as diferentes formas de endereçamento de imóveis no banco de dados? Essa flexibilidade de possuir documentos com formas distintas é que nos permitirá cadastrar imóveis de formas diferentes sem ter que atualizar todos os documentos de uma única vez!

Essa atualização, se for algo estritamente necessário, pode ser realizada aos poucos, conforme os documentos são acessados e, nesse momento, verifica-se a existência ou não das novas chaves, por exemplo, e, no caso de ser necessário adicionar uma nova chave, é feito apenas naquele documento. Os demais documentos são atualizados conforme forem sendo acessados.

_E como se faz a validação da existência ou não de uma chave?_ 🤔

Essa responsabilidade passa a ser da aplicação. Esse é o custo que deve ser pago pela flexibilidade oferecida pelos bancos de dados **NoSQL**.

# Operadores de Consulta em Arrays

Vamos imaginar a seguinte situação: Uma pessoa chegou em uma cidade e vai ficar por la, apenas dois meses. Nestes dois meses, esta pessoa deseja economizar o máximo possível e um dos gastos que pretende cortar, é alimentação! Para isso, comprar e preparar sua própria comida, é prioridade.

Com o cenário descrito acima, é desejável filtrar casas que já incluem fogão e geladeira no contrato, correto!? Mas como podemos fazer isso com que aprendemos até agora? Eu diria que é bem difícil 🥺 Utilizando operadores lógicos/comparação, não é suficiente para pesquisar fogão (_Stove_) e geladeira (_Refrigerator_), dentro de `amenities`!!! Pois `amenities` é um _array_ de opções…Para isso, o _MongoDB_ nos oferece um operador, que verifica a presença de valores dentro de um _array_, este operador é o `$all`!

## $all

Vamos solucionar o problema da pesquisa dentro de _arrays_, com esse novo operador que estamos vendo. Utilizamos `$all` sempre que é preciso passar mais de um valor para comparação em um atributo do tipo _array_, e a ordem desta lista não importa.

Observe a estrutura do operador `$all`:

|![Estrutura do operador $all](https://content-assets.betrybe.com/prod/cc6827b7-bd75-49ec-94b9-8fbc6f1181ee-Estrutura%20do%20operador%20$all.svg)|
|---|
|Estrutura do operador $all|

Podemos responder a pergunta anterior utilizando o operador `$all` da seguinte maneira:

```python
  db.places.find({ amenities: { $all: ["Stove", "Refrigerator"] } })
```

> 🚦Atenção, com o comando abaixo, o comportamento é diferente do que usar o operador `$all`!!!

```python
db.places.find({ amenities: ["Garagem", "jacuzzi", "Armários", "piscina"] })
```

- A _query_ acima retornará somente os documentos em que o _array_ `amenities` seja **exatamente igual ao passado** como parâmetro no filtro, ou seja, contenha apenas esses elementos e na mesma ordem!
- Já a _query_ utilizando o operador `$all`, analisará o mesmo _array_, **independentemente** da existência de outros valores ou da ordem em que os elementos estejam.

## Pymongo

```bash
python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install pymongo
```

Após a instalação vamos ver como podemos realizar a escrita e leitura neste banco de dados. O primeiro passo é criar uma conexão com o banco de dados e isto pode ser feito da seguinte maneira:

> ⚠️ Lembre-se que o MongoDB deve estar preparado para ser acessado do “outro lado” dessa operação!.

```python
from pymongo import MongoClient

# Por padrão o host é localhost e porta 27017
# Estes valores podem ser modificados passando uma URI
# client = MongoClient("mongodb://localhost:27017/")
client = MongoClient()
```

Em posse da conexão podemos acessar um banco de dados e posteriormente uma coleção:

```python
from pymongo import MongoClient

client = MongoClient()
# o banco de dados catalogue será criado se não existir
db = client.catalogue
# a coleção books será criada se não existir
students = db.books
client.close()  # fecha a conexão com o banco de dados
```

Para adicionarmos documentos à nossa coleção utilizamos o método `insert_one`:

```python
from pymongo import MongoClient

client = MongoClient()
db = client.catalogue
book = {
    "title": "A Light in the Attic",
}
document_id = db.books.insert_one(book).inserted_id
print(document_id)
client.close()  # fecha a conexão com o banco de dados
```

Quando um documento é inserido, um `_id` único é gerado e retornado. Também podemos fazer inserção de múltiplos documentos de uma vez da seguinte forma:

```python
from pymongo import MongoClient

client = MongoClient()
db = client.catalogue
documents = [
    {
        "title": "A Light in the Attic",
    },
    {
        "title": "Tipping the Velvet",
    },
    {
        "title": "Soumission",
    },
]
db.books.insert_many(documents)
client.close()  # fecha a conexão com o banco de dados
```

Buscas podem ser feitas utilizando os métodos `find` ou `find_one`:

```python
from pymongo import MongoClient

client = MongoClient()
db = client.catalogue
# busca um documento da coleção, sem filtros
print(db.books.find_one())
# busca utilizando filtros
for book in db.books.find({"title": {"$regex": "t"}}):
    print(book["title"])
client.close()  # fecha a conexão com o banco de dados
```

O nosso cliente é um gerenciador de contexto (_with_), logo podemos utilizá-lo como tal, evitando problemas com o fechamento da conexão com o banco de dados:

```python
from pymongo import MongoClient


with MongoClient() as client:
    db = client.catalogue
    for book in db.books.find({"title": {"$regex": "t"}}):
        print(book["title"])
```