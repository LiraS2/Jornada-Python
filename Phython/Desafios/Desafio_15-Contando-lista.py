frutas = ['maçã', 'morango', 'maçã', 'uva', 'maçã', 'pera']
qual = input('Em q fruta vc esta interessado:')
quantidade = 0

for x in frutas:
    if qual in x:
        quantidade += 1
        
print(f'Nos temos {quantidade} {qual}')