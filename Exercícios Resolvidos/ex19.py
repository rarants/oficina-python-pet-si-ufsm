# 19. Faça um programa em que o usuário deve inserir nomes em uma lista até que o mesmo digite "0".  A seguit, imprima a mesma exibindo seus 
# valores e respectivos índices.
nome = input("Digite um nome: ")
lista=[]
while nome != '0':
    lista.append(nome)
    nome = input("Digite um nome: ")
print(lista)