""" Faça um programa que carregue uma matriz 
2x2, calcule e mostre uma matriz resultante que será a própria matriz digitada 
multiplicada pelo maior elemento da matriz. """

matriz = []
bigger = counter = 0
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input(f"Insira um número na posição ({i},{j}): ")))
    matriz.append(linha)    

maior_elemento = matriz[0][0]    

for i in range(2):
    for j in range(2):
        if matriz[i][j] > maior_elemento: # Encontrando o maior elemento da matriz.
            maior_elemento = matriz[i][j]

matriz_resultante = []
for i in range(2):
    linha_resultante = []
    for j in range(2):
        linha_resultante.append(matriz[i][j] * maior_elemento) # Multiplicando pelo maior elemento.
    matriz_resultante.append(linha_resultante)    

print("\nMatriz Resultante")
for linha_resultante in matriz_resultante:
    print(linha_resultante)
    
