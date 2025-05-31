"""Faça um programa que receba três notas e 
seus respectivos pesos, calcule e mostre a média ponderada dessas notas"""
n = float(input("Digite a primeira nota: "))
p = int(input("Digite o seu primeiro peso: "))
n2 = float(input("Digite a sua segunda nota: "))
p2 = int(input("Digite o segundo peso: "))
n3 = float(input("Digite a terceira nota: "))
p3 = int(input("Digite o seu terceiro peso: "))

m_p = (n*p + n2*p2 + n3*p3)/(p+p2+p3)

print(f"Média Ponderada: {m_p:.2f}")
