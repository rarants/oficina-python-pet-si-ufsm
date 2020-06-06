# 26.Faça um programa que calcule o faterial de um número inteiro por meio de uma função.  (Ex. de  fatorial: 4! = 4 * 3 * 2 * 1 = 24)
def fatorial(num):
    fat = 1
    for i in range(1, num+1):
        fat*=i
    return fat    

res = fatorial(int(input("Digite um número: ")))
print("O fatorial é {}!".format(res))
