# 18. Faça um programa que leia uma string e duplique cada caractere da mesma em uma nova string e imprima essa nova string.
str1 = input("Digite uma string: ")
str2 = ""
for i in str1:
    str2 = str2+i+i    
print("Nova string = %s" % str2)