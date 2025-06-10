# Desafio com Funções

def pintar_area(rendimento, altura, largura):
    print(f'Voce precia de {altura * largura / rendimento} latas de tinta.')

pintar_area(int(input('Qual é o rendimento da sua tinta? ')),
       int(input('Qual é a altura da parede? ')),
       int(input('Qual é a largura da parede? '))
       )
