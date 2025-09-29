# Para abrir um arquivo ou escrever neste arquivo, usa-se as funções abaixo

# ao abrir um arquivo para escrita, um novo arquivo é criado mesmo que ele já
# exista, sobrescrevendo o antigo.
file = open("arquivo.txt", mode="w")

file.write("nome idade\n")
file.write("Maria 45\n")
file.write("Miguel 33\n")

# Não precisa da quebra de linha, pois esse é um comportamento padrão do print
print("Túlio 22", file=file)

# Para escrever múltiplas linhas podemos utilizar a função writelines.
# Repare que a função espera que cada linha tenha seu próprio caractere de
# separação (\n):
LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
file.writelines(LINES)

# Sempre precisa fechar o arquivo
file.close()

# A leitura do conteúdo de um arquivo pode ser feita utilizando a função read
# leitura
file = open("arquivo.txt", mode="r")
content = file.read()
print(content)
file.close()  # não podemos esquecer de fechar o arquivo

# Um arquivo é também um iterável
# A cada iteração, uma nova linha é retornada.
# leitura
file = open("arquivo.txt", mode="r")
for line in file:
    # não esqueça que a quebra de linha também é um caractere da linha
    print(line)
file.close()  # não podemos esquecer de fechar o arquivo
