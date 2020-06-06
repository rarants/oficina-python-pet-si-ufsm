# 13. Faça um programa que leia um número inteiro de até 4 dígitos e imprima a saída de forma a exibir quantos milhares, centenas, dezenas e unidades. 
# Ex.: xyzw. Para tanto, utilize o operador %
# milhar(es) = x000
# centenas(s) = y00
# dezena(s) = z0
# unidade(s) = w
num = int(input("Digite um número de até 4 dígitos: "))
aux = 0
while num>=10000:
    print("Valor inválido")
    num = int(input("Digite um número de até 4 dígitos: "))
aux = num//1000
print("Milhar(es) = {}".format(1000*aux))
num = num%1000
aux = num//100
print("Centena(s) =  {}".format(100*aux))
num = num%100
aux = num//10
print("Dezena(s)  =   {}".format(10*aux))
aux = num%10
print("Unidade(s) =    {}".format(aux))
