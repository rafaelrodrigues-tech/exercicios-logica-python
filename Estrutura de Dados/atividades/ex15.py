"""Faça um programa que seja capaz de armazenar os dados de uma pessoa: nome, idade, 
peso  e  altura.  Seu  programa  deve  ser  capaz  de  armazenar  5  pessoas.  Ao  final  dos
cadastros,  o  seu  programa  deve  imprimir,  na  tela,  todas  as  informações  de  todas  as 
pessoas. Seu programa deve mostrar, também, o nome da pessoa mais magra, nome da 
pessoa mais baixa e a média das idades de todas as pessoas."""

pessoas = []
print("-"*35)
print("CADASTRO PESSOAL".center(35))
print("-"*35)
# Cadastro de 5 pessoas.
for i in range(5):
    pessoa = {}
    pessoa["nome"] = str(input("Digite o seu nome: "))
    pessoa["idade"] = int(input("Digite a sua idade: "))
    pessoa["peso"] = float(input("Digite o seu peso: "))
    pessoa["altura"] = float(input("Digite a sua altura: "))
    pessoas.append(pessoa)
    soma = sum(pessoas.values("idade"))
    print()

#Exibe 5 pessoas
for i, pessoa in enumerate(pessoas, start=1):
    print(f"\n{i}ª Pessoa Cadastrada:")
    print(f" Nome: {pessoa['nome']}")
    print(f" Idade: {pessoa['idade']} anos")
    print(f" Peso: {pessoa['peso']} kg")
    print(f" Altura: {pessoa['altura']} m")


# encontra pessoa mais magra
pessoa_magra = min(pessoas, key=lambda x: x["peso"])
# encontra pessoa mais baixa
pessoa_baixa = min(pessoas, key=lambda x: x["altura"])
# calcula média de idades
media_idade = sum(p["idade"] for p in pessoas) / len(pessoas)

print("\n📊 Informações:")
print(f"Pessoa de menor peso: {pessoa_magra['nome']} ({pessoa_magra['peso']} kg)")
print(f"Pessoa de menor altura: {pessoa_baixa['nome']} ({pessoa_baixa['altura']} m)")
print(f"Média das idades: {media_idade:.2f} anos")
