## O que é WSGI?

A Python Software Foundation (PSF), juntamente com a comunidade Python, desenvolveu o padrão WSGI (Web Server Gateway Interface), que define uma interface padrão para a comunicação entre servidores _web_ e aplicativos Python.

Esse padrão determina como as solicitações HTTP devem ser feitas, como os dados devem ser processados e como as respostas devem ser enviadas de volta ao servidor.

O WSGI é essencial para que as aplicações Python possam interagir de maneira padronizada e eficiente com os servidores _web_.

Por meio desse padrão, o Flask pode retornar _strings_ ou objetos `JSON` a partir de métodos Python, o que possibilita a criação de APIs. Essa mágica é possível graças ao Werkzeug, uma biblioteca que oferece as ferramentas necessárias para implementar o padrão WSGI.

O Werkzeug está incluído na instalação do Flask, tornando todo esse processo transparente para os desenvolvedores.

|![Logotipo Werkzeug](https://content-assets.betrybe.com/prod/538cebd1-3dd0-49d9-a8a3-0984cc30668d-Logotipo%20Werkzeug.png)|
|---|
|Logotipo do Werkzeug.|

## Werkzeug

Werkzeug, palavra que significa “ferramenta” em alemão, é um _kit_ de ferramentas para aplicações _web_ em Python que oferece diversas funcionalidades para o Flask, como rotas de URL, geração de URLs, manipulação de solicitações HTTP, resposta HTTP, suporte a sessões, gerenciamento de arquivos estáticos e muito mais.

Graças a esse _kit_, o Flask obedece ao padrão WSGI mencionado acima, inclusive o servidor de desenvolvimento que estamos utilizando.

## Por que é importante falar sobre isso?

Ao executar uma aplicação Flask, você pode ter se deparado com um aviso semelhante a este:

🔴 `WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.`

Esse aviso é exibido porque o Flask oferece um servidor embutido para uso durante o desenvolvimento, o que facilita a depuração da aplicação. No entanto, é importante destacar que esse servidor embutido não é adequado para ser usado em ambientes de produção. Isso ocorre porque ele não possui a mesma performance e níveis de segurança de um servidor _web_ dedicado.

Para resolver essa questão, é possível configurar o Werkzeug para utilizar um servidor diferente em ambientes de produção. Existem várias opções disponíveis, como uWSGI, Gunicorn, Waitress e mod_wsgi. A escolha entre eles depende do tamanho e da quantidade de requisições de seu aplicativo, sendo que um pode ser mais adequado que outro para determinadas situações.

Para fins de experimentação, vamos escolher o servidor Waitress, que é recomendado para aplicações de pequeno e médio porte devido a sua fácil configuração e utilização.

> Observação: Se você utilizou o proposto na seção, esse servidor já deve estar instalado.

Caso você precise instalar manualmente o Waitress em sua aplicação Flask, adicione a linha `waitress==2.1.2` no final do arquivo `requirements.txt` e, em seguida, instale as dependências novamente.

Copiar

```bash
# Local:
pip install --no-cache-dir -r dev-requirements.txt
# Docker:
docker compose build flask
```

Agora, vamos fazer ajustes no arquivo `app.py` para configurar o uso do servidor Waitress quando a variável de ambiente não estiver definida como ambiente de desenvolvimento.

Com a ajuda da biblioteca `os`, vamos acessar a variável de ambiente `FLASK_ENV`, que é configurada no arquivo `docker-compose`. Com base nessa variável, aplicaremos a seguinte regra: se o valor for definido como `development`, continuaremos a utilizar o servidor _web_ padrão do Flask. No entanto, se o valor for diferente de `development`, utilizaremos o servidor Waitress.

> src/app.py

Copiar

```python
# ...
from os import environ
from waitress import serve

# app = Flask(__name__)

# joke_list = [
# ...
def start_server(host: str = "0.0.0.0", port: int = 8000):
    if environ.get("FLASK_ENV") == "dev":
        # Servidor de desenvolvimento do Kit Werkzeug
        return app.run(debug=True, host=host, port=port)
    else:
        # Este é o waitress, otimizado para produção
        serve(app, host=host, port=port)

# if __name__ == "__main__":
#     start_server()
```

Agora, temos um servidor para o ambiente de desenvolvimento, configurado para nos ajudar a debugar a aplicação. E outro servidor, em produção, otimizado para dar segurança e velocidade.

Antes de prosseguir, é importante se atentar a 2 pontos desse ajuste que fizemos:

1. Quando usamos o servidor de desenvolvimento do `Flask`, o servidor é reiniciado a cada alteração no código. No entanto, quando usamos o `Waitress`, isso não acontece. Portanto, se você fizer alterações no código, precisará reiniciar o servidor manualmente.
2. Como não configuramos nenhum tipo de log para o `Waitress`, não veremos nenhuma mensagem de log no terminal. Mas pode ter tranquilidade: o servidor está funcionando perfeitamente.
