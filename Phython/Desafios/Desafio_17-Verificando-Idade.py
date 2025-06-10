

idade = int(input('Qual a sua idade? '))


if idade < 13:
    print(f'Você é uma criança')
elif idade <= 19:
    print(f'Você é um adolecente')
else:
    print(f'Você é um adulto')