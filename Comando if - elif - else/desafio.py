'''Crie um programa que receba o nome e a idade de uma pessoa. caso a idade seja maior ou igual a 18, imprimir o nome da pessoa e informar, na tela , que ela é maior de idade.
 caso contrario, não imprimir o nome e informar que a pessoa é menor de idade'''

nome = input("Por Favor, Digite o seu nome: \n")
idade = int(input("Agora, Digite a sua idade: \n"))

if idade >= 18: 
    print(f"Você é maior de idade {nome}",f"sua idade é {idade} anos")
else: 
    print("Você não é maior de idade",f"Não é permitido {idade} anos")    
