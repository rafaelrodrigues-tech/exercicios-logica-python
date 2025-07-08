m = []
print("Insira valores na matriz a seguir:\n")
for i in range(3):
    linha = []
    for j in range(4):
        num = int(input(f"Na linha {i} coluna {j}: "))
        linha.append(num)
        m.append(linha)  
    print()    

# Busca por elementos da matriz
for linha in m:
    for num in linha:
        print(num,end=" ")    
    print()    

    