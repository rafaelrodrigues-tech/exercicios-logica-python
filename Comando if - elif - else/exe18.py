''' Faça um programa que receba o salário de 
um funcionário, calcule e mostre o novo salário desse funcionário, acrescido de 
bonificação e de auxílio-escola.
Salário Bonificação
Até R$ 500,00 5% do salário
Entre R$ 500,01 e R$ 1.200,00 12% do salário
Acima de R$ 1.200,00 Sem bonificação
Salário Auxílio-escola
Até R$ 600,00 R$ 150,00
Mais que R$ 600,00 R$ 600,00
'''

sal = float(input('Informe o seu salário: '))

if sal <= 500:
   bonif = sal * 0.05 
   aux = 0
elif sal > 500: 
   bonif = sal * 0.12
   aux = 0
elif sal > 1.200:
   bonif = 0
   aux = 0
elif sal <= 600:
   aux = 150   
elif sal > 600:
   aux = 600

sal_novo = sal + bonif + aux 

print(f'Seu salário novo vai passar a ser: {sal_novo: .2f} ')


