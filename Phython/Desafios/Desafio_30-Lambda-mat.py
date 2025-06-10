mult = lambda nb_1, nb_2 : nb_1 * nb_2

n1_user = int(input('Isso é uma multiplicação me diga os dois numeros dela: '))
n2_user = int(input('E qual o segundo numero: '))

print(f'O valor da multiplicação de {n1_user} por {n2_user} é 
      {mult(n1_user,n2_user)}')