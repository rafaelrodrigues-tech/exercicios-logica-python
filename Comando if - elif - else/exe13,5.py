''' Faça um programa que receba três números 
obrigatoriamente em ordem crescente e um quarto número que não siga esta regra. 
Mostre, em seguida, os quatro números em ordem não-crescente'''

# Digitar em ordem crescente.
num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número maior que o primeiro: '))
num_3 = int(input('Digite o terceiro número maior que o anterior: '))
num_4 = int(input('Informe um número que não siga essa sequência: '))# 4 - número, Sem seguir ordem
print()
if num_4 > num_3 and num_2 > num_1:
    print('{},{},{},{}'.format({num_4},{num_3},{num_2},{num_1}))
    print('Ordem não crescente')
elif num_3 > num_2 and num_1 > num_4:
    print('{},{},{},{}'.format({num_3},{num_2},{num_1},{num_4}))
    print('Ordem não crescente')    
elif num_3 > num_4 and num_4 > num_2:
    print('{},{},{},{}'.format({num_3},{num_4},{num_2},{num_1}))
    print('Ordem não crescente')
elif num_3 > num_4 and num_2 > num_1:
    print('{},{},{},{}'.format({num_3},{num_4},{num_2},{num_1}))
    print('Ordem não crescente')
    


