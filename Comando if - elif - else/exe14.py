'''Desenvolva um algoritmo que peça ao usuário que informe os coeficientes a, b e c de 
uma equação de segundo grau: ax² + bx + c. Com base na Fórmula de Bhaskara, calcule 
e mostre as raízes da respectiva equação de segundo grau.
'''



import math

#Entrada dos coeficientes 
print('Informe os coeficientes a seguir: \n')

a = int(input('Coeficiente "a": \n'))
b = int(input('Coeficiente "b": \n'))
c = int(input('Coeficiente "c": \n'))
print()
delta = pow(b,2) - 4 * a * c
raiz_delta = math.sqrt(delta)

x1 = -(b + raiz_delta)/(2 * a)
x2 = -(b - raiz_delta)/(2 * a)

print('O seu Delta é igual a',delta,'e sua raíz é',raiz_delta)
print('Logo o seu x1 é',x1,'e o seu x2 é igual a',x2)

