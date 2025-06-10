""" Jeremias possui um cronômetro que  consegue marcar o tempo apenas em segundos. 
Sabendo  disso,  desenvolva  um  algoritmo  que  receba  o  tempo  cronometrado,  em 
segundos,  e  diga  quantas  horas,  minutos  e  segundos  se  passaram  a  partir  do  tempo 
cronometrado."""

print("Cronômetro em Segundos")
seg = int(input("\nDigite o tempo em segundos: "))

hr = seg // 3600 # "//" Hora vai permanecer em número inteiro. 3600 segundos correspodem a 1 hora.
seg_res = seg % 3600 # resto do q vai sobrar das hrs
mn = seg_res // 60
seg_f = seg_res % 60 # segundos restantes

print("Se passaram ",end='')
print(f"{hr} Horas {mn} Minutos e {seg_f} Segundos")



