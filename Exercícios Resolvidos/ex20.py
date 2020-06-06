# 20. Crie um programa em que o usuário deve digitar as notas de 10 alunos. Essas notas ficarão salvas em um dicionario. A seguir, exiba os
# alunos registrados e o aluno que obteve a maior nota.
dicio = {}
maior = 1
for i in range(1, 11):
    dicio.update({"Aluno " + str(i): input("Digite a nota do aluno {}: ".format(i))})
    if dicio.get("Aluno " + str(i))>dicio.get("Aluno " + str(maior)):
        maior = i
print("Alunos registrados = {}.\nA maior nota foi do aluno {}".format(dicio, maior))
