# Preecher uma matriz 3x3, somar e calcular a média dos elementos
matriz = []
soma = 0
print("Adicione números na matriz:")
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input("Número: "))
        soma += num
        linha.append(num)
    matriz.append(linha)    

# total de elementos = linhas * colunas
tam = (i+1) * (j+1)

print("\nMatriz: ")
for linha in matriz: 
    print(linha)   

print("\n📊Resultados:")
print(f"Somatório: {soma}")
print(f"Média Aritmética: {soma/tam:.2f}")