# -*- utf-8 -*-
"""
Calculadora
Autor: Cherelzada do Bailaum
Função: Para você que é burro e não sabe somar, dividir, multiplicar ou subtrair.
"""
print("~~ Calculadara do Cherelzada --- Teste Aprimoarado Papai ~~")
print(" Sinais : (Soma = + ) (Subtração = - ) (Divisão = / ) (Multiplicação = * ) (Exponênciação = ^ )") 

num1 = input("Digite o primeiro número: ")
num1 = int(num1)
sinal = input("Digite o sinal da operação: ")
num2 = input("Digite o segundo número: ")
num2 = int(num2)
#Soma

if sinal == "+":
	Operação = num1 + num2

#Subtração 
if sinal == "-":
	Operacão = num1 - num2

#Divisão
if sinal == "/":
	Operação = num1 / num2

#Multiplicação
if sinal == "*":
	Operação = num1 * num2

if sinal == "^":
	Operação = num1 ** num2

print("Olha a merda do resultado seu burro: ")
print(Operação)