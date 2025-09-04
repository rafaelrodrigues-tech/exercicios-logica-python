"""Faça um programa que receba o número de 
horas trabalhadas por um gestor e o valor do salário mínimo vigente. Crie uma função 
que calcule o salário a receber do gestor, seguindo as regras abaixo: 
 
 I - a hora trabalhada vale a metade do salário mínimo; 
II - o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da 
hora trabalhada; 
 III - o imposto equivale a 3% do salário bruto; 
 IV - o salário a receber equivale ao salário bruto menos o imposto. 
Crie um algoritmo que invoque a respectiva função e mostre o salário a receber."""

def calculando_valor_hora_trabalhada(salario_minimo): #valor da hora trabalhada
    hora = salario_minimo / 2
    return hora

def calculando_salario_bruto(horas_trabalhadas,hora):#salario bruto
    salario_bruto = horas_trabalhadas * hora
    return salario_bruto

def calculando_imposto(salario_bruto):
    imposto = salario_bruto * (3/100)
    return imposto

def salario_liquido(salario_bruto,imposto):
    liquido = salario_bruto - imposto
    return liquido

salario_minimo = float(input("Insira o sálario mínimo: "))
horas_trabalhadas = int(input("Quantas horas trabalhadas? "))

hora = calculando_valor_hora_trabalhada(salario_minimo)
print(f"Valor da hora trabalhada: {hora}")

salario_bruto = calculando_salario_bruto(horas_trabalhadas,hora)
print(f"Sálario Bruto :R${salario_bruto:.2f}")

imposto = calculando_imposto(salario_bruto)
print(f"Imposto: {imposto}")

liquido = salario_liquido(salario_bruto,imposto)
print(f"Sálario a receber: {liquido:.2f}")