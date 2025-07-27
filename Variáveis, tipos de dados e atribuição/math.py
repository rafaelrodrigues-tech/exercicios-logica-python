""" Faça um programa que receba um número 
positivo e maior que zero, calcule e mostre: 
 
 a) o número digitado ao quadrado; 
 b) o número digitado ao cubo; 
 c) a raiz quadrada do número digitado; 
 d) a raiz cúbica do número digitado."""
import math
num = int(input("Insira um número positivo: "))

r = math.sqrt(num)
r_c = num ** (1/3)

print("\nResultado:")
print(f"Ao Quadrado: {num}² = {pow(num,2)}; Ao cubo: {num}³ = {pow(num,3)}.")
print(f"Raíz Quadrada: {r:.2f}; Raíz Cubida: {r_c:.2f}")

