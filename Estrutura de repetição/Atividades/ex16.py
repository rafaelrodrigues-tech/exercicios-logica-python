"""Desenvolva  um  algoritmo  que  peça  ao 
usuário que insira cinco conjuntos de dois números inteiros positivos (A, B), no qual A 
deve ser menor que B (supõe-se que o usuário irá respeitar esse enunciado). Para cada 
dupla  (A,  B),  informada  pelo  usuário,  o  algoritmo  deve  mostrar,  na  tela,  todos  os 
números pares compreendidos entre A e B (inclusive)."""


for i in range(1,6):
    print()
    a = int(input("Insira um número: "))
    b = int(input("Insira outro numero: "))
    print("Números Pares: ",end=" ")
    for j in range(a,b+1):
        if (j % 2 == 0):
            print(f"\033[32m{j}\033[m",end=" ")   
 

