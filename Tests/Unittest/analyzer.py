# arquivo: analyzer.py
import json
from pathlib import Path

DIRETORIO_ATUAL = Path(__file__).parent
ARQUIVO_JSON = DIRETORIO_ATUAL / "person_data.json"


def read_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def analyze_json_file(file_path):
    if file_path.suffix != ".json":
        raise ValueError("O arquivo precisa ser um arquivo JSON.")

    data = read_json_file(file_path)
    return f"A pessoa de nome {data['nome']} " f"tem {data['idade']} anos de idade."


# Chamada usando o caminho absoluto garantido:
print(read_json_file(ARQUIVO_JSON))

# Exemplo de chamada da função de análise:
print(analyze_json_file(ARQUIVO_JSON))
