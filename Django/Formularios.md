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
