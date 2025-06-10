# Map Function                                                                 pesquise *built-in functions in python*
    # Muito utilizado com listas
    # Aplicar uma função a uma Iterble, por item. (list, tuple, dic, etc.)

lista1 = [1, 2, 3, 4]

#def multi(x):      ===substituido por lambda===
#    return x * 2

#lista2 = map(lambda x: x * 2, lista1) ===empurrado para baixo===

print(list(map(lambda x: x * 2, lista1)))