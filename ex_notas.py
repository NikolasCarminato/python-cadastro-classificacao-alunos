n = int(input("Quantidade Alunos: "))
alunos_notas = []
aprovado = []
recuperacao = []
reprovado = []


for Numero in range(1, n + 1):
    Alunos = input(f"Nome Aluno {Numero}: ")
    Notas = float(input(f"Nota {Numero}: "))

    aluno = {
        "Numero" : Numero,
        "Aluno" : Alunos,
        "Notas" : Notas
    }

    alunos_notas.append(aluno)

    if Notas >= 60:
        aprovado.append(aluno)

    elif Notas >= 40:
        recuperacao.append(aluno)

    else:
        reprovado.append(aluno)



def ordenar_por_nome(aluno):
    return aluno["Aluno"].lower()


aprovado.sort(key=ordenar_por_nome)
recuperacao.sort(key=ordenar_por_nome)
reprovado.sort(key=ordenar_por_nome)

numero = 1

for aluno in aprovado:
    aluno["Numero"] = numero
    numero += 1

for aluno in recuperacao:
    aluno["Numero"] = numero
    numero += 1

for aluno in reprovado:
    aluno["Numero"] = numero
    numero += 1


print ("\n Notas dos Alunos: ")
print ("---------- Aprovados, Boa ----------")
for aluno in aprovado:
    print(f"Número: {aluno['Numero']}")
    print(f"Nome: {aluno['Aluno']}")
    print(f"Nota: {aluno['Notas']}")
    print()
print ("---------- Recuperação Jovem ----------")
for aluno in recuperacao:
    print(f"Número: {aluno['Numero']}")
    print(f"Nome: {aluno['Aluno']}")
    print(f"Nota: {aluno['Notas']}")
    print()
print ("---------- Putz, Reprovados ----------")
for aluno in reprovado:
    print(f"Número: {aluno['Numero']}")
    print(f"Nome: {aluno['Aluno']}")
    print(f"Nota: {aluno['Notas']}")
    print()






