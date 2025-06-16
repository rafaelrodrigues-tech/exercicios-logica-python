''' Faça um programa que receba três números
distintos e mostre-os em ordem crescente'''

# Recebendoo três números distintos: 
A = int(input('Informe o primeiro número: '))
B = int(input('Informe o segundo número: '))
C = int(input('Informe o terceiro número: '))

num = ( A, B, C)
sorted(num)

print(sorted(num))