def potencia(base, expoente=2):
    return base ** expoente


print('Vamos calcular a potencia de um numero')
U_n_1 = int(input('Qual base você quer: '))
U_n_2 = input('E qual o expoente você quer (default 2): ')

if U_n_2:
    print(f'Potencia de {U_n_1} elevado a {U_n_2} é: {potencia(U_n_1, int(U_n_2))}')
else:
    print(f'Potencia de {U_n_1} elevado a 2 é: {potencia(U_n_1)}')


