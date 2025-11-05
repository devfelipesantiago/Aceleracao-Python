# Primeiro projeto Django

Depois de entender o que é o Django, as bases de seu design e suas principais vantagens, é hora de adicionarmos um pouco de prática aos seus aprendizados!

No exemplo da aula de hoje, desenvolveremos uma aplicação simples de um e-commerce, no qual será possível cadastrar e consultar produtos em estoque. Ainda não trabalharemos a criação de APIs (não se preocupe, essa hora vai chegar muito em breve! 😉). Por ora, apenas exploraremos os recursos e configurações básicas do Django, mas você já pode vislumbrar o mar de possibilidades que este _framework_ oferece!

## Preparando o ambiente

Antes de começarmos a desenvolver, precisamos preparar o ambiente de desenvolvimento. A primeira coisa a se fazer é verificar a versão do Python que estamos utilizando. Você pode fazer isso com o comando:

```bash
python3 --version
```

Caso a versão seja inferior a 3.10, você precisará atualizar o Python. Para isso, você pode utilizar o **Pyenv**, basta seguir nosso [tutorial do Guia de configuração de ambiente](https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/f04cdb21-382e-4588-8950-3b1a29afd2dd/section/aa76abc8-b842-40d9-b5cc-baa960952129/lesson/0fe67ea0-1046-4b55-a37c-44afcfa9ed0a). Isso é necessário porque mais à frente utilizaremos uma biblioteca que **não funciona bem com a versão 3.9 ou inferiores** do Python.

Para começar, vamos criar um novo diretório para o nosso projeto e entrar nele:

```bash
mkdir ecommerce && cd ecommerce
```

Em seguida, vamos criar um ambiente virtual para o nosso projeto e ativá-lo:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Agora, vamos instalar o Django:

```bash
pip install django
```

E, finalmente, vamos iniciar um projeto chamado **ecommerce**, no diretório atual:

```bash
django-admin startproject ecommerce .
```

Simples assim e nosso primeiro projeto foi criado! 🎉

Logo, logo veremos melhor a estrutura de arquivos que o Django criou para nós, mas agora, vamos ver como é simples executá-lo?

## Executando o projeto

Para executar o projeto, basta executar o comando:

```bash
python3 manage.py runserver
```

> Num instante falamos da mensagem em vermelho que apareceu pra você! 😉

Você deve ter notado que um arquivo de banco de dados `db.sqlite3` foi criado _automagicamente_ no diretório do projeto. Geralmente, precisamos configurar uma conexão com o banco de dados em nossas aplicações, mas isso é um pouco diferente no Django.

Lembra que falamos que um dos diferenciais deste framework é a variedade de recursos prontos para uso? Aqui está um exemplo prático disso, pois o Django já vem com um banco de dados SQLite configurado por padrão, para facilitar o desenvolvimento.

Mais adiante, veremos como configurar um banco de dados diferente, mas, por ora, vamos seguir com o SQLite mesmo.

Se você acessar o endereço [http://localhost:8000](http://localhost:8000/) no seu navegador, você verá essa página:

|![Página inicial do Django](https://content-assets.betrybe.com/prod/f2a5bbcb-65ab-4058-b8bc-1687e1167533-P%C3%A1gina%20inicial%20do%20Django.png)|
|---|
|Página inicial do Django|

Bem mais legal que uma simples página em branco, não é mesmo? 😎

Ao executar o projeto, algo que pode ter chamado sua atenção é a mensagem em vermelho no terminal:

```bash
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
# Em português: Você tem 18 migrations não aplicadas. Seu projeto pode não funcionar corretamente até que você aplique as migrations para os apps: admin, auth, contenttypes, sessions.
```

Apesar de a mensagem estar em vermelho, ela não representa um erro, apenas um aviso (_warning_). Ele acontece porque o Django possui algumas _migrations_ internas que ainda não foram aplicadas ao banco de dados. Para aplicá-las, **abra um novo terminal**, ative o ambiente virtual e execute o comando:

```bash
python3 manage.py migrate
```

|![Terminal após rodar migrations](https://content-assets.betrybe.com/prod/f2a5bbcb-65ab-4058-b8bc-1687e1167533-Terminal%20ap%C3%B3s%20rodar%20migrations.png)|
|---|
|Terminal após rodar migrations|

Se dermos uma olhada no banco de dados agora, veremos que ele foi criado e que o Django criou algumas tabelas internas para nós.

> Como o banco de dados padrão é o SQLite, a forma mais fácil de ver as tabelas é no próprio VS Code utilizando a extensão `SQLite viewer`, mas como substituiremos este banco de dados daqui a pouco, fique a vontade para apenas observar a imagem abaixo, que mostra como é a visualização com a extensão:

|![Tabelas do banco de dados SQLite](https://content-assets.betrybe.com/prod/f2a5bbcb-65ab-4058-b8bc-1687e1167533-Tabelas%20do%20banco%20de%20dados%20SQLite.png)|
|---|
|Tabelas do banco de dados SQLite|

## Entendendo a estrutura do projeto

Já demos início a um projeto, o executamos, porém, agora surge a pergunta: o que são todos aqueles arquivos? Vamos agora aprofundar nosso entendimento sobre esse assunto!

Até agora, a estrutura de diretórios do projeto é basicamente a seguinte:

```bash
ecommerce
│   ├── .venv
│   ├── ecommerce
│      ├── __pycache__
│      ├── __init__.py
│      ├── asgi.py
│      ├── settings.py
│      ├── urls.py
│      └── wsgi.py
└── db.sqlite3
└── manage.py
```

Passando rapidamente por cada um dos arquivos dentro do diretório `ecommerce`, que é o diretório do projeto em si, temos os arquivos:

- `manage.py`: é o arquivo usado internamente quando **executamos comandos do Django** - como o `runserver` que executamos anteriormente.
- `__init__.py`: arquivo que indica que o diretório é um pacote Python - já utilizamos este arquivo lá na seção 1, lembra? 😉
- `asgi.py`: arquivo de configuração do ASGI (Asynchronous Server Gateway Interface), que é o protocolo usado pelo Django para comunicação entre servidores web e aplicações web para lidar com solicitações assíncronas e em tempo real.
- `settings.py`: arquivo de **configuração do projeto**, que contém todas as configurações do Django para o projeto. É aqui que configuramos, por exemplo, o banco de dados que será usado, o idioma padrão da aplicação, etc. Veremos este arquivo com mais atenção daqui a pouco. 🤓
- `urls.py`: arquivo de configuração de **rotas do projeto**. Vamos explorar este arquivo com mais detalhes em breve. 🤩
- `wsgi.py`: arquivo de configuração do WSGI (Web Server Gateway Interface), que é o protocolo usado pelo Django para comunicação entre servidores web e aplicações web para lidar com solicitações HTTP.
- `__pycache__`: diretório que contém arquivos gerados automaticamente pelo Python para otimizar o carregamento de módulos.

Dois arquivos valem uma atenção especial: `settings.py` e `urls.py`. Bora dar uma olhada neles?

### Arquivo `settings.py`

Este é o arquivo que reúne as principais configurações do projeto, com várias dessas configurações já definidas com valores-padrão. Vamos entender melhor algumas dessas _configs_?

- `SECRET_KEY` é uma chave de segurança que o Django utiliza para criptografar dados sensíveis, como senhas de pessoas usuárias, por exemplo. Ela já vem com um valor por padrão, mas explicitamente dada como insegura e por isso, é recomendável substitui-la por uma chave personalizada forte, especialmente em ambientes de produção.
- `DEBUG` é um booleano que indica se o modo de depuração (_debug_) está ativado ou não. Durante o desenvolvimento, ter esse modo ativado é muito útil para ajudar a identificar e corrigir bugs, o valor default (padrão) dessa variável é true justamente por isso. Contudo, ele pode trazer algumas vulnerabilidades à segurança, como, por exemplo, mostrar informações sensíveis do projeto - algo ruim se mostrado para uma pessoa usuária. Por isso, é importante que ele esteja desativado quando o projeto estiver em produção.
- `ALLOWED_HOSTS` é uma lista de nomes de domínios, subdomínios ou endereços IP que o Django permite que acessem o projeto. Você pode usar o valor `'*'`, caso queira dar acesso a todos, ou definir uma lista com os grupos que terão acesso ao projeto, por exemplo, `['exemplo.com', 'subdomínio.exemplo.com', '192.168.1.1']`.
- `INSTALLED_APPS` é uma lista de apps que serão acoplados no projeto Django. Alguns já vêm instalados por padrão, mas os _apps_ criados por você para o projeto podem compor essa variável também. Veremos como fazer isso em breve! 🤩
- `MIDDLEWARE` é uma lista de middlewares que o Django utiliza para fazer algumas coisas como, por exemplo, o middleware de autenticação de pessoa usuária. Sua lógica é similar a dos Middlewares do Express, mas entraremos em detalhes sobre eles apenas na próxima seção.
- `TEMPLATES` é uma lista de diretórios em que o Django irá procurar por templates HTML.
- `DATABASES` é a configuração de banco de dados do projeto. Como o Django já vem com o SQLite instalado por padrão, ele já vem com a configuração do **SQLite**, mas podemos trocar por outros.
- `LANGUAGE_CODE` é a configuração de idioma padrão do projeto. Por padrão, ele vem com o inglês, mas podemos alterar para qualquer outro.

> **De olho na dica 👀:** você pode alterar a linguagem padrão do projeto Django para português apenas, alterando a variável `language_code` para `pt-br`. Experimente fazer isso e atualizar a página para ver a tela inicial está traduzida! 🤩

### Arquivo `urls.py`

Já acessamos a rota raiz do projeto quando rodamos o servidor e acessamos a URL `localhost:8000`. Apesar de não termos definido nenhuma rota até aquele momento, a URL raiz já traz por padrão um retorno visual: uma página com o foguetinho informando que deu tudo certo com a instalação.

Como dito anteriormente, este arquivo reúne as rotas do projeto, com alguns valores já definidos por padrão. Vamos entender melhor como uma rota é definida?

A primeira coisa que temos é a função `path`, que define uma rota. Como parâmetro ela recebe a URL que será acessada e a função que será executada quando a URL for acessada.

Uma surpresa é que já temos uma rota definida no arquivo, a `admin/`, que é a interface administrativa que o Django fornece para o projeto. Vamos explorar ela com mais detalhes em breve. 😎

## Usando outro banco de dados

Você já viu que, por padrão, um projeto Django vem com um banco de dados SQLite. Mas, e se você quiser usar outro banco de dados, como você faz? É exatamente isso que vamos ver agora!

Você pode iniciar apagando o arquivo `db.sqlite3` do seu projeto, pois ele não será mais utilizado. Faremos as alterações no projeto para que ele use como banco de dados nosso conhecido MySQL, via Docker.

Para isso, o primeiro passo é alterar a variável `DATABASE`, no arquivo `settings.py`, para que ela tenha as configurações de acesso ao banco necessárias. De acordo com a [documentação](https://docs.djangoproject.com/en/4.2/ref/settings/#engine), a variável deve ficar assim:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce_database',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        }
}
```

Em seguida, criaremos um arquivo que conterá o script SQL que criará o banco de dados `ecommerce_database`. Ele ficará dentro do diretório `./database`:

```bash
mkdir database && cd database
touch 01_create_database.sql
```

Por ora, o banco de dados não terá nenhuma tabela, portanto, o script de criação do banco de dados `ecommerce_database` deve ficar assim:

```sql
CREATE DATABASE IF NOT EXISTS ecommerce_database;

USE ecommerce_database;
```

Com isso feito, é hora de criar um arquivo `Dockerfile` na raiz do projeto (no mesmo nível do arquivo `manage.py`), com o seguinte conteúdo:

```yaml
FROM mysql:8.0.32

ENV MYSQL_ROOT_PASSWORD password

# Copia o script SQL que acabamos de criar para um determinado diretório no container
COPY ./database/01_create_database.sql /docker-entrypoint-initdb.d/data.sql01
```

Para _buildar_ a imagem, basta rodar o comando dentro da pasta do projeto que contém o arquivo Dockerfile.

```bash
docker build -t ecommerce-db .
```

Para executar o container e o script de criação do banco copiado no Dockerfile, é preciso passar algumas as variáveis de acesso definidas na variável `DATABASES`, do arquivo `settings.py`, para o container. Para isso, vamos usar o comando:

```bash
docker run -d -p 3306:3306 --name=ecommerce-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=ecommerce_database ecommerce-db
```

Neste momento, você já pode acessar o banco de dados pelo _Workbench_ e verificar se ele foi criado corretamente.

Mas ainda não acabou! Lembra das _migrations_ iniciais que geraram o famigerado aviso em vermelho no início do projeto? Elas ainda não foram executadas neste banco de dados. Para isso, é preciso executar o comando `migrate` do Django:

```bash
python3 manage.py migrate
```

Você provavelmente se deparou com um erro agora, né? **Don’t panic!** O erro acontece porque o Django não consegue se comunicar com o banco de dados, pois não tem o pacote `mysqlclient` instalado. Resolver isso é bem simples, basta instalar o pacote exigido:

```bash
pip install mysqlclient
```

Caso ocorra algum erro no comando anterior, pode ser porque um pacote adicional chamado `pkg-config` não esteja instalado. Nesse caso, tente seguir todos os passos sugeridos pela [documentação oficial](https://github.com/PyMySQL/mysqlclient#install) do `mysqlclient` para a instalação do pacote. Para facilitar, o seguinte comando funciona para a maioria dos sistemas Linux:

```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
```

Por fim, basta rodar novamente as _migrations_ e ver que agora tudo está funcionando corretamente! 🤩

## Criando a primeira aplicação

No Django, temos o conceito de **projeto** e de **aplicação (ou app)**. Um projeto pode ser descrito como a estrutura geral que abrange todas as configurações e aplicações relacionadas a ele. Já a aplicação é um componente reutilizável que tem uma função específica dentro do projeto.

De forma resumida, todas as aplicações (componentes reutilizáveis tipo os de React), que estão registradas na variável `INSTALLED_APPS`, do arquivo `settings.py` fazem parte do projeto.

Por exemplo, podemos ter um projeto de uma loja virtual que tenha uma aplicação de autenticação, uma aplicação de cadastro de produtos, uma aplicação de cadastro de clientes, etc.

Já criamos nosso projeto, agora chegou a hora de criar nossa primeira aplicação!

Vamos começar voltando no arquivo `settings.py` e adicionando o app que iremos criar à lista preexistente:

```diff
# ecommerce/ecommerce/settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
+    "products",
]
```

Com isso feito, é hora de efetivamente criar o _app_. O comando é similar ao utilizado para criar o projeto, mas agora vamos utilizar `startapp` em vez de `startproject`:

```bash
django-admin startapp products
```

Observe que um diretório com o nome da nossa aplicação (`products`) foi criado e a estrutura de diretórios agora passa a ser:

```bash
ecommerce
│   ├── .venv
│       └── ...
│   ├── database
│       └── ...
│   ├── ecommerce
│       └── ...
│   ├── products
│       └── ...
├──  Dockerfile
├──  manage.py
```

No diretório da aplicação **products** já existem alguns arquivos. O primeiro deles que iremos ajustar é o `models.py`, que é onde definimos nossos modelos de dados.

Nele, vamos criar uma classe chamada `Product`, que será o modelo de dados que representa um produto em nosso sistema. Para isso, vamos importar o módulo `models` do Django e criar uma classe que herda de `models.Model` e, em seguida definiremos os campos que nosso modelo terá criando os atributos da classe `Product`:

```python
# ecommerce/products/models.py

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
      upload_to="media/products", null=True, blank=True
    )
```

Perceba que utilizamos os tipos de dados do Django para definir os campos do nosso modelo. Aqui utilizamos:

- `CharField` para campos de texto curtos, passando a opção `max_length` para definir o tamanho máximo do campo;
- `DecimalField` para campos de números decimais, passando as opções `max_digits` e `decimal_places` para definir o número máximo de dígitos e o número de casas decimais, respectivamente;
- `IntegerField` para campos de números inteiros, passando a opção `default` para definir um valor padrão para o campo;
- `TextField` para campos de texto longos;
- `DateTimeField` para campos de data e hora, passando as opções `auto_now_add` e `auto_now` para definir que o campo deve ser preenchido automaticamente com a data e hora atual quando o objeto for **criado** e **atualizado**, respectivamente;
- `ImageField` para campos de imagens, passando as opções `upload_to` para definir o diretório em que as imagens serão salvas, `null=True` para permitir que o campo seja nulo e `blank=True` para permitir que o campo seja vazio.

Estes são só alguns dos tipos e opções disponíveis, por isso, recomendamos que você dê uma espiada na [documentação oficial](https://docs.djangoproject.com/en/3.2/ref/models/fields/) para saber mais. 😉

Provavelmente você se deparou, no servidor em execução, com o erro `products.Product.image: (fields.E210) Cannot use ImageField because Pillow is not installed.` A solução para ele é indicada na própria mensagem do erro: basta instalar essa biblioteca no projeto com o comando `python3 -m pip install Pillow`.

> **Anota aí 📝:** Pillow é um pacote Python que adiciona suporte para imagens ao Django. Ele é necessário para que possamos utilizar o campo `ImageField`.

Depois da instalação, é só rodar novamente o servidor (`python3 manage.py runserver`) para ver que tudo voltou a funcionar corretamente. Com isso feito, prontinho, o modelo de dados foi criado! 🎉 Mas e agora? Como informar ao Django que queremos que ele crie uma tabela no banco de dados para armazenar esses dados do modelo? 🤔

A resposta é muito simples: precisamos criar uma _migration_ e executá-la:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

> Lembre-se de executar os comandos acima dentro do diretório em que se encontra o arquivo `manage.py`. 😉

O primeiro comando (`makemigrations`) cria um arquivo de _migration_ - resumidamente, são as instruções para a criação da tabela no banco de dados. Ele já olha para o seu _model_ e cria a _migration_ pra você! Já o segundo comando (`migrate`) executa as migrações, ou seja, usa as instruções do arquivo de _migration_ e cria a tabela no banco de dados.

Repare que um novo arquivo foi criado no diretório `ecommerce/products/migrations`. Ao abrir o arquivo `0001_initial.py` você verá que ele contém as instruções para a criação da tabela no banco de dados.

Com isso, nosso modelo de dados foi criado no banco de dados! 🎉

Que tal abrir o Workbench e verificar se a tabela foi criada corretamente? 😉

## Inserindo dados no banco de dados via terminal

Podemos inserir dados no banco de dados de diversas formas, mas hoje faremos isso de uma maneira nova: por meio do terminal do Django. O comando para acessar o terminal é:

```bash
python3 manage.py shell
```

Uma vez dentro do terminal, podemos importar o modelo que criamos:

```python
from products.models import Product
```

A partir disso, podemos criar um novo objeto e salvá-lo no banco de dados:

```python
moka = Product(name="Moka - 6 xícaras", price=199.99, amount=10, description="Cafeteira italiana, serve 6 xícaras, não elétrica")
moka.save()
```

Prontinho! Agora já temos o primeiro produto no banco de dados! 🎉

## Django admin

O **Django admin** é uma ferramenta que permite a criação de um painel de administração para o projeto. Com ele, é possível visualizar, criar, editar e excluir objetos do banco de dados (o famoso **CRUD**), sem a necessidade de escrever código.

Lembra da rota `'/admin'` que você viu no arquivo `urls.py`? Ela é mais um exemplo dos recursos prontos para uso que o Django oferece, pois é ela que permite o acesso ao painel de administração do projeto.

Se você acessar agora mesmo [localhost:8000/admin](http://localhost:8000/admin), verá que já existe um painel de administração criado. Ele exige, porém, um login, e não temos uma autenticação de admin configurada para o nosso projeto. Faremos essa configuração agora!

## Criando um superusuário

A primeira coisa que devemos fazer é criar um superusuário para o projeto. Esse perfil terá permissões administrativas,ou seja, poderá acessar o painel de administração e realizar qualquer operação.

Para criar um superusuário, na raiz do projeto, execute o comando:

```bash
python3 manage.py createsuperuser
```

Será preciso informar um nome de usuário, e-mail e senha. Preencha os dados e, em seguida, acesse [localhost:8000/admin](http://localhost:8000/admin) e faça login com os dados de superusuário que você criou. Você verá uma página como esta:

|![Página inicial do painel de administração do Django](https://content-assets.betrybe.com/prod/e4cf1ac4-33ad-4ddb-a0ad-96fc462c61d4-P%C3%A1gina%20inicial%20do%20painel%20de%20administra%C3%A7%C3%A3o%20do%20Django.png)|
|---|
|Página inicial do painel de administração do Django|

## Registrando o modelo

Para que o Django admin funcione, é preciso registrar os modelos criados no arquivo `admin.py`, dentro da pasta do _app_. Fazer isso é bem simples: abra o arquivo `ecommerce/products/admin.py` e adicione o código:

```python
from django.contrib import admin
from products.models import Product
from products.models import Customer # Modelo criado no exercício de fixação


admin.site.register(Product)
admin.site.register(Customer)
```

Já que estamos alterando este arquivo, que tal mudarmos também o cabeçalho do painel? Para isso, basta adicionar a linha no arquivo `ecommerce/products/admin.py`:

```diff
from django.contrib import admin
from products.models import Product


+ admin.site.site_header = "Trybe Products E-commerce"
admin.site.register(Product)
admin.site.register(Customer)
```

Agora, ao recarregar a página ou fazer login com seus dados de superusuário, você verá uma página como esta:

|![Painel de administração do Django com as tabelas](https://content-assets.betrybe.com/prod/e4cf1ac4-33ad-4ddb-a0ad-96fc462c61d4-Painel%20de%20administra%C3%A7%C3%A3o%20do%20Django%20com%20as%20tabelas.png)|
|---|
|Painel de administração do Django com as tabelas|

Nessa página você pode consultar os dados que já existem no banco de dados, criar novos objetos, editar e excluir objetos existentes. Vamos fazer um teste?

Clique em **Products**, depois no botão **ADD PRODUCT** (canto superior direito da página), preencha os campos com um novo produto e clique em **SALVAR**. Você verá uma página como esta:

|![Página de produtos](https://content-assets.betrybe.com/prod/e4cf1ac4-33ad-4ddb-a0ad-96fc462c61d4-P%C3%A1gina%20de%20produtos.png)|
|---|
|Página de produtos|

Muito legal, né?! Viu só o quanto você já conseguiu fazer utilizando o Django e com tão pouco código?! E este é apenas o início! 🚀

Repare que, quando você abre a tabela, o nome do objeto não aparece certinho - aparece um `Product object (N)`. Isso se dá porque o Django chama a função `__str__` de uma classe ao exibi-la lá. Se você sobrescrever sua implementação padrão com uma específica, pode controlar como aquela visualização fica.

Teste colocar a função abaixo no arquivo `ecommerce/products/models.py`:

```diff
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
      upload_to="media/products", null=True, blank=True
    )

+    def __str__(self):
+        return f'{self.name} - {self.price}'


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
```
