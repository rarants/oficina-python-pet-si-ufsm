# 06.Faça um programa que calcule a média de três notas de um aluno e verifique se ele foi aprovado ou reprovado. (Considere a média para aprovação, 7).
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
media = (n1+n2+n3)/3
if(media>=7):
    print("Aprovado :)")
else:
    print("Reprovado :(")
