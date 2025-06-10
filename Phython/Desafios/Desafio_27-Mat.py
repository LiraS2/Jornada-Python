def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    


U_num = int(input('escolha uma numero que você quer descobrir o fatorial dele: '))


print(f'O fatorial de {U_num} é igua a {fatorial(U_num)}')
