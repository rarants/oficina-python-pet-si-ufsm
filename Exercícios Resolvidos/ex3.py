# 03.Faça um programa que solicite dois números inteiros e verifique qual é o menor deles.
x = int(input("X: "))
y = int(input("Y: "))
if x<y:
	print("X é maior.")
elif y<x:
	print("Y é maior.")
else: 
	print("X e Y são iguais.")