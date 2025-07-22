lista_produtos = []
maximo = 5
for _ in range(maximo):
    produto = {}
    produto["id"] = int(input("\nNúmero de Identificação(ID): "))
    produto["nome"] = input("Nome: ")
    produto["preço"] = float(input("Preço:R$ "))
    lista_produtos.append(produto)
    
    print("📝Produtos Cadastrados:")
    for produto in lista_produtos:
        print(f"\nID: {produto["id"]}")
        print(f"Nome: {produto["nome"]}")
        print(f"Preço: R${produto["preço"]:.2f}")
    print(f"Produtos Cadastrados: {len(lista_produtos)}")    

    op = input("\nDeseja encerrar a lista?").upper().strip()
    if op == "S":
        break

print("Limite de produtos atingidos (No máximo 5 produtos)")
print("Volte sempre!😁")



