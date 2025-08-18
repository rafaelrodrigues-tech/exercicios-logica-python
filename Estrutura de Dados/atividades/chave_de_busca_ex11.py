"""
Crie um algoritmo que:
1. Preencha uma matriz 3x3 com valores inteiros.
2. Peça ao usuário uma chave de busca X.
3. Informe a posição (linha, coluna) da primeira ocorrência de X, 
   ou mostre 'Chave não encontrada.' caso não exista.
"""
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Insira um número na posição ({i},{j}): "))
        linha.append(num)
    matriz.append(linha)

chave_de_busca = int(input("\nInforme a chave de busca x: "))    
achou = False   # Flag para indicar se a chave foi encontrada.

print("\nMatriz preechida:")
for linha in matriz:
    print(" ".join((f"{num:3}")for num in linha)) # centraliza em 3 espaços

for i, linha in enumerate(matriz): #enumerate vai retornar o índice da linha(i).
    if chave_de_busca in linha:
        j = linha.index(chave_de_busca) #index, vai procurar pelo primeiro índice da coluna (j).
        print(f"\nNúmero encontrado na posição ({i},{j})")
        achou = True 
        break
if not achou:
    print("\nChave não encontrada.")    
