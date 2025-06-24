from random import randint
computador = randint(1,50)
tentativas = 0
print("Tente acertar o número entre 1 a 50")
print("-"*35)
while not tentativas == 5:
    player = int(input("Digite um número: "))
    print("-"*35)
    if player == computador:
        print("\033[32mParabéns, Você conseguiu me vencer.\033[m")
        break
    else:
        print("\033[31mNúmero errado, tente novamente...\033[m")
    tentativas += 1
print("\033[4;33mVocê atingiu o limite de tentativas!\033[m")           


