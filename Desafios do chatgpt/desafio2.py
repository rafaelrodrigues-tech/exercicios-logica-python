'''Desafio: Números Primos
Escreva um programa que receba um número inteiro N e determine se ele é um número primo ou não.

📌 Regras:

Um número primo é aquele que só é divisível por 1 e por ele mesmo.
O programa deve verificar se N é primo e exibir a resposta.'''

print("NÚMERO PRIMO")
n = int(input("Digite um número: "))
for i in range(1,11):
    if n % i == n and n % i == 1:
        print(f"{n} É Primo!")
        