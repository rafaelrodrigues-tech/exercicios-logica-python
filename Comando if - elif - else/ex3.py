"""Faça um programa que receba um número 
inteiro e verifique se esse número é par ou ímpar."""

n = int(input("Informe um número: "))

print("\n📝Resultado:")
if n % 2 == 0:
    print(f"O número {n} é PAR!")
else:
    print(f"O número {n} é ÍMPAR!")    