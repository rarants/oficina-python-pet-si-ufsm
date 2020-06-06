# 24. Faça um programa com uma função que calcule a média ponderada de um aluno (Nota1 = peso 2, Nota2 = peso 4, Nota3 = peso 3). 
# A seguir, informe a média e se o aluno foi aprovado ou reprovado. As notas serão inseridas pelo usuário. 
aluno = {}
media = 0
for i in range(1,4):
    aluno.update({"Nota {}".format(i): float(input("Digite a nota %d do aluno: " % i))})
    if i==1:
        media+=aluno.get("Nota {}".format(i))*2
    elif i==2:
        media+=aluno.get("Nota {}".format(i))*4
    else:
        media+=aluno.get("Nota {}".format(i))*3
media/=9
if media>=7:
    print("A média do aluno foi de: %.2f. \nO aluno foi aprovado!" % media)
else:
    print("A média do aluno foi de: %.2f. \nO aluno foi reprovado!" % media)
