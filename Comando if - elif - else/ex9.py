""" Faça um programa que receba três números 
distintos e mostre-os em ordem crescente."""
print("-"*30)
print("Ordem Crescente Númerica".center(30))
print("-"*30)
n = int(input("Primeiro: "))
n2 = int(input("Segundo: "))
n3 = int(input("Terceiro: "))

numbers = [n,n2,n3]

print(f"\nOrdem Crescente {sorted(numbers)}")