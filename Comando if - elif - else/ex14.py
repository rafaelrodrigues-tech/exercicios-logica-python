"""Faça  um  programa  que  receba  a  hora  de 
início de um jogo e a hora final do jogo (cada hora é composta por duas variáveis inteiras: 
hora e minuto). Calcule e mostre a duração do jogo (horas e minutos) sabendo-se que o 
tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e 
terminar no dia seguinte. Observação: utilizar o formato de hora que vai das 00hr00min 
até as 23hr29min"""

print("Dados do ínicio de jogo:")
hi = int(input("Horas: "))
mi = int(input("Minutos: "))

print("\nDados do fim de jogo: ")
hf = int(input("Horas: "))
mf = int(input("Minutos: "))

# Converte tudo pra minutos desde o início do dia
inicio_total = hi * 60 + mi
fim_total = hf * 60 + mf

# Calcula a duração
duracao = fim_total - inicio_total

# Se a duração for negativa, significa que o jogo passou da meia-noite
if duracao < 0:
    duracao += 24 * 60  # Soma 24 horas em minutos

# Converte de volta pra horas e minutos
horas = duracao // 60
minutos = duracao % 60

print("\nResultado obtido:")
print(f"Duração da partida: {horas}hr{minutos}mn")