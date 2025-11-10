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

## Templates no Django

Finalmente, chegou a hora de colocar a mão ~~na massa~~ no código! 🎉

### Setup inicial

Para começar, crie o ambiente virtual que será utilizado e faça a instalação dos pacotes que serão utilizados:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install django
pip install Pillow # biblioteca para trabalhar com imagens
pip install mysqlclient # biblioteca para se comunicar com o MySQL
```

Em seguida, crie o projeto Django e a aplicação:

```bash
django-admin startproject event_manager .
django-admin startapp events
```

Faça a instalação da aplicação dentro do projeto no arquivo `settings.py`:

```diff
# event_manager/settings.py
...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
+   'events',
]

...
```

Faça também a mudança para usar o MySQL como banco de dados:

```diff
# event_manager/settings.py
...

DATABASES = {
    'default': {
-       'ENGINE': 'django.db.backends.sqlite3',
+       'ENGINE': 'django.db.backends.mysql',
-       'NAME': BASE_DIR / 'db.sqlite3',
+       'NAME': 'event_manager_database',
+       'USER': 'root',
+       'PASSWORD': 'password',
+       'HOST': '127.0.0.1',
+       'PORT': '3306',
    }
}

...
```

Crie o arquivo para o script SQL dentro do diretório `./database`:

```bash
mkdir database && cd database
touch 01_create_database.sql
```

Adicione o conteúdo do script para criação do banco de dados `event_manager_database`:

```sql
CREATE DATABASE IF NOT EXISTS event_manager_database;

USE event_manager_database;
```

Crie o Dockerfile na raiz do projeto:

```yaml
FROM mysql:8.0.32

ENV MYSQL_ROOT_PASSWORD password
COPY ./database/01_create_database.sql /docker-entrypoint-initdb.d/data.sql01
```

Faça o _build_ da imagem, basta rodar o comando dentro da pasta do projeto que contém o arquivo Dockerfile.

```bash
docker build -t event-manager-db .
```

Execute o container e o script de criação do banco copiado no Dockerfile:

```bash
docker run -d -p 3306:3306 --name=event-manager-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=event_manager_database event-manager-db
```

Acesse o banco de dados pelo _Workbench_ e verifique se ele foi criado corretamente.

Execute o comando `migrate` do Django:

```bash
python3 manage.py migrate
```

## Renderizando seu primeiro _template_

Antes de começarmos, saiba que a configuração padrão do Django permite que você crie seus _templates_ dentro de cada uma das aplicações do seu projeto, e assim faremos.

É possível alterar essa configuração para indicar diretórios específicos onde o Django deve procurar por _templates_. Por exemplo: na configuração abaixo, o Django irá buscar por _templates_ dentro do diretório `_templates_`, que está na raiz do projeto e não mais dentro de cada uma das aplicações do projeto. Lembre-se que você não precisa fazer a alteração abaixo.

```diff
# event_manager/settings.py
+ import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
-       'DIRS': [],
+       'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Agora sim, crie um novo diretório com nome `templates` dentro da aplicação `events` e, em seguida, crie o arquivo `home.html` dentro do novo diretório e inicie um arquivo HTML:

```html
<!--events/templates/home.html-->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Primeiro Template</title>
</head>
<body>
    <h1> Meu primeiro template usando Django! </h1>
</body>
</html>
```

O próximo passo é implementar a view que irá fazer a renderização do _template_ criado. Acesse o arquivo `views.py` dentro do app `events` e escreva a função que fará essa tarefa:

```python
# events/views.py
from django.shortcuts import render


def index(request):
    return render(request, 'home.html')
```

Prontinho! A função acima usa o método `render` do Django para renderizar o _template_ passado como segundo parâmetro `home.html`. O primeiro parâmetro, _request_, representa a requisição feita pela pessoa que usa a aplicação.

Mas agora você pode estar se perguntando: _Como faço para invocar a função que foi implementada?_ 🤔

A resposta é: através das rotas da nossa aplicação. A função criada será vinculada a uma das rotas da aplicação e, em seguida, serão incluídas nas rotas da aplicação no projeto.

Crie o arquivo `urls.py` dentro da aplicação `events` e nele escreva o código abaixo:

```python
# events/urls.py
from django.urls import path
from events.views import index


urlpatterns = [
    path("", index, name="home-page")
#   path("/rota-comentada", função-que-será-executada, name="nome-que-identifica-a-rota")
]
```

No código acima, uma lista de rotas (`urlpatterns`) foi definida e cada uma das rotas é definida através da função `path`, que recebe três parâmetros: o primeiro é o caminho para a rota em si (`""` indica a raiz da aplicação `https://localhost:8000/`), o segundo é a função que será executada quando a rota for acessada e o terceiro é o nome que identifica essa rota.

Agora, será necessário incluir as rotas da aplicação no projeto principal. Para isso, acesse o arquivo `urls.py` do projeto e faça a seguinte alteração:

```python
# event_manager/urls.py
  from django.contrib import admin
  from django.urls import path, include


  urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls'))
  ]
```

Com essas alterações você acabou de incluir as rotas da aplicação `events` no projeto `event_manager`, e fez isso usando o método `include` nativo do Django.

Acabou! 🎉🎉🎉 Execute o servidor e acesse a rota `http://localhost:8000/` para ver o template criado sendo renderizado.

> **Relembrando 🧠:** Para executar o servidor faça: `python3 manage.py runserver` no mesmo diretório em que se encontra o arquivo `manage.py`.

## Herança de _templates_

O Django permite que não se crie toda a estrutura de HTML para cada um dos _templates_. A DTL (_Django Template Language_) permite que se crie um template base que contém a estrutura essencial do HTML e lacunas intencionais - com cada template filho preenchendo as lacunas com o próprio conteúdo. Esse mecanismo é chamado de _Herança de templates_. Como exemplo, relembre o template `home.html` que criamos:

```html
<!-- events/templates/home.html -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Primeiro Template</title>
</head>
<body>
    <h1> Meu primeiro template usando Django! </h1>
</body>
</html>
```

Para ver a herança acontecendo na prática, copie todo o conteúdo desse arquivo e cole dentro de um novo arquivo HTML chamado `base.html` dentro do diretório `events/templates`.

Substitua, em seguida, o conteúdo da tag `title` (_Primeiro Template_) por `{% block title %} {% endblock %}`, além disso, também substitua a linha da tag `h1` por `{% block content %} {% endblock %}`. Ao final dessas alterações o arquivo `base.html` fica assim:

```html
<!-- events/templates/base.html -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %} {% endblock %}</title>
</head>
<body>
    {% block content %} {% endblock %}
</body>
</html>
```

A sintaxe `{% %}` indica que está sendo usada uma **Tag de template** do DTL. Ela é a **lacuna** que mencionamos mais cedo - um template filho irá preenchê-la. Nesse caso, usamos a tag `block`. Existem muitas **Tags de template** já implementadas no DTL. Você pode conferir todas as tags nativas do DTL na [documentação oficial](https://docs.djangoproject.com/pt-br/4.2/ref/templates/builtins/).

Ao fazer essas alterações, foram criados blocos vazios que poderão ser preenchidos por aqueles _templates_ que herdarem o arquivo `base.html`. Acima, criamos dois blocos - um chamado _title_ e outro chamado _content_ - para escrever o título da página que será exibida e para colocar todo o conteúdo HTML que se quer exibir, respectivamente.

Para usar a herança de _template_, faça o seguinte:

1. Vá no template filho e inclua no seu cabeçalho a seguinte sintaxe: `{% extends 'base.html' %}`, onde se usa a palavra reservada `extends` seguida de qual _template_ se quer herdar.
2. Modifique o template filho, por exemplo o `home.html`, criando os blocos com os mesmos nomes daqueles criados no _template_ herdado de acordo com a sintaxe abaixo.

> **Anota aí 📝:** para que a herança aconteça é obrigatório que o `{% extends 'nome-do-template.html' %}` seja a primeira tag de template que aparece no arquivo.

```html
<!-- events/templates/home.html -->
{% extends 'base.html' %}

{% block title %}
  Primeiro Template
{% endblock %}

{% block content %}
  <h1> Meu primeiro template usando Django! </h1>
{% endblock %}
```

Note que, ao invés de toda a estrutura base do HTML, você inclui as tags do template base e as preenche com o HTML que quiser. Ao rodar sua aplicação, verá que tudo continua funcionando, ou seja, a herança foi feita com sucesso! 👏

## Criando o _model_ `Event`

Antes de exibir a lista de eventos no _template_, é importante definir o modelo que será usado para representá-los. Eis ele abaixo:

```python
# events/models.py
from django.db import models


class Event(models.Model):
    TYPE_CHOICES = (
        ('C', 'Conference'),
        ('S', 'Seminar'),
        ('W', 'Workshop'),
        ('O', 'Other'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    event_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    is_remote = models.BooleanField(default=False)
    image = models.ImageField(upload_to='events/img', blank=True)

    def __str__(self): # O método __str__ é sobrescrito para indicar como será a visualização do objeto
        return f'{self.title} - {self.date} - {self.location}' # Título do evento - Data - Local
```

A tabela `event` ao ser criada no banco terá 8 colunas, sendo elas:

- `id`: inteiro e chave primária única pro evento (que não precisa ser explicitamente declarado no modelo);
- `title`: texto com no máximo 200 caracteres;
- `description`: texto sem limitação de caracteres;
- `date`: data e hora do evento;
- `location`: texto com no máximo 200 caracteres;
- `event_type`: texto com no máximo 50 caracteres e que só pode assumir os valores `C`, `S`, `W` ou `O` (ao usar o parâmetro choices, o Django faz a validação se o valor inserido é um dos valores permitidos);
- `is_remote`: booleano (True ou False) que indica se o evento é remoto ou não;
- `image`: imagem que será salva na pasta `{CAMINHO-DE-MÍDIA}/events/img` (o caminho de mídia pode ser definido no arquivo `settings.py`)

|![Detalhes da tabela event pelo workbench](https://content-assets.betrybe.com/prod/64465619-fb06-4e3c-b7d2-08de3a9f7c33-Detalhes%20da%20tabela%20event%20pelo%20workbench.png)|
|---|
|Detalhes da tabela event pelo workbench|

> **Relembrando 🧠:** quando há um campo imagem é preciso fazer a instalação do módulo Pillow. Para isso, basta executar o comando `pip install Pillow` no terminal. **Relembrando 🧠:** depois de definir o modelo que será usado, crie as _migrations_ e logo depois migre-as para o banco. Para isso, execute `python3 manage.py makemigrations` e `python3 manage.py migrate` no terminal.

## Renderizando os eventos no _template_

Toda função que renderiza um _template_ usando o método _render_, do Django, é capaz também de fornecer um _contexto_ para esse _template_. O termo _contexto_ aqui se refere a um dicionário (`dict`), que pode ser construído dentro da função e passado para o _template_ como terceiro parâmetro do método _render_.

Todas as chaves do contexto podem ser acessadas diretamente pelo _template_ através da sintaxe `{{ chave }}`. Assim, o _template_ fará a renderização do valor que estava associado à chave. Modifique a função `index` do arquivo `events/views.py` para que ela fique assim:

```python
# events/views.py
from django.shortcuts import render


def index(request):
    context = {"company": "Trybe"}
    return render(request, 'home.html', context)
```

Modifique também seu _template_ `home.html` para renderizar o valor da chave `company` do contexto:

```html
<!-- events/templates/home.html -->
 {% extends 'base.html' %}

 {% block title %}
   Primeiro Template
 {% endblock %}

 {% block content %}
     <h1> Meu primeiro template usando Django! </h1>
     <h2> {{ company }} </h2>
 {% endblock %}
```

As modificações feitas acima farão com que o template renderize o valor da chave `company` do contexto, que aqui, é a palavra `Trybe`. Ao atualizar a aplicação você terá:

## Trabalhando com elementos do banco usando Python

Você percebeu que o modelo `Event` herda de `models.Model`? Todas as classes que fazem essa mesma herança são usadas para representar tabelas do banco de dados. Pode não parecer importante, mas isso mostra o vínculo entre essa classe e a sua própria tabela no banco.

Além de representarem tabelas do banco, todas as classes que herdam de `models.Model` possuem um atributo chamado `objects`. Esse atributo permite a interação direta com o banco de dados usando a própria sintaxe do Python. Através desse atributo você pode criar novas entradas no banco, fazer consultas e até mesmo aplicar filtros em uma consulta. Já tivemos um gostinho disso no começo da seção.

Vamos ver na prática? 🤓

Execute o comando `python3 manage.py shell` no terminal, no mesmo diretório do arquivo `manage.py`. Esse comando abre o shell do Django já carregando suas configurações e permitindo usar o ORM do framework. Execute os comandos abaixo, linha a linha, para entender como podemos trabalhar com o banco de dados usando a sintaxe do Python:

```python
from events.models import Event # importa o modelo Event

Event.objects.all() # retorna todos os eventos do banco. Se você não criou nenhum, o retorno será um QuerySet vazio

Event.objects.create(title='Conferência de Django', description='Evento massa sobre Django', date='2023-09-29 12:00:00-03:00', location='São Paulo', event_type='C', is_remote=False) # cria um novo evento no banco

Event.objects.all() # retorna todos os eventos do banco. Agora o retorno será um QuerySet com um evento a mais

Event.objects.create(title='Django Workshop', description='Workshop que acontece semestralmente sobre Django', date='2024-10-02 15:30:00-03:00', location='Web', event_type='W', is_remote=True) # cria outro evento no banco

Event.objects.filter(is_remote=True) # retorna apenas os eventos do banco que são remotos

Event.objects.filter(event_type='W') # retorna apenas os eventos do banco que são workshops

Event.objects.filter(event_type='C', is_remote=False) # retorna apenas os eventos do banco que são conferências e presenciais, simultaneamente

Event.objects.filter(date__year=2024) # retorna apenas os eventos do banco que acontecem em 2024

Event.objects.filter(date__range=['2023-01-01', '2024-12-31']) # retorna apenas os eventos do banco que acontecem entre 2023 e 2024
```

São muitas as possibilidades! 🤯

Uma segunda maneira de fazer a inserção de elementos no banco de dados é através da instanciação e depois uso do método `save()`. Além disso, quando um objeto do modelo é instanciado podemos também acessar o método `delete()` para removê-lo do banco. Veja só:

```python
from events.models import Event # importa o modelo Event

Event.objects.all() # <QuerySet [<Event: Conferência de Django - 2023-09-29 15:00:00+00:00 - São Paulo>, <Event: Django Workshop - 2024-10-02 18:30:00+00:00 - Web>]>

evento_1 = Event(title='Django Devs', description='Pessoas fantásticas que usam Django se reunindo em um só lugar', date='2025-07-02 13:30:00-03:00', location='Web', event_type='W', is_remote=True) # instancia um novo evento

evento_1.save() # salva o evento no banco

evento_2 = Event(title='DjangoFest', description='Um festival um pouco menos legal que desenvolver com Django', date='2023-11-22 18:00:00-03:00', location='São Paulo', event_type='C', is_remote=False) # instancia outro evento

evento_2.save() # salva o evento no banco

Event.objects.all() # <QuerySet [<Event: Conferência de Django - 2023-09-29 15:00:00+00:00 - São Paulo>, <Event: Django Workshop - 2024-10-02 18:30:00+00:00 - Web>, <Event: Django Devs - 2025-07-02 16:30:00+00:00 - Web>, <Event: DjangoFest - 2023-11-22 21:00:00+00:00 - São Paulo>]>

evento_3 = Event(title='DJ ANGO', description='Conheça a mais nova sensação musical.', date='2027-06-19 20:00:00-03:00', location='São Paulo', event_type='C', is_remote=False) # instancia um evento idêntico ao anterior

evento_3.save() # salva o evento no banco

Event.objects.all() # <QuerySet [<Event: Conferência de Django - 2023-09-29 15:00:00+00:00 - São Paulo>, <Event: Django Workshop - 2024-10-02 18:30:00+00:00 - Web>, <Event: Django Devs - 2025-07-02 16:30:00+00:00 - Web>, <Event: DjangoFest - 2023-11-22 21:00:00+00:00 - São Paulo>, <Event: DJ ANGO - 2027-06-19 23:00:00+00:00 - São Paulo>]>

evento_3.delete() # remove o evento do banco

Event.objects.all() # <QuerySet [<Event: Conferência de Django - 2023-09-29 15:00:00+00:00 - São Paulo>, <Event: Django Workshop - 2024-10-02 18:30:00+00:00 - Web>, <Event: Django Devs - 2025-07-02 16:30:00+00:00 - Web>, <Event: DjangoFest - 2023-11-22 21:00:00+00:00 - São Paulo>]>
```

## Para fixar

Adicione mais 1 entrada no banco de dados, dentro da tabela `events` utilizando cada um dos métodos mostrados.

## Renderizando os eventos no _template_

Agora sim! Finalmente será possível renderizar os eventos no _template_. Para isso, precisamos passar todos os eventos que estão no banco como contexto para o _template_. Modifique o contexto da função `index` no arquivo `views.py` para que exista uma chave `events` cujo valor será uma consulta com todos os eventos que estão cadastrados no banco de dados:

```python
# events/views.py
from events.models import Event
from django.shortcuts import render


def index(request):
    context = {"company": "Trybe", "events": Event.objects.all()}
    return render(request, 'home.html', context)
```

Agora, adicione uma segunda tag `h2` no _template_ renderizando a chave `events`:

```html
<!-- events/templates/home.html -->
{% extends 'base.html' %}

{% block title %}
  Primeiro Template
{% endblock %}

{% block content %}
    <h1> Meu primeiro template usando Django! </h1>
    <h2> {{ company }} </h2>
    <h2> {{ events }} </h2>
{% endblock %}
```

|![Print da página home com eventos renderizados](https://content-assets.betrybe.com/prod/5f572d81-7bf9-495d-9f3b-924c877724a5-Print%20da%20p%C3%A1gina%20home%20com%20eventos%20renderizados.png)|
|---|
|Print da página home com eventos renderizados|

A visualização dos eventos ainda não está muito amigável, não é mesmo? 🙁 Isso acontece porque o retorno de `Event.objects.all()` é uma consulta (`QuerySet`), que pode ter 0, 1, 2, … n elementos. Para tornar essa visualização mais amigável é necessário iterar pelos elementos que existem na consulta e renderizar cada um deles individualmente.

A iteração pode ser feita usando a tag de _template_ `{% for %}`, cuja sintaxe é muito semelhante à sintaxe do Python, com a diferença que você precisará indicar no _template_ onde o `for` se encerra com a `tag de _template_` `{% endfor %}`:

```html
<!-- events/templates/home.html -->
{% extends 'base.html' %}

{% block title %}
  Primeiro Template
{% endblock %}

{% block content %}
     <h1> Meu primeiro template usando Django! </h1>
     <h2> {{ company }} </h2>
     {% for event in events %}
         <p> {{ event }} </p>
     {% endfor %}
{% endblock %}
```

A sintaxe acima permite que, dentro do _template_, seja feita uma iteração sobre cada um dos eventos presentes no contexto. Para cada elemento da iteração, é criada uma nova tag `p` renderizando aquele evento em específico.

|![Print da página home com eventos depois da iteração](https://content-assets.betrybe.com/prod/5f572d81-7bf9-495d-9f3b-924c877724a5-Print%20da%20p%C3%A1gina%20home%20com%20eventos%20depois%20da%20itera%C3%A7%C3%A3o.png)|
|---|
|Print da página home com eventos depois da iteração|

Já imaginou o que aconteceria se a consulta não tivesse nenhum elemento? 🤔 A resposta é: nada! Em uma consulta vazia não haverá nenhum evento para renderizar e você deve concordar que isso também não é muito amigável! 😅

Para resolver isso vamos usar a `tag de _template_` `{% empty %}` dentro do `for`, ela indicará o que queremos mostrar na tela caso não exista nenhum elemento na consulta que estamos fazendo:

```html
<!-- events/templates/home.html -->
{% extends 'base.html' %}

{% block title %}
  Primeiro Template
{% endblock %}

{% block content %}
    <h1> Meu primeiro template usando Django! </h1>
    <h2> {{ company }} </h2>
    {% for event in events %}
       <p> {{ event }} </p>
    {% empty %}
       <p> Não existem eventos cadastrados </p>
    {% endfor %}
{% endblock %}
```

Agora sim! 🎉🎉🎉 Ainda da para melhorar um pouquinho a visualização dos eventos, mas espere um pouco para fazer isso. Antes, vamos à implementação da visualização dos detalhes de um evento específico. 🤓

## Criando o _template_ de detalhes do evento

Para conseguir criar o _template_ de detalhes do evento, será necessário criar uma nova função no arquivo `views.py`. Essa função renderizará o novo _template_ `details.html` que será criado dentro da pasta `_templates_`. Além disso, na função a ser implementada, é necessário passar à _view_ o contexto com o evento específico que será renderizado no _template_.

Mas como o _template_ saberá qual evento será renderizado? 😱 Resposta: Será recebido um parâmetro na função que permitirá o resgate do evento e sua renderização. No modelo `Event`, esse parâmetro é o `id`, chave primária do evento. Observe a implementação:

```python
# events/views.py
from events.models import Event
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'details.html', {'event': event})
```

```html
<!-- events/templates/details.html -->
{% extends 'base.html' %}

{% block title %}
    {{ event.title }}
{% endblock %}


{% block content %}

    <h1>{{ event.title }}</h1>

    <p>{{ event.description }}</p>

    <p>{{ event.date|date }} - {{ event.location }}</p>

    {% if event.is_remote %}
        <p> Evento remoto </p>
    {% else %}
        <p> Evento presencial </p>
    {% endif %}

{% endblock %}
```

Na função `event_details`, o parâmetro `event_id` será recebido e utilizado para resgatar o evento específico que se quer renderizar. Esse resgate é feito com o uso da função `get_object_or_404()`, essa função recebe dois parâmetros: o primeiro é o modelo a ser resgatado e o segundo indica a busca a ser feita. No exemplo acima, é buscado por um `Event` cujo `id` é igual ao `event_id` recebido como parâmetro. Caso o evento não seja encontrado, será levantada uma exceção do tipo `Http404`.

Ao passar a chave `event` no contexto, é possível acessá-la dentro do _template_ e usá-la para recuperar o evento alvo com todos os seus atributos. Esses atributos podem ser acessados dentro do _template_ através da sintaxe `{{ event.title }}`, por exemplo. Assim, é possível montar um _template_ genérico para a renderização de qualquer evento, desde que ele seja passado no contexto. 🤯

Perceba também que foi utilizada a sintaxe condicional com a _Tag de Template_ `{% if %}` `{% else %}` e, assim como no `{% for %}`, é necessário indicar o fim da condição com `{% endif %}`.

Você deve ter notado o `{{ event.date|date }}` no _template_, né? A sintaxe para o uso de filtros de _template_ é composta da variável à qual quer se aplicar o filtro seguida por um `|` e logo depois o nome do filtro. O filtro, nesse caso, é como uma máscara formatadora: ela pega a informação e ajusta a forma como ela será exibida. Nesse exemplo foi usado o filtro de data, para que a formatação da data seja no padrão `DD de MMMMM de AAAA`.

É possível, naturalmente, aplicar outras configurações para mostrar a data em outro formato. Além do filtro de data, existem outros filtros já implementados e que podem ser acessados em todos os templates como `first`, `last`, `lower`, `upper`, `length`, `random`, `slugify`, etc. Para saber mais sobre os filtros disponíveis, acesse a [documentação oficial.](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#built-in-filter-reference).

O código que foi apresentado ainda não funciona: falta vincular a função criada com uma rota específica, dentro do arquivo `urls.py`. Será nessa rota em que haverá a indicação de que o `event_id` será passado como parâmetro. Veja a implementação:

```python
# events/urls.py
from django.urls import path
from events.views import index, event_details, about


urlpatterns = [
    path("", index, name="home-page"),
    path("about", about, name="about-page"),
    path("events/<int:event_id>", event_details, name="details-page"),
#   path("/rota-comentada", função-que-será-executada, name="nome-que-identifica-a-rota")
]
```

A rota `events/<int:event_id>` indica que a rota `events/` será seguida de um número inteiro, que representa um `event_id` e que será passado como parâmetro para a função `event_details`. Vale lembrar que o nome da rota é importante para que seja possível acessá-la dentro do _template_.

## Conectando a página inicial com a página de detalhes

A página de detalhes de um evento específico já funciona, acesse a rota `events/<int:event_id>` e veja! Entretanto, ainda não é possível acessá-la de maneira rápida e eficiente através da página inicial. Para adaptar a `home.html` , será necessário que você crie um link de redirecionamento para a página de detalhes de cada evento. Tarefa fácil ao usarmos a tag de template `url` que permite criar um link absoluto, veja:

```html
<!-- events/templates/home.html -->
{% extends 'base.html' %}

 {% block title %}
   Primeiro Template
 {% endblock %}

 {% block content %}
     <h1> Meu primeiro template usando Django! </h1>
     <h2> {{ company }} </h2>
    {% for event in events %}
       <p> <a href="{% url 'details-page' event.id %}"> {{ event }} </a> </p>
    {% empty %}
        <p> Não existem eventos cadastrados </p>
    {% endfor %}
{% endblock %}
```

A _tag de template_ `{% url %}` pode ser usada quando é necessário fazer a chamada de uma rota específica que já foi implementada e tem uma identificação no arquivo `urls.py`. No exemplo acima, a _tag de template_ é usada para invocar a rota identificada como `details-page`, e, como essa rota necessita do `id` do evento como parâmetro, ele é passado logo em seguida com `event.id`. Assim, ao adicionar a tag `a` cujo atributo `href` aponta para a rota de detalhes já implementada, é feito o vínculo entre as rotas. Agora, ao executar a aplicação você deve ter algo como:

|![Print da página home com rotas vinculadas](https://content-assets.betrybe.com/prod/aa4e5a53-fc21-4673-aa9a-9d25d6df689f-Print%20da%20p%C3%A1gina%20home%20com%20rotas%20vinculadas.png)|
|---|
|Print da página home com rotas vinculadas|

## Lidando com exceções

O que será que acontece se uma pessoa tenta acessar uma página de evento que não existe? Tipo a página `http://127.0.0.1:8000/events/99999` 😱 A resposta para essa pergunta é: como durante a implementação a função `get_object_or_404` foi usada, automaticamente, se não for possível resgatar o evento com `id` informado, será renderizada uma página padrão do Django indicando uma resposta 404, _Not Found_. Contudo, é possível personalizar, tratar essa exceção e exibir a página que desejar, veja só:

```python
# events/views.py
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from events.models import Event


def event_details(request, event_id):
    try:
        event = get_object_or_404(Event, id=event_id)
        return render(request, 'details.html', {'event': event})
    except Http404:
        return render(request, '404.html')
```

Daí, basta implementar o template `404.html` que deverá ser criado junto aos demais templates:

```html
<!-- events/templates/404.html -->
{% extends 'base.html' %}

{% block title %}
    Página não encontrada
{% endblock %}

{% block content %}
    <h1> 404 - Página não encontrada </h1>
    <h2> Desculpe, mas o evento não foi encontrado </h2>
    <p><a href="{% url 'home-page' %}"> Volte a página inicial </a></p>
{% endblock %}
```

Agora, ao tentar acessar uma página de evento que não existe, a exceção `Http404` levantada pela função `get_object_or_404` será tratada pelo try/except e resulta na renderização da página `404.html`. Na implementação da página foi usada a mesma sintaxe de herança de _templates_, e ao final do bloco content foi adicionado um link para a página inicial, usando novamente a `tag de _template_` `{% url %}` vinculando assim uma rota previamente identificada no `urls.py` (_home-page_).

## Aprimorando os _templates_

Pra finalizar a nossa aplicação, que tal acrescentarmos **estilo**, com CSS, às nossas páginas? Com isso feito, nossa aplicação já estará pronta pra ser usada!

Primeiro, vamos fazer uma alteração no nosso template `home.html` para facilitar a estilização da página. Vamos incluir um pouco mais de estrutura HTML para termos com o que trabalhar no CSS - além de incluir uma lógica para exibição de imagens dos eventos!

```html
<!-- events/templates/home.html -->
 {% extends 'base.html' %}
 {% load static %}

 {% block title %}
   Primeiro Template
 {% endblock %}

 {% block content %}
     <h1> Eventos {{ company }} </h1>
    {% for event in events %}
        <a href="{% url 'details-page' event.id %}"> 
            <div>
              {% if event.image %}
                <img src="{% static event.image.url %}" alt="Imagem sobre o evento" height="50">
              {% endif %}
                <h3> {{ event.title }} </h3>
                <p> {{ event.date }} </p>
                <p> {{ event.location }} </p>
            </div>
        </a>
    {% empty %}
        <p> Não existem eventos cadastrados </p>
    {% endfor %}
 {% endblock %}
```

> **De olho na dica 👀:** Se você tiver algum registro no banco de eventos que não possua imagem, a tag `img` não será renderizada em razão da condição imposta.

Use o painel admin para criar alguns eventos de maneira que você consiga fazer o upload de uma imagem que represente o evento. Para criar uma conta admin você pode executar `python3 manage.py createsuperuser` no mesmo diretório em que se encontra o arquivo `manage.py`. Além disso, também será necessário fazer o registro do modelo `Event` dentro do site, usando o arquivo `admin.py`:

```python
from django.contrib import admin
from events.models import Event


admin.site.site_header = 'Event Manager Admin Panel'
admin.site.register(Event)
```

|![Print da página admin ao adicionar um evento com todos os campos](https://content-assets.betrybe.com/prod/7a8e2922-211b-4e1d-95a6-9264f9651ef0-Print%20da%20p%C3%A1gina%20admin%20ao%20adicionar%20um%20evento%20com%20todos%20os%20campos.png)|
|---|
|Print da página admin ao adicionar um evento com todos os campos|

Mesmo adicionando um evento com imagem você ainda não será capaz de visualizar as imagens. Isso acontece porque ainda não fizemos a configuração de como vamos servir os arquivos estáticos do projeto.

|![Print da página inicial sem a imagem aparecendo](https://content-assets.betrybe.com/prod/7a8e2922-211b-4e1d-95a6-9264f9651ef0-Print%20da%20p%C3%A1gina%20inicial%20sem%20a%20imagem%20aparecendo.png)|
|---|
|Print da página inicial sem a imagem aparecendo|

## Arquivos estáticos

O primeiro passo para fazer a configuração é instalar dois pacotes que ajudarão com essa tarefa:

```bash
pip install whitenoise # Serve os arquivos estáticos a partir de um diretório
pip install django-static-autocollect # Coleta os arquivos estáticos e os coloca em um diretório
```

Faça as modificações necessárias no arquivo `settings.py`:

```diff
# event_manager/settings.py
...

 INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'events',
+   'static_autocollect'
 ]

 MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
+   'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
 ]

 ...

+ MEDIA_URL = ''
+ MEDIA_ROOT = BASE_DIR / 'media'

 STATIC_URL = 'static/'
+ STATIC_ROOT = BASE_DIR / 'staticfiles'

+ STATICFILES_DIRS = [
+     str(BASE_DIR / 'media/'),
+ ]

+ STORAGE = {
+    "default": {
+        "BACKEND": "django.core.files.storage.FileSystemStorage",
+    },
+    "staticfiles": {
+        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
+    }
+ }

+ WHITE_NOISE_AUTOREFRESH = True
```

Com essas modificações estamos:

- instalando o pacote `static_autocollect` no projeto;
- adicionando o pacote `whitenoise` na lista de middlewares;
- definindo o caminho relativo onde se encontra o diretório `media` em `MEDIA_URL`;
- definindo o caminho absoluto em `MEDIA_ROOT` e que será usado como caminho base para o upload de imagens vindas das pessoas usuárias;
- definindo o caminho absoluto em `STATIC_ROOT` e que será usado pelo `whitenoise` para servir os arquivos estáticos;
- definindo uma lista de caminhos em `STATICFILES_DIRS` que serão usados pelo `static_autocollect` para coletar os arquivos estáticos e direcionar para `STATIC_ROOT`;
- definindo o comportamento de armazenamento do `whitenoise`;
- definindo que o `whitenoise` deve atualizar os arquivos estáticos automaticamente.

Use o comando `python3 manage.py watch_static & python3 manage.py runserver` para executar o servidor e o `static_autocollect` em paralelo. Agora, a próxima adição de registro que for feita já será refletida na página inicial.

> **De olho na dica 👀:** A _tag de template_ `static` serve para indicar o caminho relativo do arquivo estático e junto com os `whitenoise` e `static_autocollect`, possibilita servir os arquivos estáticos. **Anota aí 📝:** A metodologia mais comum para servir arquivos estáticos é separar e servi-los externamente, [leia mais sobre isso](https://whitenoise.readthedocs.io/en/latest/django.html#use-a-content-delivery-network).

|![Print da página inicial com a imagem aparecendo](https://content-assets.betrybe.com/prod/7a8e2922-211b-4e1d-95a6-9264f9651ef0-Print%20da%20p%C3%A1gina%20inicial%20com%20a%20imagem%20aparecendo.png)|
|---|
|Print da página inicial com a imagem aparecendo|

Com um pouco de estilização, você pode deixar sua aplicação mais apresentável. Você pode usar CSS puro ou qualquer framework de CSS que desejar, fica à sua escolha e como se sentir mais confortável. A seguir temos um exemplo de estilização para a página inicial, ele foi feito usando o Tailwind CSS e contém exatamente as mesmas `tags` que foram apresentadas até então.

|![Print da página inicial com estilização](https://content-assets.betrybe.com/prod/7a8e2922-211b-4e1d-95a6-9264f9651ef0-Print%20da%20p%C3%A1gina%20inicial%20com%20estiliza%C3%A7%C3%A3o.png)|
|---|
|Print da página inicial com estilização|

Você pode fazer o download dos templates estilizados: [`base.html`](https://lms-assets.betrybe.com/lms/base.html) e [`home.html`](https://lms-assets.betrybe.com/lms/home.html). Nesse exemplo foi usado o CDN do Tailwind CSS, mas você poderia registrar o seu próprio arquivo CSS no template `base.html`.
