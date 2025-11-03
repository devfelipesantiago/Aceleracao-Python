from flask import Config
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


@pytest.fixture(autouse=True)
def clear_database():
    # Aqui você pode adicionar código para limpar ou resetar o banco de dados
    # antes de cada teste, se necessário.
    Config.db.mongo_db.drop()
    yield
    # Código para rodar após cada teste, se necessário.
    Config.db.mongo_db.drop()


# A fixture clear_database é marcada com autouse=True, o que significa que ela
# será executada automaticamente antes e depois de cada teste, garantindo que
# o banco de dados esteja limpo para cada teste.
# Note que o código específico para limpar o banco de dados pode variar
# dependendo do banco de dados que você está usando. Aqui, usamos um exemplo
# genérico que pode ser adaptado conforme necessário.
