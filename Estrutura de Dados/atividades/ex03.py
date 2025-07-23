"""Desenvolva  um  algoritmo  que  preencha  um  vetor  numérico  de  10  posições.  Após 
preencher todo o vetor, o usuário deve inserir uma chave de busca X. Caso exista algum 
número  igual  a  X,  dentro  do  vetor,  o  algoritmo  deve  mostrar,  na  tela,  o  índice  da 
primeira posição na qual X foi encontrado. Caso contrário, o algoritmo deve se encerrar 
com uma única mensagem, dizendo "Chave não encontrada.". """

vetor = []

for i in range(10):
    vetor.append(int(input(f"Insira um valor para a {i+1}ª posição : ")))

chave_x = int(input("\nInsira a chave de busca: "))    

if chave_x in vetor:
    print(f"\033[32mChave encontrada na posição {vetor.index(chave_x)}\033[m")
else:
    print("\033[31;4mChave não encontrada\033[m.")    
