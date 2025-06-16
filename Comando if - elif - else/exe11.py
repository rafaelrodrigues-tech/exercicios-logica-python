''' Faça um programa que receba três notas de 
um aluno, calcule e mostre a média aritmética e a mensagem que segue a tabela abaixo. 
Para alunos de exame, calcule e mostre a nota que deverá ser tirada no exame para 
aprovação, considerando que a média no exame é 6,0.
Média aritmética Mensagem
0,0 ~ 3,0 Reprovado
3,0 ~ 7,0 Exame
7,0 ~ 10,0 Aprovado'''

A = int(input('Informe a sua primeira nota: '))
B = int(input('Informe a sua segunda nota: '))
C = int(input('Por fim, Informe a sua última nota: '))


media_a = ( A + B + C )/3

if media_a >= 7.0:
    print(f'Sua Média Aritmética foi: {media_a}') 
    print('Aprovado!')
elif media_a >= 3.0:
    print(f'Sua Média Aritmética foi: {media_a}') 
    print('Exame!')    
else:
    print(f'Sua Média Aritmética foi: {media_a}') 
    print('Reprovado!')    




