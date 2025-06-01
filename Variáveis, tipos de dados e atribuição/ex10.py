"""  Faça  um  programa  que  calcule  e  mostre a 
área de um círculo. Sabe-se que: Área = Pi * R², aonde Pi = 3,14"""

print("Área do círculo")
pi = 3.14
r = float(input("Insira o valor do Raio: "))

a = pi * pow(r,2)
print(f"Área de {a}m²")