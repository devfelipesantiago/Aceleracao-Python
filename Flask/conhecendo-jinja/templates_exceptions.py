from jinja2 import Template, TemplateNotFound, Environment
from dict_loader import DictLoader

templates = {
    "index.html": "<h1>Um template sem exceções!</h1>",
    "about.html": "<p>Este é um exemplo de template Jinja2.</p>",
}

try:
    loader = DictLoader(templates)
    environment = Environment(loader=loader)
    template = environment.get_template("index.html")
except TemplateNotFound:
    print("Erro: Template não encontrado")
except Exception as e:
    print("Erro: ", str(e))
else:
    print(template.render())
finally:
    print("Fim do programa.")


# Crie uma função que recebe uma lista de nomes e usa o Jinja2 para renderizar um
# template que exiba todos os nomes em uma lista numerada
def render_names(names: list):
    template_string = Template("Nomes: {% for name in names %}{{ name }} {% endfor %}")
    template = template_string.render(names=names)
    print(template)


render_names(["Alice", "Bob", "Charlie"])


# Crie uma função que utilize o Jinja2 para renderizar um template HTML que
# exiba uma tabela com informações sobre produtos. A função deve receber uma
# lista de dicionários, onde cada dicionário representa um produto com as chaves
# “nome”, “preco” e “estoque”.
def render_products_table(products: list):
    template = Template(
        """
    <table>
        <thead>
            <tr>
                <th>Nome</th>
                <th>Preço</th>
                <th>Estoque</th>
            </tr>
        </thead>
        <tbody>
            {% for product in products %}
            <tr>
                <td>{{ product.nome }}</td>
                <td>{{ product.preco }}</td>
                <td>{{ product.estoque }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    """
    )
    rendered = template.render(products=products)
    print(rendered)


# Exemplos de uso das funções
produtos = [
    {"nome": "Produto A", "preco": 10.99, "estoque": 100},
    {"nome": "Produto B", "preco": 5.49, "estoque": 50},
    {"nome": "Produto C", "preco": 20.00, "estoque": 75},
]
render_products_table(produtos)


# Escreva uma função que utilize o Jinja2 para renderizar um template HTML que exiba um formulário de contato. O template deve conter campos para nome, e-mail e mensagem. A função deve receber os valores preenchidos pelo usuário e renderizar o template com esses valores.
def render_contact_form(name: str, email: str, message: str):
    template = Template(
        """
    <form>
        <label for="name">Nome:</label>
        <input type="text" id="name" name="name" value="{{ name }}"><br><br>
        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email" value="{{ email }}"><br><br>
        <label for="message">Mensagem:</label><br>
        <textarea id="message" name="message">{{ message }}</textarea><br><br>
        <input type="submit" value="Enviar">
    </form>
    """
    )
    rendered = template.render(name=name, email=email, message=message)
    print(rendered)


# Exemplo de uso da função
render_contact_form("Felipe", "felipe@mail.com", "Olá, gostaria de mais informações.")
