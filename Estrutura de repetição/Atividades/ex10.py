"""Faça um programa que leia dez conjuntos de 
dois valores, o primeiro representando o número do aluno e o segundo representando 
sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número 
do aluno mais alto e o número do mais baixo, junto com suas alturas."""

counter = tall = small = 0
num_tall = num_small = 0
while counter < 10:
    num = int(input("\nNúmero do aluno: "))
    alt = float(input("Altura do aluno (em metros): "))
    counter +=1 #contador

    if counter == 1: 
        tall = small = alt
        num_tall = num_small = num
    else:
        if alt > tall: # altura maior que tall(alto)
            tall = alt # alto vai passar a ser igual a altura
            num_tall = num #Número do mais alto
        if alt < small: # altura menor que small(baixo)
            small = alt # baixo vai ser igual a altura
            num_small = num # Número do mais baixo

print("\n📝Resultado:")
print(f"O Aluno número {num_tall} é o mais alto com {tall:.2f} de altura.")
print(f"O Aluno número {num_small} é o mais baixo com {small:.2f} de altura.")