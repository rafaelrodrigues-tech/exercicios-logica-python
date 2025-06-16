''' Faça um programa que mostre o menu de 
opções a seguir, receba a opção do usuário e dos dados necessários para executar cada 
operação. Suponha que o usuário não irá inserir valores inválidos.
Menu de opções:
1. Somar dois números
2. Raiz quadrada de um número
Digite a opção desejada'''
import math

print('Menu de opções: ')
print('1 - Somar dois números')  
print('2 - Raíz quadrada de um número')  
op = int(input('Digite a opção desejada: '))
print()

if op == 1:
    escolha_1 = int(input('Digite o primeiro número: '))
    escolha_2 = int(input('Segundo número: '))
    print()
    soma = escolha_1 + escolha_2
    print(escolha_1,'+',escolha_2,'=',soma)
elif op == 2:
    escolha_1 = int(input('Digite o seu número: '))
    print()
    raiz_quad = math.sqrt(escolha_1)   
    print('A raíz de',escolha_1,'é igual a ',raiz_quad) 
else:
    print('Número inválido')

    

