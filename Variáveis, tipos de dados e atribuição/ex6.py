"""Faça um programa que receba o salário-base 
de um funcionário, calcule e mostre o salário a receber, sabendo-se que esse funcionário 
tem gratificação de 5% sobre o salário-base e paga imposto de 7% sobre o salário-base."""
sal = float(input("Salário do funcionário: "))
grt= sal + ( sal * 5 ) / 100 #gratificação
imp = grt - (sal * 7 ) / 100 #imposto

print(f"Salário a receber R${imp:.2f}")