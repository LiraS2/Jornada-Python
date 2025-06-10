# List Comprehension
    # Mais simples de se escrever
    # Utilizado quando você precisa criar uma nova lista a partir de uma existente
    # [expressao for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

# frutas2 = []

chave = input('oq vc esta a procura? ')

# for iten in frutas1:
#     if chave in iten:
#         frutas2.append(iten)

frutas2 = [iten for iten in frutas1 if chave in iten] # === reescrito d forma simplificada ===
print(frutas2)