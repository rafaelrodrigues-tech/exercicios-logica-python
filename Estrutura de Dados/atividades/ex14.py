"""Faça um programa que seja capaz de armazenar os dados de três pessoas: nome, idade, 
peso e altura. Ao final, o algoritmo deve mostrar, na tela, o nome e a idade da primeira 
pessoa e o peso e altura da última pessoa."""
pessoas = []
print("-"*35)
print("CADASTRO PESSOAL".center(35))
print("-"*35)

for i in range(3):
    pessoa = {}
    pessoa["nome"] = str(input("\nDigite o seu nome: "))
    pessoa["idade"] = int(input("Informe a sua idade: "))
    pessoa["peso"] = float(input("Informe seu peso (em KG): "))
    pessoa["altura"] = float(input("Por fim, Informe a sua altura(em M): "))
    pessoas.append(pessoa)

print("-"*35)
print("📝Relatório:")
print(f"Nome da primeira pessoa: {pessoas[0]["nome"]} e a sua idade: {pessoas[0]["idade"]} anos.")
print(f"Peso da última pessoa: {pessoas[2]["peso"]} KG e a sua altura: {pessoas[2]["altura"]} metros.")