"""Faça um programa que carregue uma matriz 
10x3  com  as  três  notas  de  dez  alunos.  Mostre  um  relatório  com  o  número  do  aluno 
(número da linha) e a prova em que cada aluno obteve menor nota. Ao final do relatório, 
mostre quantos alunos tiveram menor nota na prova 1, quantos alunos tiveram menor 
nota na prova 2 e quantos alunos tiveram menor nota na prova 3."""

matriz = []
provas = [0, 0, 0]  # contadores das provas 1, 2 e 3

# Entrada de dados
for i in range(10):
    linha = []
    for j in range(3):
        nota = float(input(f"Aluno {i+1}, digite a {j+1}ª nota: "))
        linha.append(nota)
    matriz.append(linha)

print("\nRELATÓRIO DE MENORES NOTAS")
print("-" * 40)

# Processamento e relatório
for i, notas in enumerate(matriz, start=1):
    menor = min(notas)               # pega a menor nota da linha
    prova = notas.index(menor) + 1   # pega o índice da menor nota (1,2 ou 3)
    print(f"Aluno {i}: menor nota na prova {prova}")
    provas[prova-1] += 1             # incrementa no contador

print("\nResumo final:")
print(f"Menor nota na prova 1: {provas[0]} alunos")
print(f"Menor nota na prova 2: {provas[1]} alunos")
print(f"Menor nota na prova 3: {provas[2]} alunos")
