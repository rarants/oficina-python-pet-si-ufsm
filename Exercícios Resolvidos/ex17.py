# 17.Faça um programa que conte quantas vogais há no texto (a ser inserido pelo usuário).
texto = input("Digite o texto: ")
print("Há {} vogais no texto.".format(texto.count("a") + texto.count("i") + texto.count("u") + texto.count("e") + texto.count("o") ))