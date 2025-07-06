"""Desenvolva  um  algoritmo  que  receba  um 
número N e informe se N é um número primo, ou não. A saber: um número primo é um 
inteiro positivo que só pode ser dividido por ele mesmo e por um, apenas"""
n = int(input("Insira um número: "))
c = 1
div = 0

while c <= n:
    if n % c == 0:
        div += 1
    c += 1

if div == 2:
    print(f"O número {n} é Primo!")

else:
    print(f"O número {n} Não é Primo!")            