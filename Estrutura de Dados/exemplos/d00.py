pessoas = []

print("-"*50)
print("CADASTRO DE PESSOAS".center(50))
print("-"*50)

for _ in range(3):
    pessoa = {}
    pessoa["nome"] = input("Seu Nome: ")
    pessoa["idade"] = int(input("Sua idade: "))
    pessoa["peso"] = float(input("Seu peso: "))
    pessoas.append(pessoa)
    print()
print("¨"*50)
print("\n📝Dados Cadastrados: ")
for pessoa in pessoas:
    print()
    print(f"Nome: {pessoa["nome"]}.")
    print(f"Idade: {pessoa["idade"]} anos.")
    print(f"Peso: {pessoa["peso"]} Kg.")
print("¨"*50)
