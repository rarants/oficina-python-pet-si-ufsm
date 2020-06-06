# 15.Faça um programa que o nome de uma pessoa, diga o tamanho do mesmo, sem contar os espaços e diga se possui a letra a.
nome = input("Digite um nome: ").replace(" ", "")
print("Possui {} letras.".format(len(nome)))
if "a" in nome:
    print("A letra a aparece no nome!")
else:
    print("A letra a não aparece no nome!")

    