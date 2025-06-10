# Erro
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro


try:
    valor = int(input(f'Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print(f'Favor digitar um valor em numeros')
finally:
    print('codigo ok')# faz com ou sem erro



# else:
#     print('Esse é meu catalogo por esse valor')
#     resultado = valor * 2
#     print(resultado)

print(f'mais codigo abaixo')