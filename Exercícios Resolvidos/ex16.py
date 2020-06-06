# 16.Faça um programa que solicite uma data e escreva-a por extenso. Ex.: 25/04/2020 => 25 de abril de 2020.
data = input("Digite a data [dd/mm/aaaa]: ")
mes = int(data[3:5])
if mes==1:
    print(data[:2] + " de Janeiro de " + data[6:])
elif mes==2:
    print(data[:2] + " de Fevereiro de " + data[6:])
elif mes==3:
    print(data[:2] + " de Março de " + data[6:])
elif mes==4:
    print(data[:2] + " de Abril de " + data[6:])
elif mes==5:
    print(data[:2] + " de Maio de " + data[6:])
elif mes==6:
    print(data[:2] + " de Junho de " + data[6:])
elif mes==7:
    print(data[:2] + " de Julho de " + data[6:])
elif mes==8:
    print(data[:2] + " de Agosto de " + data[6:])
elif mes==9:
    print(data[:2] + " de Setembro de " + data[6:])
elif mes==10:
    print(data[:2] + " de Outubro de " + data[6:])
elif mes==11:
    print(data[:2] + " de Novembro de " + data[6:])
elif mes==12:
    print(data[:2] + " de Dezembro de " + data[6:])
else: 
    print("Mês Inválido!")