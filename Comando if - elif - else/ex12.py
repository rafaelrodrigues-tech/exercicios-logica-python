""" Faça  um  programa  que  receba  quatro 
valores, I, A, B e C. I é um valor inteiro e positivo e A, B e C são valores reais e distintos. 
Escreva os números A, B e C obedecendo à tabela a seguir. Supor que o valor digitado 
para I seja sempre um valor válido, ou seja, 1, 2 ou 3. 
 
Valor de I  Forma de escrever 
1 A, B e C em ordem crescente 
2 A, B e C em ordem decrescente 
3 O maior fica entre os outros dois 
números 
"""

I = int(input("Informe um número entre 1,2 e 3: "))
A = float(input("Digite um número real: "))
B = float(input("Digite outro número real: "))
C = float(input("Por fim, mais um número real: "))

numbers = [A,B,C]

if I == 1:
    print(f"A ordem crescente entre os números citados acima: {sorted(numbers)}")
elif I == 2:
    print(f"A ordem decrescente entre os números citados acima: {sorted(numbers,reverse=True)}")    
elif I == 3:
    if A > B and A > C:
        print(f"Ordem gerada: {B, A, C}")
    elif B > A and B > C:
        print(f"Ordem gerada: {A, B, C}")    
    elif C > A and C > B:
        print(f"Ordem gerada: {A, C, B}")


 
 
 
 
