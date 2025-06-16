# Recebe os três números em ordem crescente
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número (maior que o primeiro): "))
num3 = float(input("Digite o terceiro número (maior que o segundo): "))

# Recebe o quarto número
num4 = float(input("Digite o quarto número: "))

# Verifica se os três primeiros números estão em ordem crescente
if num1 < num2 < num3:
    # Coloca o quarto número na posição correta
    if num4 >= num3:
        # Se o quarto número for maior ou igual ao terceiro, ele fica na primeira posição
        num1, num2, num3, num4 = num4, num1, num2, num3
    elif num4 >= num2:
        # Se o quarto número for maior ou igual ao segundo, ele fica na segunda posição
        num1, num2, num3, num4 = num1, num4, num2, num3
    else:
        # Caso contrário, ele fica na terceira posição
        num1, num2, num3, num4 = num1, num2, num4, num3
else:
    print("Os três primeiros números não estão em ordem crescente.")

# Mostra os quatro números em ordem não-crescente
print("Os números em ordem não-crescente são:", num1, num2, num3, num4)
