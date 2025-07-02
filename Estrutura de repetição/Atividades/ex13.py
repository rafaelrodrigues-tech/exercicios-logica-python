""" Desenvolva um algoritmo que mostre a tabuada de todos os números inteiros 
compreendidos entre 1 e 10 (inclusive)."""
print("-"*15)
for i in range(1,11):
    for j in range(0,11):
        print(f"{i} x {j} = {i*j}")
    print("-"*15)        