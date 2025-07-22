# Listas:
lista = []
print('Lista: ',lista)
print('\n')


lista.append(10)
print('lista.append: ',lista)
print('\n')


iteravel = [20,30,40]
lista.extend (iteravel)
print('lista.extend([20,30,40]) ',lista)
print('\n')


lista.insert(0,999)
print('lista.insert(0,999)',lista)
print('\n')


lista.remove(999)
print('lista.remove(999)',lista)
print('\n')


indice = lista.index(30)
print('lista.index(30)',indice)
print('\n')


dado = lista.pop()
print('lista.pop()',dado)
print('lista: ',lista)
print('\n')


dado = lista.pop(1)
print('lista.popo(1)',dado)
print('lista: ',lista)
print('\n')


cont = lista.count(20)
print('lista.count(20)',cont)
print('lista: ',lista)
print('\n')


lista.reverse()
print('lista.reverse() ',lista)
print('\n')


lista.sort()
print('lista.sort()',lista)
print('\n')


cont = len(lista)
print('len(lista): ',cont)
print('\n')


soma = sum(lista)
print('sum(lista): ',soma)
print('\n')


lista.clear()
print('lista.clear(): ',lista)
print('\n')



