"""Desenvolva um algoritmo que preencha uma matriz numérico de dimensões 3x3. Após 
preencher todo a matriz, o usuário deve inserir uma chave de busca X. Caso exista algum 
número igual a X, dentro da matriz, o algoritmo deve mostrar, na tela, os índices da linha 
e  da  coluna  da  posição  na  qual  na  qual  X  foi  encontrado  pela  primeira  vez.  Caso 
contrário, o algoritmo deve se encerrar com uma única mensagem, dizendo "Chave não 
encontrada."."""

matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        num = int(input(f"Insira um número na posição ({i},{j}): "))
        linha.append(num)
    matriz.append(linha)

chave_de_busca = int(input("Informe a chave de busca x: "))        
chave = matriz.index(num)
for linha in matriz:
    for num in linha:
        if chave_de_busca == num:
            print(f"Chave encontrada na posição: {chave}")