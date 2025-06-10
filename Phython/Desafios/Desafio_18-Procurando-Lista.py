caros = ['BMW X6', 'BMW i5', 'BMW i8']
pedido = input('Qual carro o senho esta procurando? ')


if pedido in caros:
    print(f'Interesante, um {pedido}, o carro que o senho deseja esta disponivel sim.')
else:
    print(f'Entendo que o senhor deseje um {pedido}, mas no momento so temos esses: {caros}')
