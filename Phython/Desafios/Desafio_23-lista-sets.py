#  DIFFERENCE
#  INTERSECTION
#  UNION


amigos_1 = {'Rita', 'Gabriel', 'Cristiane', 'Fabio', 'Thauane'}


amigos_2 = {'Pedro', 'Rita', 'Joao', 'Gabriel', 'Miguel'}




similaridade1 = amigos_2.intersection(amigos_1)

similaridade2 = amigos_2.difference(amigos_1)

similaridade3 = amigos_2.union(amigos_1)


print(similaridade1)
print('-')
print(similaridade2)
print('-')
print(similaridade3)