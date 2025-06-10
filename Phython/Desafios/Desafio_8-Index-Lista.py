frutas = ['maçã', 'banana', 'manga', 'uva']

frutas[1] = 'morango'
frutas.append('abacaxi') # add no final

print(frutas)


#             === extra ===
frutas[1:3] = ['abacaxi', 'abacate'] # ignora o limite '3'
print(frutas)
frutas.insert(2, 'abacate') # posicao + objeto
print(frutas)