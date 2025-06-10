def dobro(num):
    return num * 2

def ao_quadrado(num):
    return dobro(num) ** 2

N_user = int(input('Qual numero voçe quer que seja dobrado e elevado ao quadrado, nessa ordem: ')) 

print(f'O valor final é {ao_quadrado(N_user)}') 