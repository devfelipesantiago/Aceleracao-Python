# O que é o Django REST Framework

Um _framework_ para criar uma API REST com Django. O **Django REST Framework**: te ajudar a fazer a criação de APIs REST com bem menos código e menos trabalho do que você teria para fazer tudo manualmente.

Alguns outros bons motivos para querer utilizar o DRF são destacados pela própria [documentação oficial](https://www.django-rest-framework.org/) do _framework_, como por exemplo:

- Suas políticas de autenticação, que incluem pacotes para OAuth1a e OAuth2.
- Serialização (processo de conversão de objetos Python em formatos como JSON, XML ou YAML, por exemplo) que suporta fontes de dados baseadas em ORM (_Object-Relational Mapping_) ou não.
- Completamente personalizável - basta usar views comuns baseadas em funções caso você não precise dos recursos mais poderosos.
- Documentação extensa e grande suporte da comunidade.
- Utilizado por empresas reconhecidas internacionalmente, incluindo Mozilla, Red Hat e Heroku.

## Iniciando o projeto

A aplicação que será desenvolvida durante o conteúdo de hoje é uma API para gerenciar playlists de músicas. Você pode estar achando o exemplo familiar e isso não é a toa! Para evidenciar como o a utilização do Django REST Framework torna mais rápido o desenvolvimento, você irá desenvolver uma API bem similar à que construiu no conteúdo sobre Formulários com Django. 😉

## Preparando o ambiente

Antes de iniciar, crie um diretório novo para o projeto e, dentro dele, crie e ative o ambiente virtual:

```bash
mkdir django-rest-framework && cd django-rest-framework
python3 -m venv .venv && source .venv/bin/activate
```

Com isso feito, podemos partir para as instalações!

## Instalações

Agora que você já sabe que o DRF depende do Django para funcionar, provavelmente já tem em mente o próximo passo. Se você está pensando na instalação do Django e do Django REST Framework, pensou certíssimo! 🤩

Para isso, você pode utilizar o comando:

```bash
pip install django djangorestframework
```

A [documentação oficial do DRF](https://www.django-rest-framework.org/#installation) recomenda a instalação de algumas outras dependências para serem utilizadas no desenvolvimento de APIs com esse framework. Hoje, utilizaremos duas delas: o `markdown` e o `django-filter`, além do `mysqlclient` que nos permitirá utilizar o MySQL como banco de dados. Para instalá-los, basta executar:

```bash
pip install markdown django-filter mysqlclient
```

A partir de agora, você já tem tudo o que precisa para começar a desenvolver a API! Os próximos passos serão bem similares ao que você já têm feito durante essa seção para iniciar aplicações criadas com Django, portanto, passaremos por eles mais rapidinho neste momento.

> **De olho 👀:** Se você ainda tiver alguma dúvida sobre as configurações iniciais, não deixe de conferir o conteúdo dos dias anteriores desta mesma seção, especialmente os dias 1 e 2. Além disso, as mentorias/monitorias são ótimos espaços para sanar suas dúvidas! 😉

## Criação do projeto e do app

Com as instalações feitas, o passo seguinte é a criação do projeto Django:

```bash
django-admin startproject playlistify .
```

> **Anota aí 📝:** Você pode nomear o seu projeto como quiser, desde que não utilize espaços ou caracteres especiais.

Agora que o projeto foi criado, entre no diretório dele e crie uma aplicação chamada `core`:

```bash
django-admin startapp core
```

Agora nossa estrutura de diretórios está assim:

```bash
django-rest-framework
│   ├── .venv
│   ├── playlistify
│   ├── core
├── manage.py
```

## Configurações iniciais

A primeira coisa que faremos para que nossa aplicação funcione corretamente é adicionar a aplicação ao `INSTALLED_APPS` do projeto, no arquivo `playlistify/settings.py`:

```diff
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
+    "core"
]
```

### Configurando o banco de dados

Como nos dias anteriores, modificaremos o banco de dados padrão do projeto para utilizar o MySQL, via Docker.

Para isso, precisamos alterar a variável `DATABASE`, no arquivo `playlistify/settings.py`, para que ela tenha as configurações de acesso ao banco necessárias:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'playlistify_database',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        }
}
```

Em seguida, é preciso criar um arquivo para o script SQL dentro do diretório `./database`:

```bash
mkdir database && cd database
touch 01_create_database.sql
```

O script de criação do banco de dados `playlistify_database` deve ficar assim:

```sql
CREATE DATABASE IF NOT EXISTS playlistify_database;

USE playlistify_database;
```

Um arquivo `Dockerfile` precisa ser criado na raiz do projeto (no mesmo nível em que o arquivo `manage.py`), com o seguinte conteúdo:

```yaml
FROM mysql:8.0.32

ENV MYSQL_ROOT_PASSWORD password
COPY ./database/01_create_database.sql /docker-entrypoint-initdb.d/data.sql01
```

O _build_ da imagem pode ser feito rodando o comando a seguir no diretório do projeto que contém o arquivo Dockerfile:

```bash
docker build -t playlistify-db .
```

> Certifique-se de rodar o comando no diretório que contém o arquivo `Dockerfile`.

Por fim, só precisamos executar o container, utilizando junto algumas variáveis de ambiente e o comando para executar o script de criação do banco:

```bash
docker run -d -p 3306:3306 --name=playlistify-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=playlistify_database playlistify-db
```

Você pode conferir se o banco foi criado utilizando o _Workbench_.

#### Migrações

Agora que o banco de dados está configurado, é preciso executar as _migrations_ iniciais do Django para que as tabelas necessárias sejam criadas. Para isso, basta executar o comando:

Depois que os modelos já estão implementados, é hora de criar e executar as _migrations_:

```bash
python3 manage.py migrate
```

> Certifique-se de que o container do banco de dados está rodando antes de executar esse comando.

Agora, pelo _Workbench_, você ver as tabelas foram criadas no banco de dados.

### Criando um superusuário

Para adiantar as coisas, já podemos partir para a criação de um superusuário para que seja possível acessar o _admin_ do Django:

```bash
python3 manage.py createsuperuser
```

> **Relembrando 🧠:** Você terá que informar um nome de usuário, um e-mail e uma senha durante essa etapa. É com esses dados que você irá acessar o _admin_ daí em diante.

## Rodando o projeto

Com tudo configurado, podemos finalmente rodar o projeto para ver se está tudo funcionando corretamente:

```bash
python3 manage.py runserver
```

Faça login na rota `/admin` para conferir se está tudo certo. Daqui para frente, focaremos na construção de nossa API!

## DRF - Models

Até aqui, já foram feitas todas as configurações necessárias para o projeto e finalmente podemos seguir para a construção da nossa API com o Django REST Framework (DRF).

O ponto de partida será incluir o `rest-framework` no projeto. Uma vez que ele já está instalado no ambiente virtual, basta adicioná-lo à variável `INSTALLED_APPS`, no arquivo `playlistify.settings.py` do projeto:

```diff
# ...
"core",
+ "rest_framework",
```

A partir disso, o Django já reconhece o DRF e podemos começar a utilizá-lo.

## Models

Em seguida, é preciso que os modelos da API sejam definidos. Como dito anteriormente, nossa API será construída para o gerenciamento de playlists e por isso, utilizaremos os mesmos três modelos do dia sobre Formulários com Django, que são: `Singer`, `Playlist` e `Music`, de forma que o arquivo `core/models.py` ficará como a seguir:

```python
from django.db import models


class Singer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=50)
    recorded_at = models.DateField()
    length_in_seconds = models.IntegerField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="musics")

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    musics = models.ManyToManyField("Music", related_name="playlists")

    def add_music(self, music):
        self.musics.add(music)
        self.save()

    def remove_music(self, music):
        self.musics.remove(music)
        self.save()

    def __str__(self):
        return self.name
```

> **Relembrando 🧠:** O relacionamento entre os modelos `Singer` e `Music` é <1:N>, pois uma música pode pertencer a apenas uma pessoa artista, mas cada artista pode ter várias músicas. Enquanto isso, o relacionamento entre `Music`e `Playlist` é de <N:N>, dado que uma música pode estar em várias playlists e uma playlist pode ter várias músicas.

Com os modelos definidos, podemos parar o servidor com o atalho `ctrl`+ `c` e logo em seguida criar as _migrations_ e aplicá-las ao banco de dados com os comandos:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## Registrando os models no admin

Ainda não registramos os modelos no arquivo `core/admin.py`. É isso que faremos agora:

```python
from django.contrib import admin
from .models import Singer, Music, Playlist

admin.site.register(Singer)
admin.site.register(Music)
admin.site.register(Playlist)
```

## Serializers

Para continuar precisamos de um serializador (ou _serializer_). Mas o que é isso e qual sua utilidade para aplicações construídas com o DRF?

Um serializador de dados no DRF é o que permite converter objetos Python em formatos como JSON, XML, YAML, entre outros. Isso é importante para que os dados sejam enviados e recebidos de forma estruturada e legível por diferentes sistemas e clientes. Resumidamente, isso garante maior compatibilidade, controle de dados e facilita as validações.

Quando desenvolvemos uma API em Django com o DRF, o fluxo de dados pode ser resumido assim:

|![Fluxo de dados de requisição](https://content-assets.betrybe.com/prod/664d5b53-6c37-4043-a8a7-85f25b2f5ae1-Fluxo%20de%20dados%20de%20requisi%C3%A7%C3%A3o.png)|
|---|
|Fluxo de dados de requisição|

O passo a passo demonstrado na imagem é basicamente o seguinte:

- Alguém faz uma requisição HTTP para a API.
- A URL envia a requisição para a view.
- A view processa a requisição e envia os dados para o serializer.
- O serializer serializa os dados e os envia para a model.
- A model processa os dados e faz as consultas necessárias no banco de dados.
- O banco de dados devolve os resultados para a model.
- A model processa os dados e os envia para o serializer.
- O serializer serializa os dados e os envia para a view.
- A view envia os dados serializados para quem os solicitou.

A partir disso, a pessoa que fez a requisição pode fazer o que quiser com os dados recebidos.

Para criar os _serializers_, é necessário criar um arquivo chamado `serializers.py` dentro da pasta `core` e incluir os _serializers_ dos modelos, como a seguir:

```python
from rest_framework import serializers
from .models import Singer, Music, Playlist


class SingerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Singer
        fields = ["id", "name"]


class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Music
        fields = ["id", "name", "recorded_at", "length_in_seconds", "singer"]


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = ["id", "name", "is_active", "created_at", "updated_at", "musics"]
```

Note que utilizamos uma classe dentro de outra para definir quais campos serão serializados. Essa classe interna **precisa** se chamar **Meta** e ela é a responsável por fornecer metadados e algumas configurações adicionais ao serializador, como definir modelos associados ao serializador ou quais campos serão ou não usados por ele.

> **De olho na dica 👀:** Você pode ler mais sobre os serializadores [aqui](https://www.django-rest-framework.org/api-guide/serializers/#metadata). 😉

Além disso, utilizamos o `HyperlinkedModelSerializer`, que é uma classe especializada do serializador do DRF que cria automaticamente campos de URL para relacionamentos de modelo.

## Viewsets

_Viewsets_ são classes que fornecem uma abstração para agrupar a lógica de manipulação de um CRUD (Create, Retrieve, Update, Delete) relacionada a um modelo de dados específico.

Eles fornecem uma interface consistente e poderosa para manipular recursos RESTful, permitindo que você defina facilmente métodos para lidar com diferentes operações em um único local.

Para criar os _viewsets_ da nossa API, temos que alterar o arquivo `core/views.py` para incluir as _views_ dos nossos modelos.

Para isso, precisamos importar o `viewsets` do DRF, bem como os modelos e os serializadores que criamos, como a seguir:

```diff
- from django.shortcuts import render
+ from rest_framework import viewsets
+ from .models import Singer, Music, Playlist
+ from .serializers import SingerSerializer, MusicSerializer, PlaylistSerializer
```

Iremos definir classes para cada um de nossos modelos, que herdam de `viewsets.ModelViewSet`. Essa classe mapeia automaticamente as ações CRUD para os métodos HTTP correspondentes (GET, POST, PUT, DELETE) e manipula as operações associadas ao modelo de forma consistente.

> **Anota aí 📝:** `ModelViewSet`, que é uma classe especializada do DRF que fornece uma implementação padrão para as operações CRUD.

Dentro das classes, definimos os atributos `queryset` e `serializer_class`. O primeiro é responsável por definir o conjunto de objetos que serão retornados quando a _view_ for acessada. Já o segundo, define qual serializador será utilizado para serializar os dados retornados.

O arquivo `core/views.py` ficará como a seguir:

```diff
from rest_framework import viewsets
from .models import Singer, Music, Playlist
from .serializers import SingerSerializer, MusicSerializer, PlaylistSerializer


+ class SingerViewSet(viewsets.ModelViewSet):
+     queryset = Singer.objects.all()
+     serializer_class = SingerSerializer


+ class MusicViewSet(viewsets.ModelViewSet):
+     queryset = Music.objects.all()
+     serializer_class = MusicSerializer


+ class PlaylistViewSet(viewsets.ModelViewSet):
+     queryset = Playlist.objects.all()
+     serializer_class = PlaylistSerializer
```

Estamos quase lá! Agora, precisamos definir as rotas do nosso projeto!

## Rotas do projeto

Quando falamos de rotas do projeto, talvez você já pense automaticamente no arquivo `playlistify/urls.py`. É exatamente para lá que vamos agora!

Lá, definiremos um router, que receberá os _viewsets_ que criamos há pouco como parâmetro e registraremos as rotas da API no projeto, utilizando a função `include()` do módulo `django.urls`:

```diff
from django.contrib import admin
from django.urls import path, include
+ from rest_framework import routers
+ from core.views import SingerViewSet, MusicViewSet, PlaylistViewSet

+ router = routers.DefaultRouter()
+ router.register(r'singers', SingerViewSet)
+ router.register(r'musics', MusicViewSet)
+ router.register(r'playlists', PlaylistViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
+   path('', include(router.urls)),
]
```

Agora, se você rodar o servidor com o comando `python3 manage.py runserver` e acessar a rota `localhost:8000/singers`, por exemplo, verá que a API já está funcionando! 🎉

Mais do que isso! Ela já está apta a fazer todas as operações de um CRUD, ou seja, você pode criar, editar, deletar e listar os dados dos modelos `Singer`, `Music` e `Playlist`!

Vamos explorar um pouquinho como está a API? Utilize o Thunder Client ou qualquer outra ferramenta que permita fazer requisições HTTP para testar APIs e explore as rotas que criamos. Você pode criar, editar, deletar e listar os dados dos modelos `Singer`, `Music` e `Playlist`!

> **De olho na dica 👀:** Para fazer requisições a rotas do tipo `POST`, `PUT` e `DELETE`, você precisará colocar uma barra (‘/‘) ao fim da URL. Por exemplo, utilize `localhost:8000/singers/` ao tentar cadastrar uma nova pessoa artista na API! 😉

