""" Faça um programa que mostre o menu de 
opções a seguir, receba a opção do usuário e dos dados necessários para executar cada 
operação. Suponha que o usuário não irá inserir valores inválidos. 
 
Menu de opções: 
1. Somar dois números 
2. Raiz quadrada de um número 
Digite a opção desejada"""

from time import sleep
import math
print("""
Menu de opções:
    
    1 - Somar dois números
    2 - Raiz quadrada de um número        
""")

sleep(1.5)

op = int(input("Digite a opção desejada: "))
if op == 1:
    num = float(input("\nInsira o primeiro número: "))
    n2 = float(input("Próximo número: "))
    
    print("\nCarregando...")
    sleep(1.5)
    print(f"\n{num} + {n2} = {num+n2}")

if op == 2:
    num = float(input("\nInsira um número: "))
    raiz = math.sqrt(num)

    print(f"\nA Raíz Quadrada de {num} é {raiz}.")

print("Fim!")


