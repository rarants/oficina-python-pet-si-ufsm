# 09.Faça um programa que leia 10 valores e verifique quantos são pares.
par = 0
for i in range(0,10):
    x = int(input("Digite um valor: "))
    if x%2==0:
        par+=1
print("{} números são pares.".format(par))
