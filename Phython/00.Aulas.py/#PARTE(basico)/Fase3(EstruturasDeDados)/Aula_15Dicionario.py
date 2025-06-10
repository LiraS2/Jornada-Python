# Dicionários
    # Utiliza index no formato de Keys e Values
    # Aceita string, integer, float, bloolean...

aluno = {'nome': 'Gabriel', 'idade': 16, 'nota_final': 9.2,'Aprovação': True }

aluno['nome'] = 'Lira'
aluno.update({'nome': 'Biel', 'nota_final': 10})
#aluno.update({'endereco': 'MR_Coração'})
del aluno['idade']


#print(aluno['ap'])   ===erro===
print(aluno.get('endereco', 'Não existe'))
print(aluno)