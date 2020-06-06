# 08.Faça um programa que leia 20 valores e informe qual é o maior e qual o menor valor dentre estes.
maior = 0
menor = 0
for i in range(0,20):
    x = int(input("Digite um valor: "))
    if x<menor:
        menor = x
    if x>maior:
        maior = x
print("O maior valor é {}, e o menor é {}".format(maior, menor))
