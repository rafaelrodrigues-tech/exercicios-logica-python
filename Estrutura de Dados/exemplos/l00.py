l = []
cont = 0
while True:
    try:
        num = int(input("Insira um número(0 para finalizar): "))
    except:
        print("⚠ Por favor, Insira um número inteiro válido.")   
        continue 
    
    if not num == 0:
        l.append(num)
        cont += 1
    else:
        print("Finalizando...")
        break
if l:        
    print(f"\nQuantidade de elementos : {cont}") 
    print(f"Maior elemento: {max(l)}")
    print(f"Menor elemento: {min(l)}")
else:
    print("🚫 Nenhum número adicionado.")    
        