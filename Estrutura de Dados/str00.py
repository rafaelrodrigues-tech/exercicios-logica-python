print("Digite um texto abaixo ('/exit' para finalizar ):")
words = []
while True:
    word = input("texto: ")
    if word != "/exit":
        words.append(word)
    else:
        print("Texto: ",end="")
        for word in words:
            print(word,end=" ")
        break            
        

