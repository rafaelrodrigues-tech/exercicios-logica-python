"""Desenvolva um algoritmo que receba três números. O algoritmo deve imprimir 
"Condição satisfeita", na tela, caso o primeiro dado inserido seja maior do que os outros 
dois  (o  primeiro  não  pode  ser  igual  a  nenhum).  Caso  contrário,  deve  ser  impressa  a 
mensagem: "Erro"."""

print("Informe os números a seguir:")
n = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))

if n > n2 and n > n3:
    print("Condição Satisfeita")
else:
    print("ERRO")    
    