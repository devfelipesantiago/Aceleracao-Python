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

## Formulários de modelos (ModelForm)

Agora que você já compreende como funcionam os formulários, será apresentado um outro tipo de formulário, muito útil para quando se possui um modelo que tem muitos atributos obrigatórios para a criação de um novo registro.

Pode até ser que você já tivesse se questionado quanto à isso, mas imagine: você tem um modelo que tem 10 atributos necessários para a criação de um novo registro, você precisaria fazer a implementação de cada um desses atributos no modelo e depois “repetir” todos os atributos no formulário de criação. Isso não parece muito eficiente, e se fossem 20, 30 ou 50 atributos? 😵‍💫

O `ModelForm` tem em sua implementação uma maneira para lidar com esse tipo de problema que foi mencionado. Ele é um formulário que usa como base um modelo já criado, no qual você pode explicitar os campos que deseja que apareçam para a pessoa usuária.

## `ModelForm` na prática

Usando como base o projeto construído até aqui, você vai implementar o primeiro `ModelForm` que será usado para a criação de novos registros de `Music`. Comece uma nova classe com o nome `CreateMusicModelForm` e faça a herança de `form.ModelForm`. Além disso, para fazer esse formulário funcionar corretamente, será necessário implementar a classe `Meta` dentro da classe `CreateMusicModelForm` (Isso mesmo, uma classe dentro da outra 🤯) e nessa segunda classe implementar os atributos: `model`, `fields`, `labels` e `widgets`.

- O atributo `model` é usado para indicar o modelo que será usado como base, e recebe o nome da classe do modelo.
- O atributo `fields` pode receber a string `__all__` ou uma lista com os nomes dos atributos do modelo que você deseja que apareçam no formulário, sendo que a primeira opção faz com que todos os atributos apareçam.
- O atributo `labels` recebe um dicionário onde as chaves são os atributos do modelo e os valores são suas respectivas `labels` personalizadas.
- O atributo `widgets` recebe um dicionário onde as chaves são os atributos do modelo e os valores são os respectivos `widgets` que serão visualizados. É no campo de `widgets` que você pode personalizar um valor inicial para o atributo do modelo.

Veja a implementação como fica:

```python
# playlists/forms.py
from playlists.models import Music

# ...

class CreateMusicModelForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = "__all__"
        labels = {
            "name": "Nome da música",
            "recorded_at": "Data de gravação",
            "length_in_seconds": "Duração em segundos",
        }
        widgets = {
            "recorded_at": forms.DateInput(
                attrs={"type": "date", "value": "2023-07-06"}
            )
        }
```

Com o novo formulário implementado basta fazer a substituição na função `create_music` dentro do arquivo `views.py`.

```python
# playlists/views.py
def create_music(request):
    # form = CreateMusicForm()
    form = CreateMusicModelForm()

    if request.method == "POST":
        # form = CreateMusicForm(request.POST)
        form = CreateMusicModelForm(request.POST)

        if form.is_valid():
            Music.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "index.html", context)
```

Você verá que o formulário já estará funcionando 🤩, inclusive, as validações. Se lembra de quando foi falado que seria útil indicar validações para o campo no próprio modelo? Pois é, esse momento é agora. O `ModelForm` já estrutura seus campos inserindo as validações. Tente criar uma música com duração maior que 3600 e verá a mensagem na tela.

Agora sim! O `ModelForm` está idêntico ao `Form` construído anteriormente. É importante retomar o ponto que não há implementação certa ou errada nesse cenário, tudo depende da aplicação que será construída. Por exemplo, se os nomes padrões fossem bons o suficiente para a aplicação, seguir com a implementação da `ModelForm` seria mais interessante e pouparia algumas linhas de código na aplicação.

## Relacionamento de Modelos

Já somos capazes de criar novos registros de músicas e pessoas cantoras. Entretanto, ainda não temos como identificar quais são as músicas de uma pessoa cantora, ou mesmo quem canta determinada música. O que acha de fazer um _upgrade_ nos modelos para resolver isso?

Como mencionado no começo do conteúdo de hoje, os modelos que estão sendo usados possuem vínculos que ainda não foram estabelecidos, estes vínculos são os relacionamentos que temos entre as tabelas.

Para recordar, os modelos usados até o momento são `Singer`, `Music` e `Playlist`

Bora estabelecer os vínculos entre nossos modelos?

## Relacionamento 1 para N

Refletindo sobre os modelos acima, é possível perceber que essa relação se encaixa bem com os modelos `Singer` <1:N> `Music`, dado que uma mesma pessoa cantora pode ter várias músicas, certo?.

Ao se analisar a implementação dos modelos acima, se nota que nenhum dos campos descritos é uma chave primária. Quando não criamos esse campo explicitamente o Django, automaticamente, cria uma nova coluna para cada modelo, chamada `id`, que será a chave primária, caso algum dos campos seja designado como chave primária (`primary_key = True`), o Django não criará a coluna `id`.

Para criar o relacionamento entre os modelos `Singer` e `Music`, será utilizado o campo `models.ForeignKey` no modelo `Music`, onde será implementado que uma música pode possuir apenas uma pessoa cantora. Dessa forma, se `N` músicas diferentes referenciam a mesma pessoa cantora, podemos notar a relação `Singer` <1:N> `Music`.

No campo `models.ForeignKey` será necessário passar o modelo a ser referenciado e logo em seguida outros dois parâmetros: `on_delete`, que define o que acontecerá com os registros que estão associados ao registro que está sendo excluído e `related_name`, que será um atributo do modelo referenciado para permitir o acesso no sentido inverso do relacionamento.

Além disso, se existirem registros no banco de dados, será necessário definir um valor padrão para que as colunas adicionais sejam preenchidas. Algumas estratégias que podem ser usadas:

- Criar um objeto que representará o valor padrão e passar seu `id` como valor padrão. (Usaremos essa aqui)
- Permitir que a coluna seja nula e, posteriormente, preencher os valores.
- Ou caso ainda esteja em fase de desenvolvimento, apagar o banco e as migrações e criar tudo novamente.

Crie um objeto do tipo `Singer` usando o terminal interativo do Django `python3 manage.py shell`:

```python
from playlists.models import Singer


default = Singer.objects.create(name="Pessoa desconhecida")  # Retorna o objeto criado <Singer: Pessoa desconhecida>

default.id # Retorna o id do objeto criado, 2, por exemplo
```

Agora, veja como fica a classe `Music` com o relacionamento:

```python
# playlists/models.py
from django.db import models
from playlists.validators import validate_music_length,


class Music(models.Model):
    name = models.CharField(max_length=50)
    recorded_at = models.DateField()
    length_in_seconds = models.IntegerField(validators=[validate_music_length])
    singer = models.ForeignKey(
        Singer,
        on_delete=models.CASCADE,
        related_name="musics",
        default=2, # Se não houver o objeto com esse id em seu banco você terá um erro ao criar um objeto Music
    )

    def __str__(self):
        return self.name
```

> **De olho na dica 👀:** Para o parâmetro `on_delete` existem algumas opções de valor já implementadas pelo Django dentro de `models`. Você encontra essas opções na [documentação oficial](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ForeignKey.on_delete).

Com a implementação acima, o modelo `Music` referencia o modelo `Singer`. Já que modificamos o modelo é necessário aplicar as migrações para o banco `python3 manage.py makemigrations` e `python3 manage.py migrate`.

Na prática, será criada uma coluna adicional na tabela `music` com o nome `singer_id` que armazenará a chave primária do registro da tabela `singer` que está sendo referenciado, independentemente se essa chave primária é um `id` ou não. Além disso, foi usada a configuração `on_delete=models.CASCADE`, indicando que, caso o registro da tabela `singer` seja excluído, todos os registros da tabela `music` que possuem o `singer_id` igual ao `id` do registro excluído, também serão excluídos.

Um ponto importante a ser observado é que o atributo `singer` da classe `Music` precisa receber um objeto do tipo `Singer` para ser criado e não um `id` ou qualquer outra chave primária. O ORM do Django se encarrega da tarefa de, a partir do objeto `Singer`, escrever a chave primária no banco de dados e, ao fazer o resgate do banco, resgatar o objeto `singer` a partir do `id` registrado no banco.

Na prática, através de um objeto `Music` podemos acessar o objeto `Singer` através do atributo `singer`. Já através de um objeto `Singer`, podemos acessar todos os objetos `Music` associados à ele através do atributo `musics`, definido em `related_name` do relacionamento e, em seguida, usando o método `all()`.

Observe o exemplo abaixo do relacionamento `1:N` para entender melhor essa relação:

```python
from playlists.models import Music, Singer

corey = Singer.objects.create(name="Corey Taylor") # cria objeto Singer com id = 1 e salva em corey

music_1 = Music.objects.create(name="Snuff", recorded_at="2008-06-17", length_in_seconds=270, singer=corey) # cria objeto Music com id = 1 e salva em music_1

music_2 = Music.objects.create(name="Through Glass", recorded_at="2006-07-01", length_in_seconds=240, singer=corey) # cria objeto Music com id = 2 e salva em music_2

music_1.singer # retorna o objeto Singer associado ao objeto Music music_1
# saída: <Singer: Corey Taylor>

music_2.singer # retorna o objeto Singer associado ao objeto Music music_2
# saída: <Singer: Corey Taylor>

corey.musics.all() # retorna todos os objetos Music associados ao objeto Singer corey
# saída: <QuerySet [<Music: Snuff>, <Music: Through Glass>]>
```

## Relacionamento N para N

O relacionamento N para N representa uma relação onde um registro de uma tabela pode estar associado a vários registros de outra tabela e vice-versa. No caso aqui, podemos fazer transpor essa relação para os modelos `Music` e `Playlist`, dado que uma música pode estar em várias playlists e uma playlist pode ter várias músicas.

Para implementar esse relacionamento no Django, será usado o campo `models.ManyToManyField`, que recebe o modelo a ser referenciado e o parâmetro `related_name`, com o mesmo intuito anterior, ser possível fazer o acesso reverso ao modelo que está sendo referenciado.

```python
# playlists/models.py
class Playlist(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    musics = models.ManyToManyField("Music", related_name="playlists")

    def __str__(self):
        return self.name
```

O único motivo pelo qual o modelo `Music` se encontra entre aspas, como se fosse uma string, no parâmetro `models.ManyToManyField` é que, no momento da criação do modelo `Playlist`, o modelo `Music` ainda não foi declarado. Dessa forma, o Django busca pelo modelo `Music` apenas depois que todos os modelos forem declarados.

No Django, quando um relacionamento `N:N` é criado, o atributo responsável por esse relacionamento se torna uma espécie de `set` que pode receber objetos do tipo do modelo referenciado. Assim, é possível adicionar, usando o método `add()`, ou remover, usando o método `remove()` objetos do atributo de relacionamento.

Uma vez que uma música é adicionada à uma playlist, é preciso salvar novamente a playlist para que as atualizações sejam refletidas no banco de dados. Por essa razão, pode-se implementar métodos que encapsulam essa lógica e facilitam o gerenciamento dos objetos. Observe:

```python
# playlists/models.py
from django.db import models


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

Assim, todos os objetos do tipo `Playlist` serão capazes de usar os métodos `add_music()` e `remove_music()` que facilitam a adição e remoção de músicas de uma playlist. Para conseguir visualizar todas as músicas de uma playlist, basta acessar o atributo `musics` do objeto `Playlist` e, em seguida, usar o método `all()`. Já, se o intuito é visualizar todas as playlists que uma música está associada, basta acessar o atributo `playlists` do objeto `Music`, também definido em `related_name` do relacionamento e, em seguida, usar o método `all()`.

Novamente, foram feitas alterações nos modelos e para que sejam observadas no banco, é preciso criar e executar as migrações `python3 manage.py makemigrations` e `python3 manage.py migrate`. Observe o exemplo abaixo do relacionamento `N:N` para entender melhor essa relação:

```python
from playlists.models import Music, Playlist

music_1 = Music.objects.get(id=1) # retorna objeto Music com id = 1 e salva em music_1

music_2 = Music.objects.get(id=2) # cria objeto Music com id = 2 e salva em music_2

playlist_1 = Playlist.objects.create(name="Codando na Paz", is_active=True) # cria objeto Playlist com id = 1 e salva em playlist_1

playlist_2 = Playlist.objects.create(name="Bora Treinar", is_active=True) # cria objeto Playlist com id = 2 e salva em playlist_2

playlist_1.musics.all() # retorna todos os objetos Music associados ao objeto Playlist
# saída: <QuerySet []>

playlist_2.musics.all() # retorna todos os objetos Music associados ao objeto Playlist
# saída: <QuerySet []>

playlist_1.add_music(music_1) # adiciona objeto Music music_1 ao objeto Playlist

playlist_1.musics.all() # retorna todos os objetos Music associados ao objeto Playlist
# saída: <QuerySet [<Music: Snuff>]>

playlist_2.add_music(music_1) # adiciona objeto Music music_1 ao objeto Playlist

playlist_2.musics.all() # retorna todos os objetos Music associados ao objeto Playlist
# saída: <QuerySet [<Music: Snuff>]>

playlist_2.add_music(music_2) # adiciona objeto Music music_2 ao objeto Playlist

playlist_2.musics.all() # retorna todos os objetos Music associados ao objeto Playlist
# saída: <QuerySet [<Music: Snuff>, <Music: Through Glass>]>

music_1.playlists.all() # retorna todos os objetos Playlist associados ao objeto Music
# saída: <QuerySet [<Playlist: Codando na Paz>, <Playlist: Bora Treinar>]>

music_2.playlists.all() # retorna todos os objetos Playlist associados ao objeto Music
# saída: <QuerySet [<Playlist: Bora Treinar>]>
```

## Como ficam os formulários agora?

Na última implementação realizada dos formulários, foi utilizada a classe `ModelForm` que, automaticamente, cria os campos do formulário com base nos campos do modelo. Você chegou a visualizar como ficou o formulário depois que as alterações de relacionamento foram feitas? Se não, dê uma olhada agora:

|![Print do formulário com novo campo](https://content-assets.betrybe.com/prod/db9c19f7-8bdb-4f8a-92f1-58a4232e659d-Print%20do%20formul%C3%A1rio%20com%20novo%20campo.png)|
|---|
|Print do formulário com novo campo|

O nome que designa o novo campo ainda não foi personalizado mas, sem alterar nada da implementação do formulário, temos um novo campo funcional que já resgata todos os objetos do tipo `Singer` do banco e coloca na lista de seleção.

Caso houvesse a intenção de mostrar apenas alguns dos objetos `Singer`, seria possível personalizar o _widget_ do campo `singers` para que ele fosse um `form.Select` passando o parâmetro `choices` com o valor de uma lista de tuplas, onde cada tupla contém, respectivamente, o valor a ser submetido no formulário e o valor exibido para a pessoa usuária. Observe:

```python
# music/forms.py
class CreateMusicModelForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Nome da música"
        self.fields["recorded_at"].label = "Data de gravação"
        self.fields["recorded_at"].widget = forms.DateInput(
                attrs={"type": "date"})
        self.fields["recorded_at"].initial = "2023-07-06"
        self.fields["length_in_seconds"].label = "Duração em segundos"
        self.fields["singer"].label = "Artista"
        self.fields["singer"].widget = forms.Select(
            choices=[
                (singer.id, singer.name)
                for singer in Singer.objects.filter(name__contains="a")
            ]
        )
```

Com a modificação acima, o campo `singer` do formulário passa a exibir os nomes dos objetos `Singer` que possuem a letra “a” no nome, entretanto, ao submeter o formulário não será o nome do objeto que será passado adiante, mas sim o seu `id`.

Execute o servidor e veja as alterações feitas em funcionamento: `python3 manage.py runserver` e acesse [localhost:8000/musics](localhost:8000/musics).
