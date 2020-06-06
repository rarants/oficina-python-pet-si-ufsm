# 04.Faça um programa que verifique se os três pontos digitados pertencem a um triangulo 
# (pertencem um triângulo quando a medida de qualquer um dos lados é menor que a soma das medidas dos outros dois lados e maior que 
# o valor absoluto da diferença entre essas medidas). A seguir, verifique se o mesmo é equilátero (possui três lados iguais), 
# isósceles (possui dois lados iguais) ou escaleno (possui todos os lados diferentes).
x1 = int(input("Digite um valor para x1: "))
y1 = int(input("Digite um valor para y1: "))

x2 = int(input("Digite um valor para x2: "))
y2 = int(input("Digite um valor para y2: "))

x3 = int(input("Digite um valor para x3: "))
y3 = int(input("Digite um valor para y3: "))

# Não será um triângulo se os três pontos pertencem à mesma reta.
# Poderá ser um triângulo se dois pontos pertencerem à mesma reta e forem diferentes
# Poderá ser um retângulo se todos os pontos pertencerem a retas diferentes
if (x1!=x2 or x1!=x3)and(y1!=y2 or y1!=y3):
    print("É um triângulo!")
    # Calculam-se os valores dos lados
    A = (((x1-x2)**2)+((y1-y2)**2))**(1/2)
    B = (((x2-x3)**2)+((y2-y3)**2))**(1/2)
    C = (((x3-x1)**2)+((y3-y1)**2))**(1/2)
    if (A == B) and (B == C):
        print("É equilátero!")
    elif (A == B) or (B == C) or (A == C):
        print("É isósceles!")
    else:
        print("É escaleno!")