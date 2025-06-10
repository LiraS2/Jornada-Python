# Python Object-Oriented Programming

# Classes
    # Utilizadas para criar Objetos (instance)
    # Objetos são partes dentro de uma Class (instancias)
    # Classes  são utilizadas para agrupar dados e funções, podendo reutilizar



# criar a classe
class Funcionarios:
    
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return (self.nome + ' ' + self.sobrenome)


# criar o objeto
usuario1 = Funcionarios('Maria Rita', 'Brota', '11/06/2007')
usuario2 = Funcionarios('Gabriel', 'Lira', '27/02/2007')
usuario3 = Funcionarios('Thauanny', 'Brota', '25/11/2011')


# print
# print(usuario1.self.nome + ' ' + usuario1.sobrenome)
# print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))