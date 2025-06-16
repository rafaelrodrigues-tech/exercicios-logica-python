""" Desenvolva um algoritmo que emule um caixa eletrônico. O usuário deve inserir o valor 
total a ser sacado da máquina e o algoritmo deve informar quantas notas de 100, 50, 
20, 10, 5 ou 2 reais serão entregues. Deve-se escolher as notas para que o usuário receba 
o menor número de notas possível."""

value = int(input("Informe o valor a ser sacado: "))

cem = value // 100
value = value % 100
cin = value // 50
value = value % 50
vint = value // 20
value = value % 20
dez = value // 10
value = value % 10
cinc = value // 5
value = value % 5
dois = value // 2
value = value % 2

print(f"Nª de R$ 100,00 notas {cem}")
print(f"Nª de R$ 50,00 notas {cin}")
print(f"Nª de R$ 20,00 notas {vint}")
print(f"Nª de R$ 10,00 notas {dez}")
print(f"Nª de R$ 5,00 notas {cinc}")
print(f"Nª de R$ 2,00 notas {dois}")

