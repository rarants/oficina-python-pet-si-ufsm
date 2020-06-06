# 10.Faça um programa que leia um numero inteiro e verifique se ele é ou não um número primo (número primo é aquele que só é divisível por ele mesmo e por 1).
num = int(input("Digite um número inteiro: "))
div = 0
for i in range(1, num+1):
    if num%i==0:
        div+=1
if div==2 or num==1:
    print("É primo!")
else:
    print("Não é primo!")