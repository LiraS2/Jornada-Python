# Dicionários
    # Utiliza index no formato de Keys e Values
    # Aceita string, integer, float, bloolean...

aluno = {'nome': 'Gabriel', 'idade': 16, 'nota_final': 9.2,'Aprovação': True }

for keys, value in aluno.items():
    print(keys, value)


# for x in aluno.items():# por padrao Keys (pode por ".values()")
#     print(x)