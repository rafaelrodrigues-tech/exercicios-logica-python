"""Faça um programa que receba três notas de 
um aluno, calcule e mostre a média aritmética e a mensagem que segue a tabela abaixo. 
Para  alunos  de  exame,  calcule  e  mostre  a  nota  que  deverá  ser  tirada  no  exame  para 
aprovação, considerando que a média no exame é 6,0. 
 
Média aritmética Mensagem 
0,0 ~ 3,0 Reprovado 
3,0 ~ 7,0 Exame 
7,0 ~ 10,0 Aprovado"""

n = float(input("Digite a sua primeira nota: "))
n2 = float(input("Agora, A sua Segunda nota: "))
n3 = float(input("Por fim, a Terceira nota: "))

#Média aritmética
m_a = (n + n2 + n3) / 3 

if m_a >= 0 and m_a < 3:
    print(f"Sua Média: {m_a}")
    print("\nReprovado!")

elif m_a >= 3 and m_a < 7:
    print(f"Sua Média: {m_a}")
    print(f"\nExame! Precisa tira {12 - m_a}")

elif m_a >= 7 and m_a <= 10:
    print(f"Sua Média: {m_a}")
    print("\nAprovado!")        