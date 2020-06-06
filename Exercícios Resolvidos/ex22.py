# 22. Faça um programa em que o usuário insira 2 opostos diagonalmente de um retângulo em um dicionário e calcule e exiba sua área e seu perímetro (a soma de todos os lados).
dicio = {}
dicio.update({"x1":int(input("x1 = ")), "y1":int(input("y1 = ")), "x2":int(input("x2 = ")), "y2":int(input("y2 = "))})
# Em  um retângulo, temos 4 lados, sendo que temos pares de 2 e 2 que são iguais. 
# Calculamos as medidas dos lados com base na fórmula da distância entre dois pontos
A = ((((dicio.get("x1")-dicio.get("x2"))**2)**(1/2)))
B = ((((dicio.get("y1")-dicio.get("y2"))**2)**(1/2)))
print("A área do retângulo é {}.".format(A*B), "O perímetro do retângulo é {}".format((2*A)+(2*B)))
