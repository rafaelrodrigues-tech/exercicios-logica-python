'''Faça um programa que receba dois números 
e mostre o maior deles. Caso eles sejam iguais, deve-se mostrar a mensagem "Os 
números são iguais".
'''

# Recebendo dois números 
A = int(input("Informe o primeiro número: \n"))
print()
B = int(input('Informe o segundo número: \n'))
print()
# Identificando o maior entre eles
if A > B:
    print(A,'é maior que',B)
elif B > A:
    print(B,'é maior que',A)   
else:
    print("Os números são iguais")
        
# função else vai mostrar se eles são iguais
   