""" Faça um programa que leia um valor N inteiro 
e positivo, calcule e mostre o valor de E, conforme a fórmula a seguir: 
 
E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N"""

n = int(input("Insira um número inteiro: "))
e = 1 # começa com 1 porque o primeiro termo é fixo
f = 1 # fatorial

for i in range(1,n+1):
    f *= i  # calcula o fatorial de i
    e *= 1/ f # soma o inverso do fatorial no E
print(f"\nValor de E = {n}: {e}")    