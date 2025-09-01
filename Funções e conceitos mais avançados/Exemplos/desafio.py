# criar uma calculadora com 4 funções e uma função para o menu:
from time import sleep
def calculando_soma(num1,num2):
    return num1 + num2

def calculando_subtrair(num1,num2):
    return num1 - num2

def calculando_multiplicar(num1,num2):
    return num1 * num2

def calculando_divisao(num1,num2):
    if num2 != 0:
        return num1/num2
    else:
        return "❌Erro, Não é possível dividir por 0."

    
def menu_opcoes():
    print("-"*30)
    print("MINHA CALCULADORA".center(30))
    print("-"*30)
    print("""1 - SOMAR
2 - SUBTRAIR
3 - MULTIPLICAR
4 - DIVIDIR                              
5 - SAIR
""")    
while True:
    menu_opcoes()
    op = input("Insira a opção escolhida: ")

    if op == '5':
        print("Finalizando o programa...")
        sleep(1)
        print("👋 Volte sempre! ")
        break

    if op in ('1','2','3','4'):
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))
        print("\nResultado:")
        if op == '1':
            res = calculando_soma(num1,num2)
            print(f"{num1} + {num2} = {res}")
        elif op == '2':
            res = calculando_subtrair(num1,num2)
            print(f"{num1} - {num2} = {res}")
        elif op == '3':
            res = calculando_multiplicar(num1,num2)    
            print(f"{num1} x {num2} = {res}")
        elif op == '4':
            res = calculando_divisao(num1,num2)
            print(f"{num1}/{num2} = {res}")
    else:
        print("Escolha Invalída! Digite um número entre 1 a 5.")        
        