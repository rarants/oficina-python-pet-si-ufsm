# 07.Faça um programa que calcule a média de 10 valores. Use laços de repetição.
media = 0
for i in range(0,10):
    media+=int(input("Digite um valor: "))
media/=10
print("A média é: {}".format(media))