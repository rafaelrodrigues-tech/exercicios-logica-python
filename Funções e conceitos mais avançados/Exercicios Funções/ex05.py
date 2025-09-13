"""Sabe-se que o quilowatt de energia custa um 
milésimo  do  salário  mínimo.  Faça  um  procedimento  que  receba  o  valor  do  salário 
mínimo  e  quantidade  de  quilowatts  consumida  por  uma  residência.  O  procedimento 
deve calcular e retornar através de passagem de parâmetros por referência: 
 
 a) o valor, em reais, de cada quilowatt; 
 b) o valor, em reais, a ser pago por essa residência; 
 c) o valor, em reais, a ser pago com desconto de 15%. 
 
Sabendo  disso,  desenvolva  um  algoritmo  que  peça  para  o  usuário  inserir  o  valor  do 
salário mínimo e a quantidade de quilowatts consumida. Invoque o respectivo 
procedimento e mostre, na tela, as informações dos itens a), b) e c). """
def calculando_quilowatts(salario_minimo):
    cada_quilowatts =  salario_minimo/1000 #a
    return cada_quilowatts

def calculando_valor_residencia(qtdd_quilowatts,cada_quilowatts):
    reais = cada_quilowatts * qtdd_quilowatts #b
    return reais

def calculando_desconto(reais):
    desconto = reais - (reais * 15 / 100)#c
    return desconto

salario_minimo = float(input("Informe o seu salário minimo: "))
qtdd_quilowatts = float(input("Quantidade de quilowatts consumida: "))

cada_quilowatts = calculando_quilowatts(salario_minimo)
print(f"\nValor de 1 KW (em R$) : R${cada_quilowatts:.2f}")

reais = calculando_valor_residencia(qtdd_quilowatts,cada_quilowatts)
print(f"Valor a ser pago: R${reais:.2f}")

desconto = calculando_desconto(reais)
print(f"Com o desconto de 15%, o valor passa a custar: R${desconto:.2f}")
