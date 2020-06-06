# 21. Faça um programa que contenha dois dicionarios "a" e "b" e imprima-os. A seguir, troque seus valores e imprima-os.
dicio1 = {1: "Ana", 2: "Fernanda", 3: "José"}
dicio2 = {"r": "Rosa", "p": "Preto", "l": "laranja"}
print("Original: \nDicio1 = ", dicio1, "\nDicio2 = ", dicio2)

dicioAux = dicio2.copy()
dicio2 = dicio1.copy()
dicio1 = dicioAux.copy()
print("Invertido: \nDicio1 = ", dicio1, "\nDicio2 = ", dicio2)
