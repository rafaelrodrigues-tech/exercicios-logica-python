"""Faça um programa que receba três números 
obrigatoriamente  em  ordem  crescente  e  um  quarto  número  que  não  siga  esta  regra. 
Mostre, em seguida, os quatro números em ordem não-crescente."""

print("Adicione os números a seguir em ordem crescente:")
one = int(input("Digite um número: "))
two = int(input("Digite outro número: "))
three = int(input("Digite o terceiro número: "))
four = int(input("Agora digite um número qualquer: "))

numbers = [one,two,three,four]
print(f"Ordem não crescente {sorted(numbers,reverse=True)}")