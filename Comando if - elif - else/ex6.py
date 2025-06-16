'''Faça um programa que receba um número 
inteiro e verifique se esse número é par ou ímpar.'''

# Recebendo número inteiro : 
X = int(input('Informe um número: \n'))

par = 0

# '%' se o resto da divisão for 0, vai ser par, caso contrario, ímpar. 
if par == X % 2 :
    print('Par!')
else:
    print('Ímpar!')



