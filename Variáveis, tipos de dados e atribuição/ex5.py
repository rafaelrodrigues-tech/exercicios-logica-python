"""Faça um programa que receba o salário de 
um  funcionário  e  o  percentual  de  aumento,  calcule  e  mostre  o  valor  do  aumento e o 
novo salário."""

sal = float(input("Insira o salário: "))
perc = int(input("Qual o percentual de aumento: "))

new = sal + (sal * perc) / 100
value = (sal * perc) / 100 
print("📝Relatório: ")
print(f"Novo salário: R${new:.2f}")
print(f"O funcionário teve aumento de R${value:.2f}")