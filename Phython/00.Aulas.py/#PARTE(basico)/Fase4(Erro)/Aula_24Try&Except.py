# Erro
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

# try:                                 ===AULA 01===
#     letra = ['a', 'b', 'c']
#     print(letra[3])
# except IndexError:
#     print('Index não existe')

try:#                                  ===AULA 02===
    valor = int(input(f'Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print(f'Favor digitar um valor em numeros')

print(f'mais codigo abaixo')
