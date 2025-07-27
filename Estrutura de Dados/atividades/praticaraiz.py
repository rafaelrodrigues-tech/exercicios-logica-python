"""Faça um programa que carregue dois vetores 
de  dez  elementos  numéricos  cada  um  e  mostre  um  vetor  resultante  da  intercalação 
desses dois vetores."""

vetor_a = []
vetor_b = []

print("Primeiro Vetor:")
for i in range(10):
    msg = "\nInsira um valor para a " + str(i+1) +"ª posição: " # versão raiz
    vetor_a.append(int(input(msg))) 

    # vetor_a.append(int(input(f"Insira um número para a posição {i+1}"))) # versão python
print("."*50)
print("\nSegundo Vetor: ")
for i in range(10):
    msg = "\nInsira um valor para a " + str(i+1) +"ª posição: "
    vetor_b.append(int(input(msg))) 

print("."*50)
# Intercalação dos vetores
vetor_r = [] #vetor resultante
for i in range(10):
    vetor_r.append(vetor_a[i])
    vetor_r.append(vetor_b[i])

print(f"O resultado da intercalação entre os dois vetores: {vetor_r}")