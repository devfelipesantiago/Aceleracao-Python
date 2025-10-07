from faker import Faker


faker = Faker(locale="pt_BR")


def data_faker():
    print(faker.name())
    print(faker.phone_number())
    print(faker.cpf())


data_faker()

# A seed (semente) é um valor que serve como base para a geração de números
# aleatórios. Se a mesma seed for usada, teremos sempre a mesma sequência de
# resultados. Por padrão, o Faker usa o timestamp atual do sistema e por isso
# cada execução resulta em valores diferentes.

Faker.seed(0)  # repare que usamos a classe 'Faker', e não a instância 'faker'

# O restante do código permanece igual
faker.email()  # cria um e-mail falso;
faker.password()  # cria uma senha falsa;
faker.address()  # cria um endereço falso;
faker.credit_card_number()  # cria um número de cartão de crédito falso;
faker.phone_number()  # cria um número de telefone falso;
faker.company()  # cria um nome de empresa falso;
faker.date()  # cria uma data falsa;
faker.cpf()  # cria um CPF falso.


# Usando o Pytest com o Faker


def test_faker_email(faker):
    fake_email = faker.email()
    assert isinstance(fake_email, str)
    assert "@" in fake_email
    assert "." in fake_email
