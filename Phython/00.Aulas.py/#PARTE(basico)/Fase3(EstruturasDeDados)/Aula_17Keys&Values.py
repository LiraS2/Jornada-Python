# Dicionários
    # Utiliza index no formato de Keys e Values
    # Aceita string, integer, float, bloolean...

aluno = {'nome': 'Gabriel',
        'idade': 16,
        'nota_final': 9.2,
        'Aprovação': True, 
        'materias': ['fisica', 'matematica', 'ingles']
        }

print(len(aluno))

print(aluno.items())
#print(aluno.keys())
#print(aluno.values())
print(aluno.get('materias'))