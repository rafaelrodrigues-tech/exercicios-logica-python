"""A nota final de um estudante é calculada a 
partir  de  três  notas  atribuídas  respectivamente  a  um  trabalho  de  laboratório,  a  uma 
avaliação semestral e a um exame final. A média das três notas mencionadas 
anteriormente obedece aos pesos a seguir:

obs: Tabela no pdf"""
"""
Média ponderada Conceito 
8,0 ~ 10,0 A 
7,0 ~ 8,0 B 
6,0 ~ 7,0 C 
5,0 ~ 6,0 D 
0,0 ~ 5,0 E"""


p1 = 2
p2 = 3
p3 = 5

tr = float(input("Nota do trabalho de laboratório: "))
av = float(input("Nota de Avaliação semestral: "))
ex = float(input("Nota de Exame final: "))

#Média Ponderada
m = (tr * p1 + av * p2 + ex * p3) / (p1 + p2 + p3)

if m >= 8 and m <= 10:
    print(f"\nMédia Ponderada = {m}")
    print("\033[32mConceito A\033[m")

elif m >= 7 and m < 8:
    print(f"Média Ponderada = {m}")
    print("\033[32mConceito B\033[m")

elif m >= 6 and m < 7:
    print(f"Média Ponderada = {m}")
    print("\033[33mConceito C\033[m")

elif m >= 5 and m < 6:
    print(f"Média Ponderada = {m}")
    print("\033[33mConceito D\033[m")

elif m >= 0 and m < 5:
    print(f"Média ponderada = {m}")
    print("\033[31mConceito E\033[m")    