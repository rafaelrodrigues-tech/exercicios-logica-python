"""Desenvolva  um  algoritmo  que  peça  para  o  usuário  inserir  vários  números  inteiros.  O 
algoritmo  deverá  contabilizar  a  quantidade  de  números  positivos  informados.  Caso  o 
usuário digite 0, o algoritmo deve mostrar quantidade contabilizada e encerrar."""
cont = 0
while True:
    num = int(input("Insira um número: "))
    if num > 0:
        cont += 1   
    if not num != 0:
        print(f"Quantidade contabilizada: {cont}")    
        break
