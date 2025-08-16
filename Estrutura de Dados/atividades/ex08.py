"""Desenvolva um algoritmo que preencha uma matriz numérica de dimensões 3x3. Depois 
de a matriz ter sido populada, o algoritmo deverá imprimir a matriz da seguinte forma: 
os dados da diagonal principal devem ser  impressos normalmente  e os dados fora da 
diagonal principal devem substituídos por zero."""
matriz = []
print("Adicione números na matriz a seguir:\n")
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Linha {i} coluna {j}: "))
        if i == j:
            linha.append(num)
        else:
            linha.append(0)    
    matriz.append(linha)        

print()
print("Matriz Identidade:")
for linha in matriz:
    print(linha)