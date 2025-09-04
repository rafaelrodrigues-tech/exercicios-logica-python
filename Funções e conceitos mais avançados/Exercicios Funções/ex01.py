""" O  custo  de  um  carro  novo  ao  consumidor 
final é o preço de fábrica somado ao percentual de lucro do distribuidor, acrescido dos 
impostos  aplicados  ao  preço  de  fábrica.  Faça  um  programa  que  receba  o  preço  de 
fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos. 
Em cada item, crie uma função distinta para calcular e retornar: 
 
 a) o valor correspondente ao lucro do distribuidor; 
 b) o valor correspondente aos impostos; 
 c) o preço final do veículo. """

def lucro_distribuidor(preco_fabrica,percentual_distribuidor):
    lucro = preco_fabrica * (percentual_distribuidor / 100)
    return lucro

def impostos(preco_fabrica,percentual_impostos):
    imposto = preco_fabrica * (percentual_impostos / 100)
    return imposto

def preco_final(preco_fabrica,lucro,imposto):
    valor_final = preco_fabrica + lucro + imposto
    return valor_final

preco_fabrica = float(input("Informe o preço de fábrica: "))
percentual_distribuidor = float(input("Percentual do distribuidor: "))
percentual_impostos = float(input("Percentual dos impostos: "))


lucro = lucro_distribuidor(preco_fabrica,percentual_distribuidor)
print(f"Lucro Distribuidor: {lucro}")

imposto = impostos(preco_fabrica,percentual_impostos)
print(f"Impostos: {imposto}")

valor_final = preco_final(preco_fabrica,lucro,imposto)
print(f"Preço do veículo: {valor_final}")