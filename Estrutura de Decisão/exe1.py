#Calculo de duas Notas 


n1 = float(input("Digite a primeira nota: \n"))
n2 = float(input("Digite a segunda nota: \n"))

media = (n1 + n2)/2

print(f"Media igual a: {media:.2f} \n")
print(f"Sua Primeira nota foi: {n1:.2f} \n")
print(f"Sua Segunda nota foi: {n2:.2f} \n") 

if media >= 7.0: 
    print("Aprovado(a)! \n")
if media < 7.0 and media >= 4.0:
    print("Tem direito a exame! \n")    
if media < 4.0: 
    print("Reprovado! \n")
    



