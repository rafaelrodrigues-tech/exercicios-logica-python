""" Faça um programa que carregue um vetor e 
nove  elementos  numéricos  inteiros,  calcule  e  mostre  os  números  primos  e  suas 
respectivas posições."""
vetor = []
primos = []
for i in range(9):
    elem = int(input(f"Insira um número na posição {i+1}: "))
    vetor.append(elem)
    cont = 1
    add = 0
    
    while cont <= elem:
        if elem % cont == 0:
            add += 1 # add vai incrementando, se passar de 2, add deixa de ser primo.
        cont += 1
     
    if add == 2:
        primos.append(elem)

print("\n📝Resultado: ")
print(f"Números Primos: {primos}")