""" Faça um programa que receba dois números 
e  mostre  o  maior  deles.  Caso  eles  sejam  iguais,  deve-se  mostrar  a  mensagem  "Os 
números são iguais"."""

n = float(input("Informe um número: "))
n2 = float(input("Informe o segundo número: "))

if n > n2:
    print(f"O número {n} é maior que o {n2}.")
elif n2 > n:
    print(f"O número {n2} é maior que o {n}.")
else:
    print("Ambos são iguais.")        