
# Enviar um email com os detalhes a compra online (Maximo 3
# tentativas) para compras confirmadas.


compra_confirmada = True
dados_compra = 'Compra no valor e R$12.50 e entrega confirmada'


for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu email')
        break
else:
    print('Falha na compra')


# === for loop nested ===

    # Outer loop
      # Inner loop

for numero1 in range(1, 6):
    print(f'Produto {numero1}')
    for numero0 in range(11):
        print(numero1, numero0)