#Matriz
mat = [# 0 1 2
        [1,2,3],# 0
        [4,5,6],# 1
        [7,8,9] # 2
]

print("Todos os elementos da primeira linha: ")
for elem in mat[0]:
    print(elem,end=" ")
print()

print("Todos os elementos da matriz: ")
for linha in mat:
    for elem in linha:
        print(elem,end=" ")
    print()    
print()
print("Elemento da segunda linha terceira coluna :")
print(mat[1][2]) #Lembrando que se inicia do zero.