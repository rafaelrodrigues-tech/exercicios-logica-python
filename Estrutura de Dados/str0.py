nome = str(input("Nome: "))
sobrenome = str(input("Sobrenome: "))

nome_sobrenome = nome +" "+ sobrenome 
comp_nome = len(nome)
comp_sob = len(sobrenome)
comp_nomesob = len(nome_sobrenome)

print(f"\nSeu nome completo : {nome_sobrenome}")
print(f"Seu nome completo tem {comp_nomesob} letras.")
print(f"Seu nome tem {comp_nome} letras.")
print(f"Seu sobrenome tem {comp_sob} letras.")