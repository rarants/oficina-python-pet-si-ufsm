# 14. Faça um programa que leia 5 valores inteiros e positivos. Verifique para cada um deles se é par e, em caso positivo, 
# calcule o fatorial de cada um. Do contrário, exiba a soma dos inteiros de 0 até esse número.
for i in range(0,5):
    num = int(input("Digite um número inteiro positivo: "))
    if num==0:
        print("O fatorial de 0! é 0.")
    elif num%2==0:
        fat = 1
        for i in range(1, num+1):
            fat*=i
        print("O fatorial de {} é {}!".format(num, fat))
    else:
        soma = 0
        for i in range(1, num+1):
            soma+=i
        print("A soma é {}!".format(soma))