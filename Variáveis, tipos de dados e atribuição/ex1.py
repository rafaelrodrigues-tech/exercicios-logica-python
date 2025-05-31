"""Faça  um  programa  que  receba  quatro 
números inteiros, calcule e mostre a soma desses números."""
num = []
for i in range(0,4):
    num.append(int(input(f"Digite o {i + 1}ª número: ")))

print("Total: ")
print(f"{num[0]} + {num[1]} + {num[2]} + {num[3]} = {sum(num)}")    