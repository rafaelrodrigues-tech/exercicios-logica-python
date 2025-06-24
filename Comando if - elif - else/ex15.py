"""Faça um programa que receba o salário de 
um  funcionário,  calcule  e  mostre  o  novo  salário  desse  funcionário,  acrescido  de 
bonificação e de auxílio-escola.

Salário Bonificação 
Até R$ 500,00  5% do salário 
Entre R$ 500,01 e R$ 1.200,00 12% do salário 

Acima de R$ 1.200,00 Sem bonificação 

Salário Auxílio-escola 
Até R$ 600,00 R$ 150,00 
Mais que R$ 600,00 R$ 600,00"""

sal = float(input("Salário do funcionário: "))

#Bonificação
if sal <= 500:
    bon = (sal * 0.05)
elif sal <= 1.200:
    bon = (sal * 0.12)
else:    
    bon = 0
#Auxilio
if sal <= 600:
    aux = 150
else:
    aux = 600

new_sal = sal + bon + aux

print(f"O Salário do funcionário vai ser de R${new_sal:.2f}")

