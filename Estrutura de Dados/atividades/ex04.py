""" Faça um programa que carregue um vetor e 
nove  elementos  numéricos  inteiros,  calcule  e  mostre  os  números  primos  e  suas 
respectivas posições."""

vetor = []
cont = 1

for i in range(3):
    num = int(input(f"Insira um número na posição {i+1}: "))
    vetor.append(num)
    
while cont <= num:
    if cont % num == 0:
        cont += 1

print(cont)