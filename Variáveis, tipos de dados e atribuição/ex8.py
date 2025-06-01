"""Faça um programa que receba o valor de um 
depósito e  o valor da taxa de  juros, calcule e  mostre o valor do rendimento e o valor 
total depois do rendimento."""

dep = float(input("Insira o valor do depósito: "))
tx = float(input("Insira a taxa de juros: "))

rend = (dep * tx) / 100
total = dep + rend

print(f"Rendimento: {rend}")
print(f"Valor total: {total}")


