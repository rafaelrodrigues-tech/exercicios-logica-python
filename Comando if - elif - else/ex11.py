"""Desenvolva um algoritmo que peça ao usuário que informe os coeficientes a, b e c de 
uma equação de segundo grau: ax² + bx + c. Com base na Fórmula de Bhaskara, calcule 
e mostre as raízes da respectiva equação de segundo grau."""
import math
from time import sleep 

print("-"*35)
print("EQUAÇÃO DO SEGUNDO GRAU".center(35))
print("-"*35)

print("\nInforme os coeficientes a seguir:")
a = float(input(" a = "))
b = float(input(" b = "))
c = float(input(" c = "))

print("\nCalculando na Fórmula de Bhaskara...")
sleep(1)

#Encontrando o Delta
delta = pow(b,2) - 4 * a * c

#Raíz do Delta
r_d = math.sqrt(delta) 

# Raízes da equação
x1 = (-b + r_d) / (2 * a)
x2 = (-b - r_d) / (2 * a)

print("\n📝Resultados:")
print(f"Delta = {delta}")
print(f"Raíz do Delta = {r_d}")
print(f"Raízes da Equação: X1 = {x1} e X2 = {x2}.")
