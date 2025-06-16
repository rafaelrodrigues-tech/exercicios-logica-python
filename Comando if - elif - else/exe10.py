# Nota trabalho de Laboratorio vai receber Peso = 2 , Avaliação Semestral vai receber peso = 3 , Exame Final vai receber peso = 5. 
'''Faça um programa que receba as três notas, calcule e mostre a média ponderada e o 
conceito que segue a tabela abaixo:
Média ponderada Conceito
8,0 ~ 10,0 A
7,0 ~ 8,0 B
6,0 ~ 7,0 C
5,0 ~ 6,0 D
0,0 ~ 5,0 E'''

tr_l = float(input('Informe a sua nota de trabalho laboratorial: \n'))
av_s = float(input('Informe a nota da sua Avaliação Semestral: \n'))
ex_f = float(input('Informe a sua nota no Exame Final: \n'))

peso_1 = 2
peso_2 = 3
peso_3 = 5

media_p = (tr_l * peso_1 + av_s * peso_2 + ex_f * peso_3)/(peso_1 + peso_2 + peso_3)

if media_p >= 8.0:
    print(f'A sua média ponderada foi : {media_p:.2f}')
    print('Conceito A')
elif media_p >= 7.0:
    print(f'A sua média ponderada foi : {media_p:.2f}')
    print('Conceito B')
elif media_p >= 6.0:
    print(f'A sua média ponderada foi : {media_p:.2f}')
    print('Conceito C') 
elif media_p >= 5.0:
    print(f'A sua média ponderada foi : {media_p:.2f}')
    print('Conceito D')       
elif media_p >= 0.0:
    print(f'A sua média ponderada foi : {media_p:.2f}')
    print('Conceito E')    
