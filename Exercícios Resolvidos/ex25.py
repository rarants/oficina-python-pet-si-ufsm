# 25. Faça um programa (usando funções) que calcule o pagto (parametros: horas semanais e valor hora) considere um limite de horas de 40horas semanais e, 
# para o excedente, o pagto por hora sera 10% a mais.
def pgto(horas, valorH):
    if horas<=40:
        print("Pagamento = {}".format(horas*valorH))
    else:
        print("Pagamento = {}".format((valorH*40)+((horas-40)*valorH*0.1)))

pgto(int(input("Qual o número de horas trabalhadas? ")), int(input("Qual o valor pago por hora? ")))