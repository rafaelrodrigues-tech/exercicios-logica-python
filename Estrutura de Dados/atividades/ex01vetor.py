"""Desenvolva um algoritmo que preencha um vetor numérico de 10 posições. Ao final, o 
algoritmo deve mostrar o somatório de todos os elementos do vetor, bem como a média 
aritmética entre todos os termos."""

v = [] # Vetor
for i in range(10):
    num = int(input(f"Número para a posição {i+1}: "))
    v.append(num)
 
print(f"\nSomatório: {sum(v)}") 
print(f"Média Aritmética: {sum(v) / len(v)}") #len() verifica o tamanho do vetor "v"