# Set (Lista)
    # Similar a lista
    # Evita itens duplicados
    # Não utiliza index

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.symmetric_difference(set3)


print(set4)


'''
s1 = {1, 2, 3, 4, 5, 6}

s1.add(7)
s1.update([8, 9, 10, 3])
s1.remove(2) # da erro se o numero n existir
s1.discard(0) # se n tiver continua

print(s1)
'''