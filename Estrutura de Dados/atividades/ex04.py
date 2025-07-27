""" Faça um programa que carregue um vetor e 
nove  elementos  numéricos  inteiros,  calcule  e  mostre  os  números  primos  e  suas 
respectivas posições."""

vetor = []
cont = 1
soma = 0

for i in range(3):
    msg = "\nInsira um valor para a posição " + str(i+1) + ": "
    vetor.append((int(input(msg))))
    
