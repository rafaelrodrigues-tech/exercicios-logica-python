"""Desenvolva  um  algoritmo  que  simule  uma  calculadora.  Você  deve  dar  a  opção  de  o 
usuário escolher entre: 1 - Somar; 2 - Subtrair; 3 - Multiplicar; 4 - Dividir. O usuário só 
conseguirá processar dois números inteiros por vez."""

n = float(input("Digite um número: "))
n2 = float(input("Digite o segundo número: "))

print("Escolha uma opção abaixo:")
print("""
1 - SOMAR.
2 - SUBTRAIR.
3 - MULTIPLICAR.
4 - DIVIDIR.
""")
op = int(input("Qual operação deseja? "))
if op == 1:
    print(f"{n} + {n2} = {n + n2}")
elif op == 2:
    print(f"{n} - {n2} = {n - n2}")
elif op == 3: 
    print(f"{n} x {n2} = {n * n2}")
elif op == 4:
    if n2 != 0:
        print(f"{n} / {n2} = {n // n2}")
    else:
        print("Divisão por zero!")
    
              
