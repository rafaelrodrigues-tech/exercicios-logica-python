"""Desenvolva um algoritmo que peça ao usuário que preencha os dados de um vetor de 5 
posições com valores reais quaisquer, desde que estejam compreendidos entre 1 e 100 
(suponha que o usuário irá respeitar o enunciado). Ao final, o algoritmo deve mostrar, 
na tela, o conteúdo de cada posição do vetor, dividido por 100."""

v = []

print("Preencha o vetor a seguir utilizando números reais de 1 a 100:")
for i in range(5):
    v.append(float(input(f"Insira um valor para a posição {i+1}: ")))

for i in range(len(v)):
    v[i] = v[i] / 100
print(f"\nConteúdo dividido por 100: {v}")    
