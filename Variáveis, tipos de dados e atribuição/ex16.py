""" Faça  um  programa  que  receba  o  ano  de 
nascimento de uma pessoa e ano atual, calcule e mostre: 
 
 a) a idade dessa pessoa; 
 b) quantos anos essa pessoa terá em 2030;"""
from datetime import datetime
atual = datetime.now().year
ano = int(input("Ano do seu nascimento: "))
idade = atual - ano

print(f"\nVocê tem {idade} anos.")
print(f"Em 2030 você terá {2030 - ano} anos.")