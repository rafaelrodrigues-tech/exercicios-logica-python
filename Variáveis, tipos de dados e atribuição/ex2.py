"""Faça  um  programa  que  receba  três  notas, 
calcule e mostre a média aritmética entre elas."""

notas = [] 
print("Calculo de notas:")

for i in range(0,3):
    notas.append(float(input(f"{i + 1}ª Nota: ")))

print("Média aritmética : ",end='')
print(f"{notas[0]} + {notas[1]} + {notas[2]} = {sum(notas)/ 3}")