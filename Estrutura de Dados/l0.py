from time import sleep
l = []
c = 1

while c <= 5:
    num = int(input("Insira um número: "))
    l.append(num)
    c +=1

print("Calculando a Média...")
sleep(1)

print("~"*30)  
print("📝Resultado:")  
print(f"Média = {sum(l)/len(l):.2f}")    
print("~"*30)
