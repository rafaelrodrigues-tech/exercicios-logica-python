'''Desenvolva um algoritmo que peça para que o usuário informe a base e a altura de um 
retângulo, e um terceiro número inteiro "op". Caso o usuário escolha "op" igual a 0, 
calcule e mostre o perímetro do retângulo. Caso o usuário insira um valor 1 para "op", 
calcule e mostre a área do retângulo. Se o usuário inserir um valor diferente de 0 e 1 
para "op", mostrar a mensagem "Opção inválida."'''

print('0 - Perímetro ')
print('1 - Área ')

op = int(input('Informe a operação: '))

# Entrada de dados númericos:
base = float(input('Informe a base: \n'))
altura = float(input('Informe a altura: \n'))

# 'p' vai calcular o perímetro do retângulo. 
# 'a' vai calcular a área do retângulo.
p = 2 * (base+altura)
a = base * altura

if op == 0:
    print('O perímetro do retângulo é: ',p)
elif op == 1:
    print('A área do retângulo é: ',a)

else: 
    print('opção inválida')    