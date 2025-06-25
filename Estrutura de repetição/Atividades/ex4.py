#4) Desenvolva um algoritmo que receba um número N e imprima a tabuada de N, na tela.

n = int(input("Insira um número:"))
print(f"Tabuada do {n}".center(20))

print("-"*20)

for i in range(0,11):
    res = n * i
    print(f" {n} x {i} = {res} ".center(20))

print("-"*20)    
