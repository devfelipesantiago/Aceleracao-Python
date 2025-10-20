# 🐍 Guia Rápido: Manipulação de JSON e CSV em Python

A manipulação de JSON (JavaScript Object Notation) e CSV (Comma Separated Values) é uma tarefa comum em Python. O módulo `json` é usado para serializar (converter objetos Python em strings JSON) e desserializar (converter strings JSON em objetos Python), ideal para APIs e configurações. O módulo `csv` é especializado em trabalhar com arquivos de valores separados, muito usado em planilhas e data warehousing.

## 1. Manipulação de Dados JSON (`import json`)

O módulo `json` lida principalmente com a conversão entre tipos de dados Python (`dict`, `list`, `str`, `int`, etc.) e a notação de string JSON.

| **Método**           | **Descrição**                                                                                  | **Uso Principal**                                                                     |
| -------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `json.dumps(obj)`    | **Dump String:** Serializa um objeto Python (`obj`) em uma **string** formatada em JSON.       | Converter dados Python para enviar pela rede (API) ou armazenar em um campo de texto. |
| `json.loads(s)`      | **Load String:** Desserializa uma **string** formatada em JSON (`s`) em um objeto Python.      | Receber dados de uma API ou ler uma string JSON de uma variável.                      |
| `json.dump(obj, fp)` | Serializa um objeto Python (`obj`) e **escreve** o resultado diretamente em um arquivo (`fp`). | Escrever dados Python diretamente em um arquivo `.json`.                              |
| `json.load(fp)`      | **Lê** um arquivo JSON aberto (`fp`) e o desserializa em um objeto Python.                     | Ler dados de um arquivo `.json`.                                                      |

### Exemplo de Código: JSON

```Python
import json

# 1. Objeto Python que será convertido para JSON (Serialização)
dados_python = {
    "nome": "Teacher Python",
    "idade": 3,
    "linguagens": ["Python", "SQL", "Javascript"],
    "ativa": True,
    "configuracao": None
}

# --- Métodos DUMPS e LOADS (Trabalhando com strings na memória) ---

# 1.1. json.dumps(obj): De Python para String JSON
json_string = json.dumps(dados_python, indent=4) # indent=4 para formatar (pretty-print)
print("--- 1.1 json.dumps() ---")
print(f"Tipo de retorno: {type(json_string)}")
print(f"Retorno:\n{json_string}")

# 1.2. json.loads(s): De String JSON para Python
dados_de_string = json.loads(json_string)
print("\n--- 1.2 json.loads() ---")
print(f"Tipo de retorno: {type(dados_de_string)}")
print(f"Valor em Python: {dados_de_string}")
print(f"Acessando um valor: {dados_de_string['nome']}")


# --- Métodos DUMP e LOAD (Trabalhando com arquivos) ---

NOME_ARQUIVO_JSON = 'dados.json'

# 2.1. json.dump(obj, fp): Escrevendo em um arquivo JSON
with open(NOME_ARQUIVO_JSON, 'w', encoding='utf-8') as arquivo:
    json.dump(dados_python, arquivo, indent=2, ensure_ascii=False) # ensure_ascii=False para acentos
print(f"\n--- 2.1 json.dump() ---")
print(f"A string JSON foi escrita no arquivo '{NOME_ARQUIVO_JSON}'.")
# Conteúdo do arquivo (após execução):
# {
#   "nome": "Teacher Python",
#   "idade": 3,
#   ...
# }

# 2.2. json.load(fp): Lendo de um arquivo JSON
with open(NOME_ARQUIVO_JSON, 'r', encoding='utf-8') as arquivo:
    dados_lidos = json.load(arquivo)
print(f"\n--- 2.2 json.load() ---")
print(f"Tipo de retorno: {type(dados_lidos)}")
print(f"Dados lidos do arquivo: {dados_lidos}")
```

#### Detalhes do Código JSON

- **`json.dumps(obj)`:** Recebe o dicionário `dados_python` e retorna uma `string` (variável `json_string`) no formato JSON. O argumento `indent=4` é opcional e serve para formatar a saída com quebras de linha e indentação para torná-la mais legível.

- **`json.loads(s)`:** Recebe a `string` JSON e a transforma de volta em um dicionário Python (`dados_de_string`). O tipo de retorno é um `<class 'dict'>`.

- **`json.dump(obj, fp)`:** Abre o arquivo em modo de escrita (`'w'`), e passa o objeto Python e o objeto de arquivo (`arquivo`) para a função. Ela cuida da serialização e da escrita no disco.

- **`json.load(fp)`:** Abre o arquivo em modo de leitura (`'r'`), e passa o objeto de arquivo para a função. Ela lê o conteúdo, o desserializa e retorna um objeto Python (normalmente um `dict` ou `list`).

- **Context Manager (`with open(...)`):** É a forma recomendada de trabalhar com arquivos em Python, garantindo que o arquivo seja fechado corretamente, mesmo que ocorram erros.

---

### 2. Manipulação de Dados CSV (`import csv`)

O módulo `csv` fornece classes e funções para ler e escrever dados tabulares (tabela) em formato CSV. Por padrão, ele trata cada linha como uma lista de strings.

| **Objeto/Função**                     | **Descrição**                                                                                                                    | **Retorno de Exemplo (por linha)**                       | **Uso Principal**                                                    |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------- |
| `csv.reader(csvfile)`                 | Retorna um objeto **iterador** que processa linhas do arquivo CSV, tratando cada linha como uma **lista de strings**.            | `['Alice', '30', 'Engenheiro']`                          | Leitura simples onde a ordem e o tipo de dado são conhecidos.        |
| `csv.writer(csvfile)`                 | Retorna um objeto que converte dados em strings delimitadas para serem **escritas** no arquivo.                                  |                                                          | Escrita simples de listas/tuplas no formato CSV.                     |
| `csv.DictReader(csvfile)`             | Retorna um objeto **iterador** que mapeia as informações de cada linha para um **dicionário**, usando os cabeçalhos como chaves. | `{'Nome': 'Bob', 'Idade': '25', 'Ocupacao': 'Analista'}` | Leitura onde os dados são acessados pelo nome da coluna (cabeçalho). |
| `csv.DictWriter(csvfile, fieldnames)` | Semelhante ao `writer`, mas escreve linhas a partir de **dicionários**, usando `fieldnames` para definir a ordem das colunas.    |                                                          | Escrita de dados estruturados como dicionários, garantindo a ordem.  |

#### Exemplo de Código: CSV

```Python
import csv
import os

NOME_ARQUIVO_CSV = 'dados.csv'
DADOS_PARA_CSV = [
    ['Nome', 'Idade', 'Cidade'],
    ['Alice', 30, 'São Paulo'],
    ['Bob', 25, 'Rio de Janeiro'],
    ['Charlie', 40, 'Belo Horizonte']
]
DADOS_DICT_PARA_CSV = [
    {'Nome': 'David', 'Idade': 35, 'Cidade': 'Curitiba'},
    {'Nome': 'Eva', 'Idade': 28, 'Cidade': 'Porto Alegre'}
]
CABECALHOS = ['Nome', 'Idade', 'Cidade']

# --- Escrita CSV (writer e DictWriter) ---

# 1.1. csv.writer: Escreve listas no arquivo CSV
with open(NOME_ARQUIVO_CSV, 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    print("--- 1.1. csv.writer (writerow/writerows) ---")
    
    # escritor.writerow(): Escreve uma única linha
    escritor.writerow(DADOS_PARA_CSV[0]) # Escreve o cabeçalho
    # escritor.writerows(): Escreve múltiplas linhas (listas de listas)
    escritor.writerows(DADOS_PARA_CSV[1:]) # Escreve os dados
    print(f"Dados (listas) escritos em '{NOME_ARQUIVO_CSV}'.")

# 1.2. csv.DictWriter: Escreve dicionários no arquivo CSV (adiciona novos dados)
with open(NOME_ARQUIVO_CSV, 'a', newline='', encoding='utf-8') as arquivo:
    escritor_dict = csv.DictWriter(arquivo, fieldnames=CABECALHOS)
    print("\n--- 1.2. csv.DictWriter (writerows) ---")
    
    # Não usamos writeheader() aqui para não duplicar o cabeçalho (apenas 'a'ppend)
    escritor_dict.writerows(DADOS_DICT_PARA_CSV)
    print(f"Novos dados (dicionários) adicionados a '{NOME_ARQUIVO_CSV}'.")


# --- Leitura CSV (reader e DictReader) ---

# 2.1. csv.reader: Lendo o arquivo como listas (simples)
with open(NOME_ARQUIVO_CSV, 'r', newline='', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    print("\n--- 2.1. csv.reader ---")
    print(f"Tipo de retorno do iterador: {type(leitor)}")
    for i, linha in enumerate(leitor):
        print(f"Linha {i}: {linha} (Tipo: {type(linha)})")
        # Retorno de Exemplo (linha 1): ['Alice', '30', 'São Paulo']


# 2.2. csv.DictReader: Lendo o arquivo como dicionários (com cabeçalho)
with open(NOME_ARQUIVO_CSV, 'r', newline='', encoding='utf-8') as arquivo:
    leitor_dict = csv.DictReader(arquivo)
    print("\n--- 2.2. csv.DictReader ---")
    print(f"Tipo de retorno do iterador: {type(leitor_dict)}")
    for i, linha in enumerate(leitor_dict):
        print(f"Linha {i} (dict): {linha}")
        # Retorno de Exemplo (linha 1): {'Nome': 'Alice', 'Idade': '30', 'Cidade': 'São Paulo'}
        # Acesso por chave: print(linha['Nome'])
        
# Limpeza para evitar sujeira nos testes
if os.path.exists(NOME_ARQUIVO_CSV):
    os.remove(NOME_ARQUIVO_CSV)
```

#### Detalhes do Código CSV

- **`newline=''`:** É crucial ao abrir arquivos CSV em Python (especialmente no Windows) para evitar problemas com quebras de linha em branco extras.

- **`csv.writer(arquivo)`:** Cria um objeto escritor. Use `escritor.writerow(lista)` para escrever uma única linha (lista) e `escritor.writerows(lista_de_listas)` para escrever várias linhas de uma vez.

- **`csv.DictWriter(arquivo, fieldnames=CABECALHOS)`:** Cria um objeto escritor que usa dicionários. O argumento obrigatório `fieldnames` define a ordem das colunas e as chaves esperadas nos dicionários. Use `escritor_dict.writerows(lista_de_dicionarios)`. Se estivesse criando o arquivo, usaria `writer_dict.writeheader()` para escrever a primeira linha (cabeçalho).

- **`csv.reader(arquivo)`:** Cria um objeto leitor que retorna um iterador. Ao iterar, cada elemento (`linha`) é uma **lista de strings** representando os campos daquela linha. Todos os dados são strings, então você pode precisar de conversão de tipos (`int(linha[1])`).

- **`csv.DictReader(arquivo)`:** Cria um objeto leitor que usa a primeira linha do arquivo como chaves (cabeçalhos) e retorna um iterador. Ao iterar, cada elemento (`linha`) é um **dicionário**, permitindo acesso aos valores pelo nome da coluna (ex: `linha['Nome']`).
