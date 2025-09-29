from tkinter import Y


x = "ab"
x, y = "ab"
# Saída:
# x = "a"; y = "b"

nome_e_nascimento = [("Felipe", "Japão"), ("João", "Brasil")]
for nome, pais in nome_e_nascimento:
    print(nome, pais)
# Saída:
# Felps Máxico
# João Brasil

# x, y = "Felipe"
# Saída:
# ValueError: too many values to unpack

x, *y = "Felipe"
# Saída:
# x = "F"
# y = ["e", "l", "p", "s"]
print(x)
print(Y)
