"""Desenvolva um algoritmo que peça para que o usuário informe a base e a altura de um 
retângulo,  e  um  terceiro  número  inteiro  "op".  Caso  o  usuário  escolha  "op"  igual  a  0, 
calcule e mostre o perímetro do retângulo. Caso o usuário insira um valor 1 para "op", 
calcule e mostre a área do retângulo. Se o  usuário inserir um valor diferente de 0 e 1 
para "op", mostrar a mensagem "Opção inválida."."""
print("-"*36)
print("CALCULO DO RETÂNGULO".center(35))
print("-"*36)
b = float(input("Informe a Base do retângulo: "))
a = float(input("Informe a Altura do retângulo: "))

print("""\033[33m
0 - Perímetro
1 - Área   
\033[m         
""")

op = int(input("Qual opção deseja escolher? "))

if op == 0:
    print("\nVocê escolheu calcular o perímetro do retângulo!")
    print(f"P = 2 x ( b + a ) = {2 * ( b + a )}.")
elif op == 1:
    print("\nVocê escolheu calcular a Área!")    
    print(f"A = b x a = {b * a}.")
else:
    print("\033[4;31mOpção inválida!\033[m")    

 

