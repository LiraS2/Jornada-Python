nome = 'Gabriel'
sobrenome = 'Lira'
profissao = 'Vagabundo'

texto = 'O ' + nome + ' ' + sobrenome + ' é um excelente [' + profissao + ']' 

texto2 = f'O {nome} {sobrenome} é um excelente [{profissao}]'

print(texto)
print(texto2)



# TEXTO FUNCIONALIDADES
mensagem = 'Eu adoro comida Caseira'

'''
.lower #minusculo
.upper #MAIUSCULO
.capitalize #Pimeira letra em maiusculo
.find #posicao onde a letra é encontrada
.replace #subtitue algo por outro ('x', 'y') ou ('Caseiro', 'picante')
.strip #remove oq n faz sentido/oq for especificado (da frente para tras)
'''
print(mensagem.strip)