# Unpacking Lists
    # Armazenar mais de uma informação em variáveis
    # Manter a sequancia dos dados em uma variável

produtos = ['arroz', 'feijão', 'laranja', 'banana', 5, 6, 7]

item1, *outros, item7  = produtos

print(item1)
print(item7)
print(outros)
#
#  ===For loop===
#
valores = [50, 80, 110, 150, 170]

for x in valores:
    print(f' O valor final do produto é de R${x}.')