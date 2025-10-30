import pytest
from app import app


# Fixtures usa o test_client para simular requisições à aplicação
@pytest.fixture
def client():
    return app.test_client()


# Essa fixture faz uma requisição GET para a rota raiz ("/") e usa o client
# definido acima para isso.
@pytest.fixture
def response(client):
    return client.get("/")


# No código acima definimos 2 fixtures (funções que rodam antes e/ou depois
# dos testes) para o nosso teste client que nos permite simular requisições à
# aplicação e response que faz a requisição para a aplicação e nos fornece o
# retorno dessa requisição.
