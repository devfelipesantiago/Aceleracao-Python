# API do Jinja2

No conteúdo de hoje nós vimos muitas das ferramentas base do Jinja2, como elas funcionam e como podemos utilizá-las no nosso dia a dia

- `Template` - A classe `jinja2.Template` representa um template carregado a partir de uma string ou arquivo.
- `BaseLoader` - A classe `jinja2.BaseLoader` é uma classe base abstrata da qual outros loaders do Jinja2 podem ser derivados.
- `FileSystemLoader` - A classe `jinja2.FileSystemLoader` é usada para carregar templates de um sistema de arquivos local.
- `DictLoader` - A classe `jinja2.FileSystemLoader` é usada para carregar templates de um dicionário, e outros.
- `Environment` - A classe `jinja2.Environment` é responsável por gerenciar o ambiente de execução para os templates.
- `Filtros` - Vimos o que são, como usar e quais são alguns dos filtros padrões do Jinja2, como o `capitalize`, `upper`, `lower` e `default`.
- `Filtros customizados` - Vimos como criar e como usar filtros customizados como o `convert_date` que nós criamos
- `Exceções` - Vimos o que são e como tratar exceções com os blocos `try-except`, `else` e `finally`, tanto no Python quanto no Jinja2.

O Jinja2 é um mecanismo de template para Python que permite a geração dinâmica de conteúdo HTML, XML ou qualquer outro formato de texto. É amplamente utilizado em frameworks web, como Flask e Django, para separar a lógica de apresentação da lógica de negócios.

A API do Jinja2 abrange um conjunto de classes, métodos e funcionalidades que permitem interagir com o Jinja2 por meio do código Python. Por meio dessa API, é possível carregar e renderizar templates, fornecer variáveis e contextos para os templates, definir filtros e macros personalizados, além de controlar o comportamento do mecanismo de template.

É importante ressaltar que o Jinja2 é instalado por padrão juntamente com o Flask, uma vez que ele desempenha um papel fundamental nesse framework.

Se você deseja trabalhar apenas com o Jinja2 de forma isolada, você pode instalá-lo usando o seguinte comando:

```bash
pip install Jinja2
```

Esse comando instalará o Jinja2 em seu ambiente Python, permitindo que você utilize o mecanismo de template sem depender de outros frameworks como Flask ou Django. Dessa forma, você pode usar o Jinja2 em qualquer projeto Python em que deseje realizar a geração dinâmica de conteúdo.

## Funcionamento do Jinja

> Não é necessário que você memorize todos os passos e processos que serão mencionados a seguir, mas é interessante que você tenha conhecimento de que eles existem. Iremos ver esses passos ao longo do conteúdo e na aplicação que iremos montar, de forma mais orgânica e leve.

O funcionamento do Jinja2 envolve a execução dos seguintes passos básicos:

1. Carregamento do template:

    - O processo se inicia com o carregamento do template de uma fonte específica, como um arquivo, um banco de dados ou mesmo uma string.
    - Esse carregamento é realizado por meio de um “loader”, que tem a função de localizar e carregar o conteúdo do template, podendo esse conteúdo estar armazenado em uma simples variável ou um arquivo HTML.
2. Compilação do template:

    - Após o carregamento, o Jinja2 compila o template em uma representação interna otimizada, conhecida como código de template.
    - Essa compilação transforma o template em uma estrutura de dados que o Jinja2 pode entender e processar de forma eficiente.
3. Criação do ambiente:

    - O próximo passo é criar um ambiente Jinja2. O ambiente é responsável por fornecer a configuração global e os recursos necessários para processar o template.
    - Ele contém informações como os _loaders_ disponíveis, filtros personalizados, funções auxiliares e outras configurações.
4. Renderização do template:

    - Após a configuração do ambiente, o Jinja2 utiliza o código do template e o contexto fornecido para realizar a renderização.
    - O contexto consiste em um dicionário de variáveis e seus respectivos valores, que são utilizados durante a renderização para substituir as partes dinâmicas do template.
    - Durante o processo de renderização, o Jinja2 interpreta as expressões, tags e blocos específicos do Jinja2 presentes no template, substituindo-os pelos valores correspondentes no contexto.
5. Saída do resultado:

    - O resultado final da renderização é uma string que contém o conteúdo resultante.
    - Esse resultado pode ser retornado como uma resposta HTTP em um aplicativo web, gravado em um arquivo ou utilizado de outras formas, dependendo do contexto de uso.

Essa é uma visão geral básica de como o Jinja2 funciona. Para obter mais detalhes sobre o uso do Jinja2 e suas funcionalidades, consulte a [documentação oficial](https://jinja.palletsprojects.com/)

## Classe Jinja2.Template

A API do Jinja2 fornece uma série de classes e funções que permitem interagir com o mecanismo de template Jinja2 em seu código Python. Uma delas é a `Template`

A classe `jinja2.Template` é uma das principais classes na API do Jinja2. Ela representa um template carregado a partir de uma string ou arquivo e fornece métodos para renderizá-lo com um contexto específico.

### Iniciando com Templates

Vamos ver na prática como utilizar a classe `Template`. Criaremos um diretório chamado `conhecendo-jinja` e iniciaremos um ambiente virtual dentro desse diretório:

```bash
mkdir conhecendo-jinja && cd conhecendo-jinja &&
python3 -m venv .venv && source .venv/bin/activate
```

Vamos instalar a biblioteca `Jinja2`:

```bash
pip install Jinja2
```

É possível verificar se a instalação foi bem sucedida com o comando:

```bash
pip freeze
```

A saída deve ser parecida com:

![Retorno pip freeze](https://content-assets.betrybe.com/prod/12a20fa1-3b48-4378-8723-e66bd6aeefe5-Retorno%20pip%20freeze.png)

Agora vamos criar um arquivo chamado `template.py`

```bash
touch template.py
```

Adicionaremos o seguinte código:

```python
from jinja2 import Template

# Carrega um template a partir de uma string
template_string = "Eu sou um {{ nome }}!"
template = Template(template_string)

# Renderiza o template com um contexto específico
output = template.render(nome='template')

# Imprime o resultado
print(output)
```

Execute o arquivo

```bash
python3 template.py
```

A saída deve ser parecida com essa:

![Retorno da execução do arquivo template.py](https://content-assets.betrybe.com/prod/12a20fa1-3b48-4378-8723-e66bd6aeefe5-Retorno%20da%20execu%C3%A7%C3%A3o%20do%20arquivo%20template.py.png)

Neste exemplo, importamos a classe `Template` de dentro da biblioteca `jinja2`, depois criamos uma instância dessa classe passando uma string contendo o conteúdo do template. Em seguida, utilizamos o método `render()` para renderizar o template com um contexto específico. O resultado final é a string `"Eu sou um template!"`.

> O contexto é um dicionário que mapeia nomes de variáveis para valores, nesse caso `{'nome': 'template'}`.

## Renderizando um HTML

Como falamos anteriormente, o `Jinja2` tem a capacidade de renderizar também templates em HTML. Vamos ver como ele faz isso, mas antes vamos criar um arquivo HTML para ser usado de base:

```bash
touch template.html
```

Adicionaremos o seguinte conteúdo ao arquivo `template.html`:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <title>Template</title>
</head>
<body>
    <h1>{{ saudacao }}</h1>
</body>
</html>
```

Vamos fazer algumas alterações ao nosso arquivo `template.py`

```python
# from jinja2 import Template

# # Carrega um template a partir de um arquivo
template_file = open('template.html').read()
template = Template(template_file)

# # Cria um contexto
saudacao = 'Eu sou um template HTML'

# # Renderiza o template com um contexto específico
output = template.render(saudacao=saudacao)

# # Imprime o resultado
# print(output)
```

Execute o arquivo `template.py`

```bash
python3 template.py
```

Saída esperada:

![Retorno da execução do arquivo template.py com saudação no HTML](https://content-assets.betrybe.com/prod/12a20fa1-3b48-4378-8723-e66bd6aeefe5-Retorno%20da%20execu%C3%A7%C3%A3o%20do%20arquivo%20template.py%20com%20sauda%C3%A7%C3%A3o%20no%20HTML.png)

Nesse caso, o conteúdo do arquivo `template.html` é lido e fornecido à classe `Template` para criar uma instância do template. Em seguida, criamos um contexto e utilizamos o método `render()` para renderizar o template com o contexto criado.

Também é possível passar diretamente a string `'Eu sou um template HTML'` para o `render` como valor do contexto `saudacao` (`template.render(saudacao='Eu sou um template HTML')`), obtendo o mesmo resultado.

É interessante utilizar uma variável para inicializar o contexto, uma vez que podemos utilizar um dicionário para armazenar várias informações que desejamos imprimir no nosso template.

Vamos voltar ao nosso `template.html` e adicionar algumas modificações:

```html
<!-- <!DOCTYPE html>
...
<body>
    <h1>{{ saudacao }}</h1> -->
    <h2>{{ informacao }}</h2>
    <p>{{ contexto }}</p>
<!-- </body>
</html> -->
```

Agora vamos ao nosso arquivo `template.py` e fazer algumas modificações nele também

```python
# ...
# template = Template(template_file)

# # Cria um contexto
data = {
    'saudacao': 'Eu sou um template HTML',
    'informacao': 'E essa é uma das formas de se passar múltiplas informações para o template',
    'contexto': 'Isso é possível através da criação de um contexto'
}

# # Renderiza o template com um contexto específico
output = template.render(data)

# # Imprime o resultado
# print(output)
```

Execute o arquivo `template.py`

```bash
python3 template.py
```

Saída esperada:

![Retorno da execução do arquivo template.py com múltiplas frases](https://content-assets.betrybe.com/prod/12a20fa1-3b48-4378-8723-e66bd6aeefe5-Retorno%20da%20execu%C3%A7%C3%A3o%20do%20arquivo%20template.py%20com%20m%C3%BAltiplas%20frases.png)

É importante ressaltar que a classe `jinja2.Template` é apenas uma parte da API do Jinja2. Existem muitas outras classes e recursos disponíveis para manipular templates de maneira mais avançada.

## Classe Jinja2.BaseLoader

Como falado anteriormente, a API do Jinja2 fornece uma série de classes e funções que permitem interagir com o mecanismo de template Jinja2 em seu código Python. Uma delas é a `BaseLoader`

A classe `jinja2.BaseLoader` é uma classe base abstrata na biblioteca Jinja2 que define a interface básica para os loaders de templates. Ela é usada para carregar os templates de suas respectivas origens, como sistema de arquivos, banco de dados, rede, entre outros.

## Iniciando com BaseLoader

Embora `jinja2.BaseLoader` seja uma classe abstrata, ela não pode ser usada diretamente para carregar templates, pois não fornece uma implementação concreta do método `get_source()`. Em vez disso, é necessário derivar uma classe concreta dela e implementar o método `get_source()` para carregar os templates da origem desejada.

Vamos ver na prática como utilizar a classe `Template`. Continuaremos dentro do diretório `conhecendo-jinja`, vamos criar um arquivo chamado `dict_loader.py`:

```bash
touch dict_loader.py
```

Adicionaremos o seguinte código:

```python
from jinja2 import BaseLoader

class DictLoader(BaseLoader):
    def __init__(self, templates):
        self.templates = templates

    def get_source(self, environment, template):
        if template in self.templates:
            source = self.templates[template]
            return source, None, lambda: False
        return
```

Neste exemplo, criamos a classe `DictLoader` que herda de `jinja2.BaseLoader`. No construtor `__init__()`, recebemos um dicionário `templates` que mapeia os nomes dos templates para seus conteúdos.

Em seguida, implementamos o método concreto `get_source()` para carregar o template a partir do dicionário. Seguindo a [documentação da BaseLoader](https://jinja.palletsprojects.com/en/3.1.x/api/#jinja2.BaseLoader), se o template solicitado estiver presente no dicionário devemos retornar uma tupla contendo:

1. o conteúdo do template;
2. nenhuma informação (`None`) de código-fonte adicional;
3. e uma função **lambda** para indicar que o template não é um recurso atualizável.

> **Relembrando 🧠:** Uma função lambda em Python é uma função anônima que pode ser definida de forma concisa e em uma única linha. Ela é útil quando você precisa de uma função simples que não será reutilizada em outros lugares do seu código.

Após criar essa classe de _loader_ personalizado, você pode usá-la para carregar os templates em seu ambiente Jinja2. Por exemplo:

> dict_loader.py

```python
from jinja2 import BaseLoader, Environment

# class DictLoader(BaseLoader):
    # ...

# Configurando o loader personalizado
templates = {
    'index.html': '<h1>Um template usando {{ nome }}!</h1>',
    'about.html': '<p>Este é um exemplo de template Jinja2.</p>'
}
loader = DictLoader(templates)

# Criando um ambiente Jinja2
environment = Environment(loader=loader)

# Carregando um template e renderizando com um contexto
template = environment.get_template('index.html')
output = template.render(nome='BaseLoader')
print(output)
```

Execute o arquivo

```bash
python3 dict_loader.py
```

A saída deve ser parecida com essa:

![Retorno da execução do arquivo dict_loader.py com o template index.html](https://content-assets.betrybe.com/prod/9b48134e-9f1b-43ca-9803-0a7e6d726482-Retorno%20da%20execu%C3%A7%C3%A3o%20do%20arquivo%20dict_loader.py%20com%20o%20template%20index.html.png)

Altere o argumento passado para a função `get_template` de `"index.html"` para `"about.html"` e execute novamente o arquivo. A saída deve ser parecida com essa:

![Retorno da execução do arquivo dict_loader.py com o template about.html](https://content-assets.betrybe.com/prod/9b48134e-9f1b-43ca-9803-0a7e6d726482-Retorno%20da%20execu%C3%A7%C3%A3o%20do%20arquivo%20dict_loader.py%20com%20o%20template%20about.html.png)

Neste exemplo, configuramos o loader personalizado `DictLoader` para carregar os templates a partir de um dicionário e criamos um ambiente Jinja2 através da classe `Environment`. Em seguida, usamos o método `get_template()` para carregar os templates `"index.html"` ou `"about.html"` e renderizá-los com um contexto específico.

## Environment

A classe `jinja2.Environment` é uma parte fundamental da API do Jinja2. Ela representa o ambiente de execução do Jinja2 e contém as configurações globais e os recursos necessários para processar templates.

Ao criar uma instância da classe `Environment`, você pode personalizar o comportamento do Jinja2 para atender às necessidades específicas do seu aplicativo.

Essa classe pode receber alguns parâmetros de inicialização, dentre eles temos o `loader`. Através do parâmetro `loader`, é possível especificar o carregador (loader) que será usado para carregar os templates.

Os loaders podem ser responsáveis por ler os templates de diferentes origens, como o sistema de arquivos, um pacote Python ou até mesmo um banco de dados.

A classe `Environment` nos fornece muitas funções, como por exemplo a função `get_template`, que carrega um template pelo nome através do parâmetro `loader` e retorna um `Template`.

Se você quiser saber mais sobre os parâmetros e as funções da classe `Environment`, dê uma olhada [nesta página](https://jinja.palletsprojects.com/en/3.0.x/api/#jinja2.Environment) da documentação do Jinja2

## Filtros customizados no Jinja2

No Jinja2, existem funções embutidas que permitem transformar ou modificar valores dentro dos templates, essa funções são chamadas de filtros. Eles são usados para realizar manipulações nos dados antes de serem exibidos no output final.

Os filtros são aplicados aos valores usando a sintaxe de pipe `|` após a expressão ou variável a ser filtrada. A função de filtro é chamada com o valor original como argumento e retorna o valor modificado.

Existem alguns filtros que são mais utilizados e/ou difundidos na comunidade, dentre eles estão:

- `capitalize`: Converte o primeiro caractere de uma string em maiúsculo e os demais em minúsculo. Exemplo: `{{ name|capitalize }}`
- `upper`: Converte todos os caracteres de uma string em maiúsculo. Exemplo: `{{ text|upper }}`
- `lower`: Converte todos os caracteres de uma string em minúsculo. Exemplo: `{{ text|lower }}`
- `length`: Retorna o tamanho de uma sequência (string, lista, etc.). Exemplo: `{{ my_list|length }}`
- `default`: Define um valor padrão para ser usado caso a variável seja nula ou vazia. Exemplo: `{{ variable|default("Valor padrão") }}`
- `truncate`: Trunca uma string para um número específico de caracteres. Exemplo: `{{ text|truncate(20) }}`

Vamos ver como aplicar filtros na prática, dentro do diretório `conhecendo-jinja` criaremos um diretório chamado `filters`, um arquivo chamado `filters.html` e um arquivo chamado `filters.py`

```bash
mkdir filters && touch filters/filters.html && touch filters/filters.py
```

Vamos adicionar o seguinte conteúdo ao arquivo `filters/filters.html`:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Filtros</title>
</head>
<body>
    <p>{{ name|capitalize }}</p>
    <p>{{ to_upper|upper }}</p>
    <p>{{ to_lower|lower }}</p>
    <p>{{ my_list|length }}</p>
    <p>{{ variable|default("Valor padrão") }}</p>
    <p>{{ text|truncate(20) }}</p>
</body>
</html>
```

Vamos adicionar o seguinte código ao arquivo `filters/filters.py`:

```python
from jinja2 import Environment, FileSystemLoader

# Configurando um loader
loader = FileSystemLoader('filters')

# Criando um ambiente Jinja2
environment = Environment(loader=loader)

# Carrega um template a partir de um arquivo
template = environment.get_template('filters.html')


# Cria um contexto
data = {
    'name': 'a primeira letra vai ficar maiúscula',
    'to_upper': 'todas as letras vão ficar maiúsculas',
    'to_lower': 'TODAS AS LETRAS VÃO FICAR MINÚSCULAS',
    'my_list': [0, 1, 2, 3, 4, 5],
    'text': 'Esse texto irá ser truncado'
}

# Carregando um template e renderizando com um contexto
output = template.render(data)

# Imprime o resultado
print(output)
```

> **Anota aí 📝:** O `FileSystemLoader` é uma classe fornecida pelo Jinja2 que atua como um _loader_. Essa classe tem a finalidade de carregar o diretório onde os templates estão localizados, templates os quais serão posteriormente utilizados pela função `get_template()`. É importante destacar que o `FileSystemLoader` difere do `BaseLoader` por ser específico para carregar templates a partir de um diretório.

Execute o arquivo `filters/filters.py`

```bash
python3 filters/filters.py
```

Saída esperada:

![Retorno da execução do arquivo filters.py 01](https://content-assets.betrybe.com/prod/bfa8fad1-8b9b-477a-91ca-b502bf25097d-Retorno%20da%20execu%C3%A7%C3%A3o%20do%20arquivo%20filters.py%2001.png)

Neste exemplo, no arquivo `filters.py`, utilizamos a classe `FileSystemLoader` para carregar o diretório onde o template que desejamos utilizar está localizado. Em seguida, criamos uma instância da classe `Environment`, passando o resultado do `FileSystemLoader` como argumento para o parâmetro `loader`. Posteriormente, buscamos o template chamado `filters.html` e criamos um contexto no formato de dicionário, contendo os nomes e valores das variáveis que serão utilizadas no arquivo `filters.html`. Por fim, realizamos a renderização do template.

No arquivo `filters.html`, criamos um template no qual passamos as variáveis e especificamos quais filtros devem ser aplicados a cada uma delas.

## Criando filtros customizados

O Jinja2 permite a criação de filtros personalizados para manipular e formatar dados nos templates. A criação de filtros personalizados no Jinja2 é bastante flexível e pode ser feita de maneira simples.

Os filtros customizados (ou personalizados) devem ser implementados como funções, assim como os filtros padrão. Assim como os filtros padrão, os filtros personalizados também devem receber pelo menos um parâmetro, que será a informação passada na chamada do filtro dentro do template.

Vamos a prática, criaremos o arquivo `filters/custom_filters.py`:

```bash
touch filters/custom_filters.py
```

Adicionaremos o seguinte código ao arquivo `filters/custom_filters.py`:

```python
from datetime import datetime

def convert_date(date):
    data_obj = datetime.strptime(date, "%Y-%m-%d")
    return data_obj.strftime("%d/%m/%Y")
```

> **De olho na dica 👀:** As funções `strptime` e `strftime` são funções de formatação e manipulação de datas, caso queira saber mais sobre elas você pode olhar na documentação sobre a [strptime](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime) e a [strftime](https://docs.python.org/3/library/datetime.html#datetime.date.strftime).

Em seguida iremos adicionar o nosso novo filtro os filtros no nosso ambiente, no arquivo `filters/filters.py`

```python
# from jinja2 import Environment, FileSystemLoader
from custom_filters import convert_date
# Importamos o filtro customizado

#...

# environment = Environment(loader=loader)
environment.filters['convert_date'] = convert_date
# Adicionamos o filtro customizado ao ambiente, poderia ter sido dado qualquer nome ao nosso filtro
# O nome que for passado dentro dos colchetes como uma string, é o nome que irá ser chamado no template

# ...

# data = {
#     'name': 'a primeira letra vai ficar maiúscula',
#     'to_upper': 'todas as letras vão ficar maiúsculas',
#     'to_lower': 'TODAS AS LETRAS VÃO FICAR MINÚSCULAS',
#     'my_list': [0, 1, 2, 3, 4, 5],
#     'text': 'Esse texto irá ser truncado',
      'date': '2023-05-21',
# }
# Adicionamos a nova informação ao contexto
```

Após importar o novo filtro customizado, adiciona-lo ao ambiente e adicionar a nova variável ao contexto, vamos modificar o nosso arquivo `filters/filters.html` para utilizar a nova variável e chamar o nosso filtro:

```html
<!-- ... -->
    <!-- <p>{{ text|truncate(20) }}</p> -->
    <p>{{ date|convert_date }}</p>
<!-- </body>
</html> -->
```

Execute o arquivo `filters/filters.py`

```bash
python3 filters/filters.py
```

Saída esperada:

![Retorno da execução do arquivo filters.py 02](https://content-assets.betrybe.com/prod/bfa8fad1-8b9b-477a-91ca-b502bf25097d-Retorno%20da%20execu%C3%A7%C3%A3o%20do%20arquivo%20filters.py%2002.png)

## Filtros com mais de um parâmetro

Conforme mencionado anteriormente, ao chamar um filtro dentro de um template, a informação anterior ao pipe `|` é passada automaticamente como o primeiro parâmetro para a função do filtro. No entanto, caso seja necessário criar um filtro com mais de um parâmetro, isso também é possível. Vamos ver como fazer isso.

No arquivo `filters/custom_filters.py` vamos adicionar o seguinte código:

```python
def replace_text(string, old_text, new_text):
    return string.replace(old_text, new_text)
```

> A função `replace_text` tem a finalidade de substituir uma palavra ou trecho por outra palavra ou trecho. Em outras palavras, ela substitui um texto antigo (`old_text`) por um texto novo (`new_text`) e retorna a `string` modificada como resultado.

Vamos agora adicionar nosso novo filtro ao nosso ambiente, no arquivo `filters/filters.py`:

```python
# from jinja2 import Environment, FileSystemLoader
from custom_filters import convert_date, replace_text
# Importamos o filtro customizado

#...

# environment.filters['convert_date'] = convert_date
environment.filters['replace_text'] = replace_text
# Adicionamos o filtro customizado ao ambiente, poderia ter sido dado qualquer nome ao nosso filtro
# O nome que for passado dentro dos colchetes como uma string, é o nome que irá ser chamado no template

# ...

# data = {
#     'name': 'a primeira letra vai ficar maiúscula',
#     'to_upper': 'todas as letras vão ficar maiúsculas',
#     'to_lower': 'TODAS AS LETRAS VÃO FICAR MINÚSCULAS',
#     'my_list': [0, 1, 2, 3, 4, 5],
#     'text': 'Esse texto irá ser truncado',
#     'date': '2023-05-21',
# }
# Adicionamos a nova informação ao contexto
```

> Não adicionamos uma nova variável, vamos usar uma que já temos

Agora vamos adicionar uma nova tag ao nosso arquivo `filters/filters.html` e usar o nosso novo filtro:

```html
<!-- ... -->
    <!-- <p>{{ date|convert_date }}</p> -->
        <p>{{ text|replace_text("truncado", "trocado") }}</p>
<!-- </body>
</html> -->
```

Execute o arquivo `filters/filters.py`

```bash
python3 filters/filters.py
```

Saída esperada:

![Retorno da execução do arquivo filters.py 03](https://content-assets.betrybe.com/prod/bfa8fad1-8b9b-477a-91ca-b502bf25097d-Retorno%20da%20execu%C3%A7%C3%A3o%20do%20arquivo%20filters.py%2003.png)

Neste exemplo, podemos observar que, ao utilizar nosso filtro, a informação contida na variável `text` é utilizada como argumento para o parâmetro `string` em nosso filtro `replace_text`. A palavra “truncado” é passada como argumento para o parâmetro `old_text`, e a palavra “trocado” é passada como argumento para o parâmetro `new_text`. Essa forma de passar argumentos é conhecida como passagem de argumentos posicional. No entanto, também é possível realizar a passagem de argumentos de forma nominal.

Vamos alterar a chamada do nosso filtro no arquivo `filters/filters.html`:

```html
<!-- ... -->
    <!-- <p>{{ date|convert_date }}</p> -->
        <p>{{ text|replace_text(new_text="trocado", old_text="truncado") }}</p>
<!-- </body>
</html> -->
```

Após executar o arquivo `filters/filters.py` a saída deve permanecer a mesma.

Em funções que possuem muitos parâmetros, a ordem na qual você passa os argumentos se torna indiferente ao utilizar o nome do parâmetro seguido de um valor como argumento para a chamada da função. Isso é extremamente útil, pois permite maior flexibilidade e facilidade na passagem dos valores, independentemente da sequência original dos parâmetros.

## Tratamento de exceções no Jinja2

Assim como o Python, o Jinja2 também possui sua forma de tratar exceções. No Jinja2 é possível a utilização do bloco `try-except` para capturar exceções e fornecer um tratamento adequado.

## Relembrando a sintaxe do Python para exceções

Antes de avançarmos com o Jinja2, vamos relembrar a sintaxe do Python para tratamento de exceções:

Copiar

```python
try:
    # Código que pode gerar exceções
    resultado = 10 / 0  # Exemplo de divisão por zero
except ZeroDivisionError:
    # Trecho de tratamento específico para a exceção ZeroDivisionError
    print("Erro: Divisão por zero não é permitida.")
except Exception as e:
    # [opcional] Trecho de tratamento genérico para todas as outras exceções
    print("Erro: ", str(e))
else:
    # [opcional] Trecho executado se nenhuma exceção for levantada
    print("Resultado:", resultado)
finally:
    # [opcional] Trecho sempre executado, independentemente de exceções
    print("Fim do programa.")
```

Além disso, vale relembrar a expressão `raise` utilizada para lançar uma exceção intencionalmente. Por exemplo:

Copiar

```python
if x < 0:
    raise ValueError("O valor de x não pode ser negativo.")
```

## Tratando exceções no Jinja2

Para começar o nosso tratamento de exceções do Jinja2, vamos criar um arquivo chamado `templates_exceptions.py` e adicionar o seguinte conteúdo:

> templates_exceptions.py

Copiar

```python
from jinja2 import TemplateNotFound, Environment
from dict_loader import DictLoader

templates = {
    'index.html': '<h1>Um template sem exceções!</h1>',
    'about.html': '<p>Este é um exemplo de template Jinja2.</p>'
}

try:
    loader = DictLoader(templates)
    environment = Environment(loader=loader)
    template = environment.get_template('random.html')
except TemplateNotFound:
    print('Erro: Template não encontrado')
except Exception as e:
    print("Erro: ", str(e))
else:
    print(template.render())
finally:
    print("Fim do programa.")
```

No código anterior, nós utilizamos a classe `DictLoader` que criamos anteriormente para criar um `loader` do templates que criamos neste arquivo e após criarmos um ambiente com esse `loader`, tentamos acessar um template “random.html” inexistente no nosso ambiente.

Adicionamos alguns tratamentos de exceção, vamos ver o que acontece.

Execute o arquivo `templates_exceptions.py`:

Copiar

```bash
python3 templates_exceptions.py
```

A saída deve ser parecida com essa:

![Erro NoneType object lançado](https://content-assets.betrybe.com/prod/fc77931f-9fcb-4341-bfcc-3f9b338873cb-Erro%20NoneType%20object%20lan%C3%A7ado.png)

> O erro `cannot unpack non-iterable NoneType object` é disparado quando tentamos atribuir a algo um objeto do tipo None.

Como o nosso template não existe e se dermos uma olhada na nossa classe `DictLoader`, veremos que setamos pra que ela retorne um objeto do tipo `None` caso o template não seja encontrado. Vamos então fazer com que a nossa classe `DictLoader` lance uma exceção adequada.

> dict_loader.py

Copiar

```python
from jinja2 import BaseLoader, Environment, TemplateNotFound

class DictLoader(BaseLoader):
    def __init__(self, templates):
        self.templates = templates

    def get_source(self, environment, template):
        if template in self.templates:
            source = self.templates[template]
            return source, None, lambda: False
        raise TemplateNotFound(template)

# ...
```

Execute o arquivo `templates_exceptions.py`:

Copiar

```bash
python3 templates_exceptions.py
```

A saída deve ser parecida com essa:

![Erro Template não encontrado](https://content-assets.betrybe.com/prod/fc77931f-9fcb-4341-bfcc-3f9b338873cb-Erro%20Template%20n%C3%A3o%20encontrado.png)

Agora nossa classe `DictLoader` lança um erro condizente com a aplicação dela e nós podemos o tratar de forma específica.

Vamos voltar ao nosso arquivo `templates_exceptions.py` e passar um template existente para a função `get_template()`:

Copiar

```python
# ...
    template = environment.get_template('index.html')
# ...
```

Execute o arquivo `templates_exceptions.py`:

Copiar

```bash
python3 templates_exceptions.py
```

A saída deve ser parecida com essa:

![Renderização do template](https://content-assets.betrybe.com/prod/fc77931f-9fcb-4341-bfcc-3f9b338873cb-Renderiza%C3%A7%C3%A3o%20do%20template.png)

Como nenhuma exceção é disparada, o template é renderizado sem problemas.

O Jinja2 possui outros tipos de exceções que podem ser lançadas, se quiser saber mais sobre elas, leia [essa](https://jinja.palletsprojects.com/en/3.0.x/api/#exceptions) página da documentação.
