# 23. Faça um programa que o usuário insira uma lista de 10 frutas e atribua números em sequência aos seus índices. Exiba esse dicionário.
# A seguir, remova todos os elementos que possuam chaves ímpares. Exiba o dicionário com as alterações.
dicio = {}
for i in range(1,11):
    dicio.update({i: input("Digite o nome da fruta {}: ".format(i))})
print(dicio)
for i in range(1,11):
    if i%2!=0:
        dicio.pop(i)
print(dicio)