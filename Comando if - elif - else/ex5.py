'''Desenvolva um algoritmo que receba três números. O algoritmo deve imprimir 
"Condição satisfeita", na tela, caso o primeiro dado inserido seja maior do que os outros 
Algoritmos do Início ao Fim
dois (o primeiro não pode ser igual a nenhum). Caso contrário, deve ser impressa a 
mensagem: "Erro".
'''

# Recebendo os três números

A = int(input('Por favor, Informe o primeiro número: \n'))
B = int(input('Agora, Informe o segundo número: \n'))
C = int(input('Digite o último número: \n'))

if A > B and A > C and A != B and A != C:
    print('Condição Satisfeita')
else:
    print('Erro')


