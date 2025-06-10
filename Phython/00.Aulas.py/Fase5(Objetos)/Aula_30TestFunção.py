from datetime import datetime
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
        self.ano_nascimento = data_nascimento

    def nome_completo(self):
        return (self.nome + ' ' + self.sobrenome)

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

# criar o objeto
usuario1 = Funcionarios('Maria Rita', 'Brota', 2007)
usuario2 = Funcionarios('Gabriel', 'Lira', 2007)
usuario3 = Funcionarios('Thauanny', 'Brota', 2012)


# print
print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))
print(Funcionarios.idade_funcionario(usuario3))