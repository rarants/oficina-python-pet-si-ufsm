# 05.Faça um programa que verifique se o ano é bissexto.
# Para um ano ser bissexto, ele deve ser divsível por 4.
# Não pode ser divisível por 100.
# Pode ser divisível por 400.
ano = int(input("Digite o ano: "))
if (ano%4==0 and ano%100!=0) or ano%400==0:
    print("É bissexto!")
else:
    print("Não é bissexto")       
