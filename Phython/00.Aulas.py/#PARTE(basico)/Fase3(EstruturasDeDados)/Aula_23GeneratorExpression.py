from sys import getsizeof # fala o tamanho do objeto

# Generator Expressions
    # Uma forma mais rápida para Listas, dicionários e etc
    # Menos memória alocada
    # Valores em bytes

numeros = [x * 10 for x in range(100000000)]
print(type(numeros))
# print(numeros)
print(getsizeof(numeros))

print('==============')

numeros = (x * 10 for x in range(100000000))
print(type(numeros))
# print(list(numeros))
print(getsizeof(numeros))
