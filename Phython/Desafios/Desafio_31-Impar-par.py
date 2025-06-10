p_ou_i = lambda x: 'par' if x % 2 == 0 else 'impar'

n_user = int(input('Desaja saber se é par ou impar? diga um numero: '))

print(f'O numero {n_user} é {p_ou_i(n_user)}')