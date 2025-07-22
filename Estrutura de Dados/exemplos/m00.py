m = []
print("Insira valores na matriz a seguir:\n")
for i in range(3):
    linha = []
    for j in range(4):
        linha.append(int(input(f"Na linha {i} coluna {j}: ")))
    m.append(linha)  
    print()    

maior_ele = m[0][0]
menor_ele = m[0][0]
posicao_maior = (0,0)
posicao_menor = (0,0)

for i in range(3):
    for j in range(4):
        if m[i][j] > maior_ele:
            maior_ele = m[i][j]
            posicao_maior = (i,j)
        if m[i][j] < menor_ele:
            menor_ele = m[i][j]
            posicao_menor = (i,j)

print("Matriz Inserida:")
for linha in m:
    print(linha)

print(f"O maior elemento é o {maior_ele} na posição {posicao_maior}.")
print(f"O menor elemento é o {menor_ele} na posição {posicao_menor}.")    