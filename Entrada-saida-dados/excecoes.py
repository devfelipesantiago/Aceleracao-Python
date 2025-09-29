# Para tratar exceções utilizamos o conjunto de instruções try,
# com as palavras reservadas try e except.
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


try:
    arquivo = open("arquivo.txt", "r")
except OSError:
    # será executado caso haja uma exceção
    print("arquivo inexistente")
else:
    # será executado se tudo ocorrer bem no try
    print("arquivo manipulado e fechado com sucesso")
    arquivo.close()
finally:
    # será sempre executado, independentemente de erro
    print("Tentativa de abrir arquivo")


# Criamos um contexto, limitando o escopo onde o arquivo está aberto.
# O uso do "as" aqui é somente para atribuir o valor utilizado no contexto à variável file
with open("arquivo.txt", "w") as file:
    file.write("Michelle 27\n")
# como estamos fora do contexto, o arquivo foi fechado
print(file.closed)


notas = open("file.txt", mode="w")
notes = [
    "Marcos 10\n",
    "Felipe 4\n",
    "José 6\n",
    "Ana 10\n",
    "Maria 9\n",
    "Miguel 5\n",
]
notas.writelines(notes)
notas.close()

notas = open("file.txt", mode="r")
content = notas.read()
print(content.split())
notas.close()

recovery_students = []
with open("file.txt") as grades_file:
    for line in grades_file:
        student_grade = line
        student_grade = student_grade.split(" ")
        if int(student_grade[1]) < 6:
            recovery_students.append(student_grade[0] + "\n")


with open("recoveryStudentsFile.txt", mode="w") as recovery_students_file:
    print(recovery_students)
    recovery_students_file.writelines(recovery_students)
