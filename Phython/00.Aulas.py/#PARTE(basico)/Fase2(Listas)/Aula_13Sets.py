# Set (Lista)
    # Similar a lista
    # Evita itens duplicados
    # Não utiliza index

lista1 = [10, 20, 30 ,40, 50]
lista2 = [10, 20, 60, 70]

num1 = set(lista1)
num2 = set(lista2)

print(len(num1))
#print(num1[0]) n funciona sem index

print(num1 | num2) # Union
print(num1 - num2) # Difference
print(num1 ^ num2) # Symmetric Difference
print(num1 & num2) # And

