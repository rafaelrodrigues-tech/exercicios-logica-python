"""Faça um programa que receba dois números 
maiores que zero, calcule e mostre um elevado ao outro."""

n = int(input("Número maior que zero: "))
n2 = int(input("Segundo número: "))

a = pow(n,n2)

print(f"O número {n} elevado {n2} = {a}.")
