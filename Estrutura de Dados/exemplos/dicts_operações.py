# keys(): Retorna uma lista de todas as chaves(keys) no dicionário.
# values(): Retorna uma lista de todos os valores no dicionários.
# items(): Retorna uma lista de pares chave-valor(keys-values) como tuplas no dicionário.
# popiteam(): Remove e renotar um par chave-valor aleatório do dicionário.
# update(<dict>): Atualiza o dicionário com pares chave-valor de outro dicionário específicado.
# clear(): Remove todos os pares chave-valor do dicionário, deixando-o vazio.
# len(<dict>): Retorna o número de pares chave-valor no dicionário especificado.
# issubset(<chave>, default=None): Verifica se a chave especificada está presente no dicionário e, se não estiver, retorna o valor padrão(default) ou None.
# pop(<chave>, default=None): Remove a chave especificada do dicionário e retorna o valor correspondente.Se a chave não estiver presente,retorna o valor padrão (default) ou gera um erro se default não for especificado.
# fromkeys(<chave>, default=None): Cria um novo dicionário com as chaves especificadas e atribui a todas elas o mesmo valor padrão (default).
# setdefault(<chvae>, default=None): Retorna o valor associado à chave especificada no dicionário,e se a chave não estiver presente, atribui ao valor padrão (default) e a retorna.

dicionario = { 
    "arroz": 10.11,
    "feijao": 15.10, 
    "farinha": 11.11
}
print(f"dicionario: {dicionario}")
print()

print(f"dicionario.keys():{dicionario.keys()}")
print()

print(f"dicionario.values():{dicionario.values()}")
print()

print(f"dicionario.items():{dicionario.items()}")
print()

print(f"dicionario.pop():{dicionario.pop("arroz")}")
print()



