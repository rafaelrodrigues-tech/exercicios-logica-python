'''Desenvolva um algoritmo que receba dois números, calcule e mostre a multiplicação 
entre eles, se ambos forem iguais. Caso o primeiro seja maior que o segundo, mostre a 
subtração do primeiro pelo segundo. Caso contrário, mostre a soma entre os dois.'''

# Entrada dos números:
x = int(input('Informe o primeiro número: \n'))
y = int(input('Informe o segundo número: \n'))

mul = x * y
sub = x - y
som = x + y

if x == y:
    print(x,'x',y,'=',mul)
if x > y:
    print(x,'-',y,'=',sub)
if x < y:
    print(x,'+',y,'=',som)





    
