# Array (Matriz)
from array import array
    # Similar a listas
    # Melhor performance

letras_u = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras_u)
print(numeros_i)
print(numeros_f)

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2])

print(letras)
print(numeros_i)
print(numeros_f)
