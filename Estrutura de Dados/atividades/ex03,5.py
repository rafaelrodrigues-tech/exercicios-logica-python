# Código do professor.

vet = [] 
 
for i in range(10):                    
    msg = "Insira o dado da posição " + str(i+1) + ":\n" 
    vet.append(float(input(msg))) 
 
X = float(input("Insira a chave de busca:\n")) 
achou = False 
i = 0 
 
while i < 10 and achou == False: 
    if vet[i] == X: 
        achou = True 
        p = i # Posição
    i += 1 
 
if achou: 
    print("Chave encontrada na posição:", p+1) 
else: 
    print("Chave não encontrada") 

