# Python Object-Oriented Programming

# Classes
    # Utilizadas para criar Objetos (instance)
    # Objetos são partes dentro de uma Class (instancias)
    # Classes  são utilizadas para agrupar dados e funções, podendo reutilizar
    # ====
    # Class: Frutas
    # Objects: Abacate, Banana...


# criar a classe
class Funcionarios:#                or pass(vazia)
    pass

# criar o objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

# criar os parametros do usuario1
usuario1.nome = 'Maria Rita'
usuario1.sobrenome = 'Brota'
usuario1.data_nascimento = '11/06/2007'

# criar os parametros do usuario2
usuario2.nome = 'Gabriel'
usuario2.sobrenome = 'Lira'
usuario2.data_nascimento = '27/02/2007'

# print
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)

print('============')

print(usuario2.nome)
print(usuario2.sobrenome)
print(usuario2.data_nascimento)