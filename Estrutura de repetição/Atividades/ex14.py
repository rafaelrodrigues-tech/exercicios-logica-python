""" Faça um programa que leia um número N e 
que  indique  quantos  valores  inteiros  e  positivos  devem  ser  lidos  a  seguir.  Para  cada 
número lido, mostre o fatorial desse valor."""
cont = 0
n = int(input("Quantos valores deseja fatorar? "))
while cont < n:
    num = int(input("\nInsira um número: "))
    f = 0
    print(f"{num}! =",end=" ")
     
    for i in range(num,0,-1):
        print(f"{i}",end="")
        if i > 1:
            print(" x ",end="")
            f *= i    
    print(f"= {f}",end="") 
    cont += 1    


    
