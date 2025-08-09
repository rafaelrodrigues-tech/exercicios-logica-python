# Carregando um vetor de 9 números e identificando quais elementos são números primos.
vetor = []
primos = []
for i in range(9):
    elem = int(input(f"Insira um número na posição {i+1}: "))
    vetor.append(elem)
    contador = 1
    divisores = 0
    
    # Conta quantos divisores o número possui
    while contador <= elem:
        if elem % contador == 0:
            divisores += 1  # Encontrou um divisor
        contador += 1
     
    # Se número tem exatamente 2 divisores, é primo
    if divisores == 2:
        primos.append(elem)

print("\n📝Resultado: ")
print(f"Números Primos: {primos}")