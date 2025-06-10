
cidades = {
    'Brasil': 'Brasília',
    'França': 'Paris',
    'Japão': 'Tóquio',
    'Austrália': 'Canberra',
    'Canadá': 'Ottawa'
}

usuario = input('Diga o nome de um país: ')


if usuario in cidades:
    print(f'A capital de {usuario} é {cidades[usuario]}')
else:
    print('Desculpe, não temos informações sobre a capital desse país')

