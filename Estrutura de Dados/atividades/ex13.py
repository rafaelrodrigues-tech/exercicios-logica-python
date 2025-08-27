"""Faça um programa que carregue uma matriz 
10x3  com  as  três  notas  de  dez  alunos.  Mostre  um  relatório  com  o  número  do  aluno 
(número da linha) e a prova em que cada aluno obteve menor nota. Ao final do relatório, 
mostre quantos alunos tiveram menor nota na prova 1, quantos alunos tiveram menor 
nota na prova 2 e quantos alunos tiveram menor nota na prova 3."""

notas = []
menores_notas = []
for i in range(3):
    nota_linha = []
    for j in range(3):
        nota_linha.append(float(input(f"Digite a {j+1}ª do {i+1}ª aluno: ")))
    print()
    notas.append(nota_linha)    
    menores_notas.append(min(nota_linha)) #min, vai pegar as menores notas

