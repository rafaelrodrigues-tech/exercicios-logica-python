"""Faça um programa que receba o salário de 
um  funcionário,  calcule  e  mostre  o  novo  salário,  sabendo-se  que  este  sofreu  um 
aumento de 25%."""

sal = float(input("Insira o salário: "))
new_sal = sal + (sal*25)/100

print("📝Relatório:")
print(f"Salário antes do aumento: R${sal:.2f}")
print(f"Após o aumento: R${new_sal:.2f}")
