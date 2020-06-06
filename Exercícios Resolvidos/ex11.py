# 11.Faça um programa que calcule o faterial de um número inteiro. (Ex. de  fatorial: 4! = 4 * 3 * 2 * 1 = 24)
num = int(input("Digite um número: "))
fat = 1
for i in range(1, num+1):
    fat*=i
print("O fatorial de {} é {}!".format(num, fat))