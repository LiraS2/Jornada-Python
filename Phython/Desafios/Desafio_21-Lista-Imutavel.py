
cidades = ('Sao paulo', 'Rio de Janeiro', 'Salvador')

print(cidades)


cidade = str(input('Diga-me o nome de uma cidade do Brasil: '))


if cidade in cidades:
    print('A cidade esta na lista de cidades')
else:
    print('A cidade não está na lista de cidades')