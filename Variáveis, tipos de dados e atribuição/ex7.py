""" Faça um programa que receba o salário-base 
de  um  funcionário,  calcule  e  mostre  o  seu  salário  a  receber,  sabendo-se  que  esse 
funcionário teve gratificação de R$ 600,00 e paga imposto de 10% sobre o salário base."""

sal = float(input("Insira seu Salário: "))
imp = sal - (sal * 10) / 100 # Calculo do imposto.
new_sal = 600 + imp # Calculo do novo salário

print(f"Novo Salário a receber: \033[32mR${new_sal:.2f}\033[m") # Aumento do salário na cor verde para das destaque.
