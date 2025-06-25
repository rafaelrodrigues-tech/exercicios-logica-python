"""2) Desenvolva um algoritmo que receba dois números inteiros positivos A e B. Exiba na tela 
todos  os  números  inteiros  compreendidos  entre  A  e  B,  excluindo  os  próprios  A  e  B. 
Suponha que o usuário respeite o enunciado e insira valores válidos para A e B."""

a = int(input("Digite um número inteiro: "))
b = int(input("Agora, Digite outro: "))

# a = 1, b = 5, vai printar= 2,3,4

i = a + 1
while i < b:
    print(i,end=" ")
    i += 1
