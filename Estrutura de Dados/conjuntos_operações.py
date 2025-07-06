# add (<elemento>): Adiciona um elemento ao conjunto.
# remove (<elemento>): Remove um elemento específico do conjunto e gera um erro se o elemento não estiver presente.
# discard (<discard>): Remove um elemento do conjunto, mas não gera um erro se o elemento não estiver presente.
# pop(): Remove e retorna um elemento aleatório do conjunto.
# clear(): Remove todos os elementos do conjunto, deixando-o vazio.
# union(<set>): Retorna um novo conjunto contendo a união dos elementos de dois conjuntos.
# intersection (<stet>): Retorna um novo conjunto contendo a intersecção dos dois conjuntos.
# difference (<set>): Retorna um novo conjunto contendo os elementos que estão no primeiro conjunto,mas não no segundo.
# issubset(<set>): Verifica se o conjunto é um subconjunto do conjunto específico.
# issuperset(<set>): Verifica se o conjunto é um superconjunto do conjunto específico.
# isdisjoint(<set>): Verifica se dois conjuntos são disjuntos,ou seja, não tem elemento em comum.
# symmetric_difference(<set>): Retorna um novo conjunto contendo os elementos que estão em um dos conjuntos, mas não em ambos.

conjunto = {10,20,30}
print(f"Conjunto: {conjunto}")
print()

conjunto.add(15)
print(f"conjunto.add(15): {conjunto}")
print()

conjunto.remove(15) # Gera um erro se o elemento não estiver presente.
print(f"conjunto.remove(15): {conjunto}")
print()

conjunto.discard(0) # Remove um elemento sem gerar erros.
print(f"conjunto.discard(0): {conjunto}")
print()

print(f"Conjunto: {conjunto}")
outro_conjunto = {40,50,60}
uniao = conjunto.union(outro_conjunto) # Vai unir o conjunto A com o conjunto B.
print(f"uniao = conjunto.union(outro_conjunto): ({outro_conjunto} ): {uniao}")
print()

print(f"Conjunto: {conjunto}")
outro_conjunto = {20,30,40}
inter = conjunto.intersection(outro_conjunto) # Vai verificar se tem algum número igual do conjunto A no conjunto B.
print(f"inter = conjunto.intersection(outro_conjunto): ({outro_conjunto} ): {inter}")
print()

print(f"Conjunto: {conjunto}")
outro_conjunto = {20,30,40}
diferenca = conjunto.difference(outro_conjunto) # Vai pegar o número do conjunto A que não vai ter no conjunto B.
print(f"diferenca= conjunto.difference(outro_conjunto): ({outro_conjunto} ): {diferenca}")
print()

print(f"Conjunto: {conjunto}")
outro_conjunto = {10,20,30,40,50,60}
e_subconj = conjunto.issubset(outro_conjunto) # Verifica se o conjunto A está presente no conjunto B. 
print(f"e_subconj= conjunto.issubset(outro_conjunto): ({outro_conjunto} ): {e_subconj}")
print()

print(f"Conjunto: {conjunto}")
outro_conjunto = {20,30}
e_superconj = conjunto.issuperset(outro_conjunto) # Verifica se o conjunto A contém elementos do conjunto B.
print(f"e_superconj= conjunto.issuperset(outro_conjunto): ({outro_conjunto} ): {e_superconj}")
print()

print(f"Conjunto: {conjunto}")
outro_conjunto = {40,50,60}
e_disj = conjunto.isdisjoint(outro_conjunto) # Verifica se existe elementos dijuntos(elementos diferentes) entre os conjuntos.
print(f"e_disj= conjunto.isdisjoint(outro_conjunto): ({outro_conjunto} ): {e_disj}")
print()

print(f"Conjunto: {conjunto}")
outro_conjunto = {20,30,40}
diferenca = conjunto.symmetric_difference(outro_conjunto) #Retorna elementos que não tem nd em comum entre os dois conjuntos. .
print(f"diferenca= conjunto.symmetric_difference(outro_conjunto): ({outro_conjunto} ): {diferenca}")
print()

conjunto.clear()
print(f"Conjunto.clear(0): {conjunto}")
print()


