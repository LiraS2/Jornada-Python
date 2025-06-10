 # Listas
        # Armazenar mais de uma informação em variáveis
        # Manter a sequencia dos dados em uma variável

'''
numeros = [2, 3, 4, 5]
letras =['a', 'b', 'c', 'd']

numeros.extend(letras)
print(numeros)
'''
itens = ['iten1', 'iten2'], ['iten3', 'iten4']

print(itens[1][0])

''' alguns exemplos de list function
cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Sergipe']
#                 0               1           2           3

cidades.append('Brasilia')      # add final
cidades.remove('Salvador')      # remove 'x'
cidades[1] = "Rita's heart"     # add sobrepondo-se a [x] posição
cidades.insert(2, 'Bahia')      # add na posição [x]
cidades.pop(3)                  # remove [x] posição
cidades.sort()                  # ordem alfabetica

print(cidades)
'''