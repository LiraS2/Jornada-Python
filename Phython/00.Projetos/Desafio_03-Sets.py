# Desafio com 'Sets'

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

car_noite = set(tem_carro) & set(turno_noite)   #poderia usar .intersection
print(f'O(s) funcionario(s) {car_noite} tem carro e trabalha(m) pela noite\n')

car_dia = set(tem_carro) & set(turno_dia)       #poderia usar .intersection
print(f'O(s) funcionario(s) {car_dia} tem carro e trabalha(m) pela manha\n')

no_car = set(funcionarios) - set(tem_carro)     #poderia usar .difference
print(f'O(s) funcionario(s) {no_car} não tem carro e trabalha(m)\n')



