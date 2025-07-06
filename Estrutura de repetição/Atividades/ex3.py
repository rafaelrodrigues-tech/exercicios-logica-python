"""3) Desenvolva um algoritmo que receba um número N e calcule o fatorial de N, sabendo 
que N! = N * (N-1) * (N-2) * ... * 3 * 2 * 1"""

""" n = int(input("Número: 5"))

fatorial = 5 x 4 x 3 x 2 x 1 = 120

N * (n - 1) * (n - 2) * (5 - 3) * ( 5 - 4) = 120"""

n = int(input("Qual número deseja fatorar? "))

f = 1
print(f"Fatorial de {n}! = ",end="")

for i in range(n,0,-1):
    print(f"{i}",end="")
    if i > 1:
        print(f" x ",end="")
        f *= i
print(f" = {f}")    

