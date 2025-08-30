""" Faça um programa que seja capaz de armazenar os dados de um produto: código, nome, 
valor e quantidade. Seu programa deve ser capaz de armazenar 5 produtos. Ao final dos 
cadastros,  o  usuário  deve  inserir  o  código  de  um  produto  e  o  seu  programa  deve 
imprimir,  na  tela,  as  informações  daquele  produto.  Caso  o  produto  não  se  encontre 
cadastrado, deve-se informar ao usuário a seguinte mensagem: "código não 
encontrado". """

produtos = []
print("~"*35)
print("SUPERMARKET".center(35))
print("~"*35)
for i in range(2):
    produto = {}
    produto["codigo"] = int(input("\nCódigo do produto: "))
    produto["nome"] = str(input("Nome do produto: "))
    produto["valor"] = float(input("Preço:R$ "))
    produto["quantidade"] = int(input(f"Quantos deseja comprar? "))
    produtos.append(produto)

codigo_produto = int(input("\nInsira o código do produto: "))
achou = False

for produto in produtos:
    if codigo_produto == produto["codigo"]:
        achou = True
        total = produto["valor"] * produto["quantidade"]
        print(f"\nCódigo: {produto["codigo"]}")
        print(f"Produto: {produto["nome"]}")
        print(f"Preço: R$ {produto["valor"]}")
        print(f"Quantidade: {produto["quantidade"]}")
        print(f"\nTotal: R$ {total:.2f}")
        break

if not achou:
    print("Código não encontrado.")

        


