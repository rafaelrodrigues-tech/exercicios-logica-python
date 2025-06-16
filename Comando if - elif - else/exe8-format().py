'''Desenvolva um algoritmo que simule uma calculadora. Você deve dar a opção de o 
usuário escolher entre: 1 - Somar; 2 - Subtrair; 3 - Multiplicar; 4 - Dividir. O usuário só 
conseguirá processar dois números inteiros por vez'''

print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir\n')

op = int(input('Operação: '))
x = int(input('Informe o primeiro número: '))
y = int(input('Informe o segundo número: '))

som = x + y
sub = x - y
mul = x * y 
div = x / y

if op == 1:
    print(x,'+',y,'=',som)
if op == 2:
    print(x,'-',y,'=',sub)
if op == 3:
    print(x,'x',y,'=',mul)
if op == 4:
    print(x,':',y,'=',div)            








 


