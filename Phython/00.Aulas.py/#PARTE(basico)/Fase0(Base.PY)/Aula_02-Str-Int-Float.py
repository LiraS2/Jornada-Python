x = str(3) #text/texto
y = int(4) #integer/inteiro
z = float(5) #float/fração
                            # TESTE
print(x+x) 
print(y+y)
print(z+z)

# TRABALHANDO COM
nome = 'Gabriel'
idade = 17
idade = str(idade) #ou assim
cidade = 'Rio de Janeiro'

print('O ' + nome + ' tem ' + str(idade) + ' e mora na cidade de ' + cidade)

 # O Gabriel tem 17 anos de idade e mora na cidade de Rio de Janeiro


# INTRAGINDO COM O USUARIO
nome = input('Qual é o seu nome: ')
idade = input('Qual é a sua idade: ')
idade = str(idade) #ou assim
cidade = input('Onde você mora: ')

print('O ' + nome + ' tem ' + str(idade) + ' anos de idade e mora na cidade no ' + cidade)

 # O Gabriel tem 17 anos de idade e mora na cidade de Rio de Janeiro


# DIFICULDADES 
ano_nascimento = input('Em que ano você nasceu? ')

idade = 2024 - int(ano_nascimento) # INT na pode ser tabalhado
idade = str(idade)                 # junto a uma STR

print('Você tera ' + idade + ' anos de idade no ano 2024')