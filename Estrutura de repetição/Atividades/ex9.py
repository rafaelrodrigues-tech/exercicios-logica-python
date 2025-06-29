"""Desenvolva um algoritmo que peça ao usuário que insira dois números inteiros positivos 
A  e  B,  no  qual  A  deve  ser  menor  que  B  (supõe-se  que  o  usuário  irá  respeitar  esse 
enunciado). O algoritmo deve mostrar, na tela, todos os números ímpares 
compreendidos entre A e B (inclusive)."""

# Entrada de números inteiros.
a = int(input("1ª Número: "))
b = int(input("2ª Número: "))

#Exibição dos números ímpares.
print(f"\nNúmeros ímpares: ",end=" ")

if a > b: # Caso o usuário digite um número maior primeiro vai haver uma troca.
    a,b = b,a # troca os valores.

# Para cada número entre A e B( incluindo A e B), vai retornar um número. 
for num in range(a,(b + 1)): # (a,(b+1)) Inicia-se no A e termina no B. B+1 pq o ultimo número não ia contar, no caso o número B. 
    if num % 2 == 1: # '%' Quando o resto da divisão for 1, o número vai ser ímpar.
        print(f"\033[32m{num}\033[m",end=" ")
#Cor verde para destacar os números ímpares.    
