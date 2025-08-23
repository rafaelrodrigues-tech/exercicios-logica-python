""" Faça um programa que carregue uma matriz 
3 x 5 com números inteiros e some cada uma das linhas, armazenando o resultado das 
somas  em  um  vetor.  A  seguir,  multiplique  cada  elemento  da  matriz  pela  soma  da 
respectiva linha daquele elemento e mostre a matriz resultante."""

matriz = []
matriz_soma = []
#preenchimento da matriz 3x5
for i in range(3):
    linha = []
    linha_soma = []
    for j in range(5):
        num = int(input(f"Insira um número na posição ({i},{j}): "))
        linha.append(num)  
    matriz.append(linha)
    matriz_soma.append(sum(linha)) # soma da linha pronta

matriz_resultante = []
# Multiplicando cada elemento pelo valor da soma da respectiva linha
for i in range(3):
    linha_resultante = []
    for j in range(5):
        linha_resultante.append(matriz[i][j] * matriz_soma[i])
    matriz_resultante.append(linha_resultante)    

print("\nMatriz Resultante:")
for linha_resultante in matriz_resultante:
    print(linha_resultante)