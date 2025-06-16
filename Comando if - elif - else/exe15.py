'''Faça um programa que receba quatro 
valores, I, A, B e C. I é um valor inteiro e positivo e A, B e C são valores reais e distintos. 
Escreva os números A, B e C obedecendo à tabela a seguir. Supor que o valor digitado 
para I seja sempre um valor válido, ou seja, 1, 2 ou 3'''



I = int(input('Escolha um deles: 1, 2 ou 3: '))
A = float(input('Informe um número real: '))
B = float(input('Agora,Informe outro número real: '))
C = float(input('Por fim, informe o ultimo número real: '))
print()

numbers = (A,B,C)
if I == 1:
    result = sorted(numbers)
    print('Números em ordem crescente : ',result)
    print()
elif I == 2:
    result = sorted(numbers,reverse=True)    
    print('Números em ordem decrescente : ',result)
    print()
elif I == 3:
    sorted_numbers = sorted(numbers)
    result = [sorted_numbers[0], sorted_numbers[2], sorted_numbers[1]]
    print("Maior número no meio:", result)
    print()
else:
    print('Número Inválido')    
    print()
