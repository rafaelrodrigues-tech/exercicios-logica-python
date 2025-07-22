"""Desenvolva um algoritmo que preencha um vetor numérico de 10 posições. Ao final, o 
algoritmo deve mostrar o somatório de todos os elementos do vetor, bem como a média 
aritmética entre todos os termos."""

vetor = []
print("Preencha o vetor a seguir:")
for _ in range(6):
    num = int(input("Número: "))
    vetor.append(num)

for linha in vetor:
    for num in linha: 
        print(num)  
