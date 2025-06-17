"""Desenvolva  um  algoritmo  que  receba  dois  números,  calcule  e  mostre  a  multiplicação 
entre eles, se ambos forem iguais. Caso o primeiro seja maior que o segundo, mostre a 
subtração do primeiro pelo segundo. Caso contrário, mostre a soma entre os dois."""

print("Informe dois números a seguir: ")
n = float(input("\nPrimeiro: "))
n2 = float(input("Segundo: "))

if n == n2:
    print(f"{n} x {n2} = {n * n2}")

elif n > n2:
    print(f"{n} - {n2} = {n - n2}")    

else:
    print(f"{n} + {n2} = {n + n2}")