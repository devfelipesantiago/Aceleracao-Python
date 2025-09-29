# Um conjunto é uma coleção de elementos únicos e não ordenados.
# Conjuntos implementam operações de união, intersecção e outras.

permissions = {
    "member",
    "group",
}  # elementos separados por vírgula, envolvidos por chaves

permissions.add("root")  # adiciona um novo elemento ao conjunto

permissions.add(
    "member"
)  # como o elemento já existe, nenhum novo item é adicionado ao conjunto

permissions.union({"user"})  # retorna um conjunto resultado da união

permissions.intersection(
    {"user", "member"}
)  # retorna um conjunto resultante da intersecção dos conjuntos

permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos
