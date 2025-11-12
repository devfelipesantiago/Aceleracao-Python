# Setup inicial

Hoje veremos como utilizar vários recursos legais do Django com formulários. Para conduzir o aprendizado de forma mais dinâmica, usaremos um exemplo prático para guiar o conteúdo.

Para isso, hoje desenvolveremos uma aplicação para gerenciar _playlists_!

Como sempre, o primeiro passo é criar o ambiente virtual que será utilizado e fazer a instalação dos pacotes que serão utilizados:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install django
pip install mysqlclient
```

Em seguida, crie o projeto Django `playlist_manager` e a aplicação `playlists`:

```bash
django-admin startproject playlist_manager .
django-admin startapp playlists
```

No arquivo `settings.py`, adicione a aplicação ao projeto e altere as configurações para usar o MySQL:

```diff
# playlist_manager/settings.py
# ...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
+   'playlists',
]

# ...

DATABASES = {
    'default': {
-       'ENGINE': 'django.db.backends.sqlite3',
+       'ENGINE': 'django.db.backends.mysql',
-       'NAME': BASE_DIR / 'db.sqlite3',
+       'NAME': 'playlist_manager_database',
+       'USER': 'root',
+       'PASSWORD': 'password',
+       'HOST': '127.0.0.1',
+       'PORT': '3306',
    }
}
```

> O simples ato de adicionar a aplicação ao projeto, incluindo-a na variável `INSTALLED_APPS`, equivale a instalar a aplicação no projeto. Por isso, é comum que este passo seja descrito da segunda forma em alguns fóruns.

Crie o arquivo para o script SQL dentro do diretório `./database`:

```bash
mkdir database && cd database
touch 01_create_database.sql
```

Adicione o conteúdo do script para criação do banco de dados `playlist_manager_database`:

```sql
/* database/01_create_database.sql */
CREATE DATABASE IF NOT EXISTS playlist_manager_database;

USE playlist_manager_database;
```

Crie o Dockerfile na raiz do projeto:

```yaml
# Dockerfile
FROM mysql:8.0.32

ENV MYSQL_ROOT_PASSWORD password
COPY ./database/01_create_database.sql /docker-entrypoint-initdb.d/data.sql01
```

Agora você já pode fazer o _build_ da imagem. Basta rodar o comando a seguir **dentro da pasta do projeto que contém o arquivo Dockerfile**:

```bash
docker build -t playlist-manager-db .
```

O próximo passo é executar o container e o script de criação do banco de dados:

```bash
docker run -d -p 3306:3306 --name=playlist-manager-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=playlist_manager_database playlist-manager-db
```

> Caso queira, verifique pelo _Workbench_ se o banco de dados foi criado corretamente. 😉

Ao longo deste conteúdo, utilizaremos três modelos: `Singer`, `Music` e `Playlist`. O primeiro representará pessoas cantoras das músicas, o segundo representará a música em si, enquanto o terceiro será a representação de um conjunto de músicas que compõe uma _playlist_.

A implementação do arquivo `playlists/models.py` é apresentada abaixo:

```python
# playlists/models.py

from django.db import models


class Singer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=50)
    recorded_at = models.DateField()
    length_in_seconds = models.IntegerField()

    def __str__(self):
        return self.name
```

Perceba que não há nada novo na implementação destes modelos.

Você deve ter notado também que, por existir uma conexão entre eles, poderíamos adicionar relacionamento entre essas tabelas. Pode acalmar seu coração, nós faremos isso! Só que um pouquinho mais adiante! 😅

## Introdução aos Formulários no Django

No Django, existe uma classe que permite que você consiga receber e validar dados de uma maneira rápida e prática. Essa é a classe `Form`, que está implementada no módulo `django.forms`.

Em resumo, um formulário pode ser criado para receber e validar dados que chegarão em uma requisição. Isso possibilita a criação ou atualização de registros no banco de dados de forma mais confiável.

## Criando um formulário

Quando pensamos em criar um formulário, a primeira coisa a se fazer é definir qual será seu propósito. Como ele se encaixa na lógica da aplicação que estamos desenvolvendo para conseguirmos delimitar o que ele irá conter.

iniciaremos construindo um formulário cujo propósito é adicionar novas músicas ao banco.

Para isso, crie um arquivo `forms.py` dentro da aplicação `playlists`. É nesse arquivo que serão construídos os formulários da aplicação. Depois de criado, adicione o seguinte código:

```python
# playlists/forms.py
from django import forms


class CreateMusicForm(forms.Form):
    name = forms.CharField(max_length=50)
    recorded_at = forms.DateField()
    length_in_seconds = forms.IntegerField()
```

Percebeu que os atributos do formulário que criamos têm praticamente a mesma sintaxe dos que foram criados no modelo `Music`?

Isso acontece porque para criar um novo registro na tabela `music` é obrigatório fornecer os três campos. Já para o modelo `Playlist`, por exemplo, os campos `created_at` e `updated_at` não precisam ser passados, então não precisamos desses campos:

```diff
# playlists/forms.py
from django import forms


class CreateMusicForm(forms.Form):
    name = forms.CharField(max_length=50)
    recorded_at = forms.DateField()
    length_in_seconds = forms.IntegerField()


+ class CreatePlaylistForm(forms.Form):
+     name = forms.CharField(max_length=50)
+     is_active = forms.BooleanField()
```

Uma grande vantagem de se usar um formulário é a maneira eficaz que ele proporciona a validação dos dados em cada campo.

Observe: o atributo `name = forms.CharField(max_length=50)` indica que o formulário deve ter uma entrada `name` do tipo _String_ com no máximo 50 caracteres. Por outro lado, o atributo `duration_in_seconds = forms.IntegerField()` indica que o formulário deve ter uma entrada `duration_in_seconds` cujo valor correspondente deve ser do tipo inteiro.

## Formulários vinculados vs não vinculados

Para o Django, formulários podem ser classificados como vinculados ou não vinculados.

Um formulário é considerado como não vinculado caso seja instanciado sem nenhum dado, caso contrário, ele é vinculado. A própria classe `Form` apresenta um atributo `is_bound` que indica se o formulário é vinculado ou não. Observe o exemplo abaixo:

```python
from playlists.forms import CreatePlaylistForm


form = CreatePlaylistForm()
form.is_bound # retorna False

form = CreatePlaylistForm({"name":"Playlist de Estudo", "is_active": True})
form.is_bound # retorna True
```

> **De olho na dica 👀:** qualquer dicionário passado como parâmetro já faz com que o formulário seja considerado como vinculado.

E afinal, qual a diferença? 🤔

Formulários vinculados podem validar os dados passados por parâmetro. Já formulários não vinculados não podem fazer isso. Veremos sobre isso a seguir!

## Validação de dados

A classe `Form` implementa o método `is_valid()`, que retorna um booleano para informar se os dados do formulários são válidos ou não.

Além disso, a classe `Form` também implementa o atributo `errors` que retorna um dicionário com os erros de validação de cada campo do formulário. Veja o exemplo abaixo:

```python
from playlists.forms import CreatePlaylistForm

form = CreatePlaylistForm({}) # formulário instanciado com um dicionário vazio
form.is_valid() # retorna False
form.errors # retorna {'name': ['Este campo é obrigatório.'], 'is_active': ['Este campo é obrigatório.']}

form_2 = CreatePlaylistForm({"name":"Essa playlist tem um nome com mais de cinquenta caracteres, o que você acha que vai acontecer?", "is_active": True})
form_2.is_valid() # retorna False
form_2.errors # retorna {'name': ['Certifique-se de que o valor tenha no máximo 50 caracteres (ele possui 94).']}

form_3 = CreatePlaylistForm({"name":"Playlist de Estudo", "is_active": True})
form_3.is_valid() # retorna True
form_3.errors # retorna {}

unbound_form = CreatePlaylistForm() #  formulário não vinculado
unbound_form.is_valid() #  retorna False
unbound_form.errors #  retorna {} Esse tipo de formulário não passa por validação
```

Muito legal e prático, não é mesmo? 😎

Mas e se a validação envolver uma regra de negócio mais complexa? 🤔

## Criando validações personalizadas

É possível criar suas próprias funções de validação para os campos de um formulário, isso permite que você aplique a regra de negócio que quiser para validar um campo.

Para trazer o exemplo prático, vamos considerar que a duração de uma música, `length_in_seconds`, precisa ser um número inteiro entre 1 e 3600 segundos. A função de validação precisa levantar uma exceção `ValidationError`, que será implementada no módulo `django.core.exceptions` e que receberá como parâmetro a mensagem de erro que será exibida caso a validação falhe.

Crie um arquivo `validators.py` dentro da aplicação `playlists` e implemente uma função que faz a checagem se um número inteiro está entre 1 e 3600 segundos:

```python
# playlists/validators.py

from django.core.exceptions import ValidationError


def validate_music_length(value):
    if value not in range(1, 3601):
        raise ValidationError(
            f"A duração da música deve ser um número"
            f" inteiro entre 1 e 3600 segundos. O valor "
            f"{value} não é válido."
        )
```

O próximo passo é indicar no campo do formulário que o dado recebido ali deve ser validado pela função criada, para além das validações padrão. Essa tarefa é feita por meio do parâmetro `validators` que recebe uma lista com todas as funções personalizadas para validação do campo. Veja abaixo:

```diff
# playlists/forms.py

from django import forms
+ from playlists.validators import validate_music_length


class CreateMusicForm(forms.Form):
    name = forms.CharField(max_length=50)
    recorded_at = forms.DateField()
+    length_in_seconds = forms.IntegerField(validators=[validate_music_length])
```

Agora, se você tentar criar uma música com uma duração menor que 1 ou maior que 3600 segundos, o formulário não será considerado válido e a mensagem de erro será exibida. Veja o exemplo abaixo:

> Execute o código abaixo no terminal interativo do Django (`python3 manage.py shell`) ⚠️ Se você já estiver com um terminal interativo aberto, é necessário fechá-lo (`exit()`) e abrir um novo, pois, do contrário, as modificações feitas não serão consideradas.

```python
from playlists.forms import CreateMusicForm


form = CreateMusicForm({"name":"The sound of silence", "recorded_at":"2023-07-05", "length_in_seconds":0}) # formulário instanciado com um dado inválido
form.is_valid() # retorna False
form.errors # retorna {'length_in_seconds': ['A duração da música deve ser um número inteiro entre 1 e 3600 segundos. O valor 0 não é válido.']}
```

> **De olho na dica 👀:** o Django possui uma série de validações prontas para serem usadas, você pode conferir a lista com as validações na [documentação oficial.](https://docs.djangoproject.com/en/4.2/ref/validators/#built-in-validators)

Além de indicar os validadores nos campos do formulário, também é possível indicar os validadores dentro do modelo da aplicação, utilizando o mesmo parâmetro (`validators`) na função que define cada campo.

Entretanto, é importante dizer que, mesmo que você indique os validadores no modelo, eles não serão executados automaticamente e ainda será possível criar registros com dados que não passam nas validações desejadas. Por isso, indicar os validadores no modelo pode parecer inútil, mas acredite, isso trará benefícios quando explorarmos outros tipos de formulários. 😉

Veja como fica o modelo com a validação:

```diff
# playlists/models.py

from django.db import models
+ from playlists.validators import validate_music_length

# ...

class Music(models.Model):
    name = models.CharField(max_length=50)
    recorded_at = models.DateField()
+    length_in_seconds = models.IntegerField(validators=[validate_music_length])

    def __str__(self):
        return self.name
```

> **Relembrando 🧠:** como foi feita uma modificação no modelo, lembre-se de criar as migrações e migrá-las para o banco de dados. Para isso, execute os comando: `python3 manage.py makemigrations`e `python3 manage.py migrate`.

## Renderizando formulários em templates

Neste momento, você já sabe como fazer para criar registros no banco de dados e também já sabe checar se um formulário é válido ou não. Chegou a hora de unir esses dois conhecimentos!

> **Relembrando 🧠:** para criar um novo registro no banco, você pode usar o método `.create()` do atributo `objects`, do modelo em questão.

## Novo registro a partir de um formulário

Uma vez que você já possui um formulário que tem dados válidos, é preciso repassar esses dados para o modelo e, assim, criar o novo registro no banco. Para isso, depois de usar o método `is_valid()` para checar a integridade dos dados passados, você pode usar o atributo `cleaned_data` para que um dicionário com todos os dados sejam retornados para você. Esses dados, agora já validados, podem ser usados para criar um novo registro no banco.

O passo a passo abaixo demonstra como é possível fazer isso e pode ser executado no terminal interativo do Django:

```python
from playlists.forms import CreateMusicForm
from playlists.models import Music

form = CreateMusicForm({"name":"Be brave, Dev", "recorded_at":"2023-06-05", "length_in_seconds":180})

if form.is_valid():
    data = form.cleaned_data # data será igual à {"name":"Be brave, Dev", "recorded_at":"2023-06-05", "length_in_seconds":180}
    Music.objects.create(**data) # criando um novo registro no banco com os dados do formulário
    # Music.objects.create(**data) é o mesmo que Music.objects.create(name="Be brave, Dev", recorded_at="2023-06-05", length_in_seconds=180)
```

Você pode apertar a tecla `enter` duas vezes para sair do escopo da condição (`if`) que acabamos de criar. 😉

> **Anota aí 📝:** A sintaxe `**data` é do Python e é uma desestruturação para passar cada um dos pares chave e valor, individualmente, como parâmetros.

Prontinho! Conseguimos conectar os conhecimentos sobre criação de registros no banco de dados e formulários. 🤩 O próximo passo agora é receber os dados direto da requisição e, a partir deles, criar o novo registro no banco. Vamos lá?

## Formulários e templates

Você já sabe que podemos renderizar variáveis passadas como contexto para um template. Vamos explorar esse recurso?

Crie o diretório `templates` dentro da aplicação `playlists` e nele crie os dois primeiros templates `base.html` e `music.html`. Implemente a estrutura para herança de templates e, no arquivo `music.html`, renderize a variável `form` dentro do bloco `content`.

```html
<!-- playlists/templates/base.html -->

<!DOCTYPE html>
<html lang="pt-br">
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

```html
<!-- playlists/templates/music.html -->

{% extends 'base.html' %}

{% block title %}
    Formulário para Nova Música
{% endblock %}

{% block content %}
    {{form}}
{% endblock %}
```

Implemente a primeira função no arquivo `views.py` com nome de `music` que irá renderizar `music.html`. Passe no contexto uma instância do formulário `CreateMusicForm` como valor da chave `form`.

```python
# playlists/views.py

from django.shortcuts import render
from playlists.forms import CreateMusicForm


def music(request):
    form = CreateMusicForm()
    context = {"form": form}
    return render(request, "music.html", context)
```

Crie o arquivo `urls.py`, dentro da aplicação `playlists`. Nele, configure a rota para a função `create_music` que você acabou de criar.

```python
# playlists/urls.py

from django.urls import path
from playlists.views import music


urlpatterns = [
    path("musics/", music, name="musics-page"),
]
```

Por fim, inclua a rota da aplicação no arquivo `urls.py` **do projeto**.

```diff
# playlist_manager/urls.py

from django.contrib import admin
+ from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
+     path("", include("playlists.urls"))
]
```

Execute a aplicação (`python3 manage.py runserver`) e veja como o formulário é renderizado na [tela](http://localhost:8000/musics/). 😱

|![Print da página home com formulário renderizado](https://content-assets.betrybe.com/prod/96e99cca-8ea5-49f9-9722-6bd9cfb47988-Print%20da%20p%C3%A1gina%20home%20com%20formul%C3%A1rio%20renderizado.png)|
|---|
|Print da página home com formulário renderizado|

A instância do formulário é convertida para um conjunto de tags HTML que renderizam o formulário criado por você. Você pode alterar a forma como esse formulário é renderizado por meio de alguns atributos com _layouts_ diferentes. Usaremos aqui o `as_p`:

```diff
<!-- playlists/templates/music.html -->

{% extends 'base.html' %}

{% block title %}
    Formulário para Nova Música
{% endblock %}

{% block content %}
+     {{form.as_p}}
{% endblock %}
```

Experimente trocar o `as_p` por `as_div` e `as_ul`, inspecione o conteúdo HTML ao usar cada um e veja a diferença entre eles!

Você deve ter notado, também, que embora o formulário esteja lá, não temos nenhum botão para enviar os dados. Veremos, após o exercício, como incluí-l.o 😉

## Personalizando o formulário

O formulário renderizado no template ainda não está dentro do que é esperado. Os nomes que designam cada um dos campos ainda estão em inglês e, além disso, é necessário modificar os campos que são renderizados. Por exemplo, `recorded_at`, que representa uma data, está sendo renderizado como um campo de texto.

Essas configurações podem ser feitas diretamente no formulário, no momento de se definir a classe. Podemos usar o parâmetro `labels` para indicar qual deverá ser o nome de cada um dos campos. Ainda, podemos usar o parâmetro `initial` para sugerir um dado inicial caso faça sentido para aquele campo. Veja como fica a implementação do formulário `CreateMusicForm` ao usarmos esses parâmetros:

```python
# playlists/forms.py

from django import forms
from playlists.validators import validate_music_length, validate_name


class CreateMusicForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        validators=[validate_name],
        label="Nome da música",
    )
    recorded_at = forms.DateField(
        label="Data de gravação",
        initial="2023-07-06",
    )
    length_in_seconds = forms.IntegerField(
        validators=[validate_music_length],
        label="Duração em segundos",
    )
```

> **De olho na dica 👀:** também é possível usar o parâmetro `help_text` para indicar uma frase de auxílio no preenchimento do campo. Experimente!

Colocar um valor inicial pode ajudar no preenchimento do campo, mas isso não necessariamente melhora a experiência da pessoa usuária. Contudo, é possível melhorar essa experiência modificando a aparência dos campos do formulário com um _widget_.

Um _widget_ nada mais é do que uma representação HTML mais elaborada de um campo `input`. Felizmente, o Django tem diversos _widgets_ já implementados e prontos para serem usados. Além disso, ele também permite que você crie seus próprios _widgets_! 🤯

Para usar um _widget_, basta passá-lo como parâmetro ao definir o campo, assim como é feito para o parâmetro `label`.

Para fazer as melhores escolhas, é necessário conhecer os _widgets_ disponíveis e você pode ver a lista completa de _widgets_ nativos do Django na [documentação oficial](https://docs.djangoproject.com/en/4.2/ref/forms/widgets/#built-in-widgets). Aqui, usaremos o `DateInput()`:

```diff
# playlists/forms.py

from django import forms
from playlists.validators import validate_music_length, validate_name


class CreateMusicForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        validators=[validate_name],
        label="Nome da música",
    )
    recorded_at = forms.DateField(
        label="Data de gravação",
+         widget=forms.DateInput(attrs={"type": "date"}),
        initial="2023-07-06",
    )
    length_in_seconds = forms.IntegerField(
        validators=[validate_music_length],
        label="Duração em segundos",
    )
```

> **De olho na dica 👀:** o parâmetro `attrs` passado para o _widget_ é usado para atribuir um conjunto `chave: valor` à _tag_ que está sendo inserida no _template_. Nesse caso, definimos o tipo do input como data `type: date`, mas poderíamos, adicionalmente, definir uma classe: `class: inputDate`.

Execute o servidor antes e depois da adição do novo _widget_. Essa implementação diminui a probabilidade de _bugs_ relacionados à entrada de dados do tipo data, que precisam ser digitados em um formato específico. Além disso, ainda houve uma melhora na experiência de quem usa o formulário.

|![Print da página home com formulário personalizado](https://content-assets.betrybe.com/prod/ab153ff3-0c1e-4813-acda-57f1d2d8a578-Print%20da%20p%C3%A1gina%20home%20com%20formul%C3%A1rio%20personalizado.png)|
|---|
|Print da página home com formulário personalizado|

## Enviando dados do template para a view

Se você inspecionar o conteúdo HTML do formulário que está renderizado no _template_, verá que, apesar de chamarmos de formulário, não há _tag_ `form` alguma. Isso é um problema, pois queremos enviar os dados inseridos para algum local, então vamos dar um jeito nisso!

O primeiro passo é justamente envolver o formulário em uma _tag_ `form`, indicando o método HTTP e ação que será realizada quando o formulário for submetido.

Além disso, duas outras coisas são necessárias: adicionar uma tag `input` capaz de submeter o formulário (`type: submit`) e adicionar `{% csrf_token %}` logo após a _tag_ `form`.

A _tag_ de _template_ `{% csrf_token %}` é uma estratégia de segurança do _framework_ contra _Cross-site Request Forgery_. Se quiser ler mais sobre esse tipo de ataque, visite esse [site aqui](https://www.ibm.com/docs/pt-br/sva/10.0.0?topic=configuration-prevention-cross-site-request-forgery-csrf-attacks).

```diff
<!-- playlists/templates/music.html -->

{% extends 'base.html' %}

{% block title %}
    Formulário para Nova Música
{% endblock %}

{% block content %}
+    <form method="post" action="">
+        {% csrf_token %}
        {{form.as_p}}
+        <input type="submit" value="Submeter formulário">
+    </form>
{% endblock %}
```

Neste ponto, você já deve ser capaz de submeter o formulário, contudo, esses dados não estão indo para lugar algum. É preciso indicar qual função da camada `view` receberá os dados submetidos pela requisição (`request`).

O parâmetro `request` possui atributos e métodos. Todos os dados que são submetidos por meio de formulários podem ser visualizados no atributo `POST`, na forma de um dicionário. Entretanto, se os dados forem enviados no `body` da requisição, eles podem ser acessados no atributo `body` na forma de _bytes_. Além disso, também é possível identificar o método HTTP utilizado por meio do atributo `method`. Logo mais veremos isso na nossa aplicação!

Adicione a _tag_ de template `{% url %}` para invocar a rota `musics-page` no template `music.html`:

```diff
<!-- playlists/templates/music.html -->

{% extends 'base.html' %}

{% block title %}
    Formulário para Nova Música
{% endblock %}

{% block content %}
+    <form method="post" action="{% url 'musics-page' %}">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Submeter formulário">
    </form>
{% endblock %}
```

Agora, ao submeter o formulário, você está enviando os dados submetidos para a função `music` que, por sua vez, renderiza novamente o template `music.html`.

Para conseguir visualizar no terminal os dados que estão sendo submetidos e o _body_ da requisição, adicione os _prints_ abaixo à função `music` e refaça a submissão do formulário:

```diff
# playlists/views.py

from django.shortcuts import render
from playlists.forms import CreateMusicForm


def music(request):
+    print(request.POST)
+    print(request.body)
+    print(request.method)
    form = CreateMusicForm()
    context = {"form": form}
    return render(request, "music.html", context)
```

Parabéns, você conseguiu passar dados de um _template_ para uma função da camada `view`! 🎉 O próximo passo é usar esse formulário para validar os dados enviados e, em seguida, criar um novo registro no banco!

> **De olho na dica 👀:** sempre que você quiser inspecionar métodos e atributos de uma variável, você pode usar o método `dir`, nativo do Python. Acrescente `print(dir(request))` aos prints da função e veja o que é mostrado no terminal ao submeter o formulário.

## Criando o novo registro

Iremos implementar uma nova função chamada `index`, que recebe no contexto todos os objetos `Music`. Também iremos renderizar um novo template `home.html`, no qual serão colocados na tela todos os objetos criados e um link de redirecionamento para a função `music`.

A implementação de ambos pode ser observada abaixo:

```python
# playlists/views.py

# ...
from playlists.models import Music


def index(request):
    context = {"musics": Music.objects.all()}
    return render(request, "home.html", context)

# ...
```

```html
<!-- playlists/templates/home.html -->

{% extends 'base.html' %}

{% block title %}
    Home Page
{% endblock %}

{% block content %}
    {% for music in musics %}
        <p>{{music}}</p>
    {% endfor %}

    <a href="{% url 'musics-page' %}">Criar nova música</a>
{% endblock %}
```

Registre a função `index` no arquivo `urls.py`:

```diff
# playlists/urls.py

from django.urls import path
+ from playlists.views import music, singer, index


urlpatterns = [
+    path("", index, name="home-page"),
    path("musics/", music, name="musics-page"),
    path("singers/", singer, name="singers-page"),
]
```

Para finalizar o processo de criação, basta implementar a lógica da instanciação e validação de um formulário e, se os dados forem válidos, adicionar o novo registro no banco e redirecionar para o template inicial `home.html`. Usaremos o método `redirect` e passaremos como parâmetro a identificação da rota desejada: `home-page`.

É preciso lembrar que esse processo completo só deve acontecer caso o método HTTP da requisição seja POST. Vale lembrar também que o próprio formulário passado como contexto para o _template_ é capaz de ligar com erros, caso existam.

Observe a implementação da função `music`:

```python
# playlists/views.py

from django.shortcuts import render, redirect
from playlists.forms import CreateMusicForm, CreateSingerForm
from playlists.models import Music


def music(request):
    form = CreateMusicForm()

    if request.method == "POST":
        form = CreateMusicForm(request.POST)

        if form.is_valid():
            Music.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "music.html", context)
```

Agora sim! Você conseguiu criar um novo registro no banco de dados por meio de um formulário! 🎉

Execute o servidor e veja funcionando! `python3 manage.py runserver`
