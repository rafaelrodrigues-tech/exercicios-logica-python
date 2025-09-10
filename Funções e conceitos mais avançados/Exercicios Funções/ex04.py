"""Cada  degrau  de  uma  escada  tem  X  cm  de 
altura. Faça uma função que receba essa altura, em centímetros, e a altura que o usuário 
deseja  alcançar  ao  subir  a  escada,  em  metros.  A  função  deve  retornar  o  número  de 
degraus necessários para se atingir a altura desejada (desprezando a altura do próprio 
usuário). Em seguida, crie um algoritmo para que o usuário possa informar os dados de 
entrada da função e, ao final, calcule e mostre o número de degraus."""

def calculando_degraus(altura_degrau,altura_escada):
    altura_desejada = (altura_escada * 100 / altura_degrau)
    return altura_desejada



altura_degrau = float(input("Insira a altura de cada degrau(em cm): "))
altura_escada = float(input("Insira a Altura da escada(em metros): "))

altura_desejada = calculando_degraus(altura_degrau,altura_escada)
print(f"Número de degraus necessários para se atingir a altura desejada: {altura_desejada} ")

