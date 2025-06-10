# Lista
    # Armazenar mais de uma informação em variáveis
    # Manter a sequancia dos dados em uma variável

cor_cliente = input('Digite a cor desejada: ')
cores_estoque = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower().strip() in cores_estoque:
    print('Em estoque')
else:
    print('Não temos esta cor em estoque')