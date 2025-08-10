"""Desenvolva  um  algoritmo  que  preencha  cada  elemento  de  uma  matriz  3x3  com  o 
quadrado do valor do índice da linha mais o valor do índice da coluna daquela posição. 
Ao final, o algoritmo deve mostrar a matriz, na tela."""
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Linha {i} na Coluna {j}: "))
        linha.append(num)
    matriz.append(linha)    

for i in range(3):
    for j in range(3):
        matriz[i][j] = (i + j) ** 2 # Cálculo

print("\nMatriz elevado ao quadrado: ")
for linha in matriz:
    print(linha)