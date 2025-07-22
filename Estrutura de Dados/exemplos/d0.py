pessoa = {
    "nome" : "Teste",
    "peso" : 0.0,
    "idade" : 0
}

print("Dados da pessoa: ")
print(f"Nome: {pessoa["nome"]}")
print(f"Peso: {pessoa["peso"]}")
print(f"Idade: {pessoa["idade"]}")

pessoa["nome"] = "Texto"
pessoa["peso"] = 99.99
pessoa["idade"] = 10

print("\nDados atualizados:")
print(f"Nome: {pessoa["nome"]}")
print(f"Peso: {pessoa["peso"]}")
print(f"Idade: {pessoa["idade"]}")

pessoa["nome"] = input("\nDigite seu nome: ")
pessoa["peso"] = float(input("Digite seu peso: "))
pessoa["idade"] = int(input("Digite sua idade: "))

print("\nDados atualizados:")
print(f"Nome: {pessoa["nome"]}")
print(f"Peso: {pessoa["peso"]:.2f} Kg")
print(f"Idade: {pessoa["idade"]} anos")
