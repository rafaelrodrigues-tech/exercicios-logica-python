"""Desenvolva um algoritmo que peça para o usuário informar dois números. Após isso, o 
algoritmo  deve  mostrar  cálculo  o  primeiro  número  elevado  ao  segundo.  Ao  final,  o 
algoritmo deve perguntar se o usuário deseja repetir a operação. Caso o usuário insira 
o  caractere  "s",  o  algoritmo  solicita  novamente  dois  números  e  mostra  novamente  a 
potência do primeiro pelo segundo. Caso contrário, o algoritmo é encerrado."""

while True: 
    num = int(input("Insira um número: "))
    n2 = int(input("Agora, Insira outro número: "))

    print("-"*40)
    print(f"\n{num} elevado a {n2} é igual a {pow(num,n2)}")

    op = input("\nDeseja repetir a operação? ")
    if op.lower() != 's':
        break

print("\n😁Obrigado por usar a Calculadora de Potências.")    