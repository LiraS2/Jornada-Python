# Python Object-Oriented Programming

# Classes
    # Utilizadas para criar Objetos (instance)
    # Objetos são partes dentro de uma Class (instancias)
    # Classes  são utilizadas para agrupar dados e funções, podendo reutilizar
    # ====
    # Class: Frutas
    # Objects: Abacate, Banana...


# criar a classe
class Funcionarios:
    
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

# criar o objeto
usuario1 = Funcionarios('Maria Rita', 'Brota', '11/06/2007')
usuario2 = Funcionarios('Gabriel', 'Lira', '27/02/2007')
usuario3 = Funcionarios('Thauanny', 'Brota', '25/11/2011')

# print
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)

print('============')

print(usuario2.nome)
print(usuario2.sobrenome)
print(usuario2.data_nascimento)

print('============')

print(usuario3.nome)
print(usuario3.sobrenome)
print(usuario3.data_nascimento)




# # criar os parametros do usuario1         ===Foi Reescrito===
# usuario1.nome = 'Maria Rita'
# usuario1.sobrenome = 'Brota'
# usuario1.data_nascimento = '11/06/2007'

# # criar os parametros do usuario2
# usuario2.nome = 'Gabriel'
# usuario2.sobrenome = 'Lira'
# usuario2.data_nascimento = '27/02/2007'
