# Functions {Funções}
    # DRY - Don't repeat yourself.
''''
def somar_dois_dumeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)

def somar_dois_dumeros1():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)

somar_dois_dumeros()
somar_dois_dumeros1()
'''



# Functions (Funções)   ===P1===

# DRY - Don't repeat yourself.
# Parametro --> Argumento
'''
def boas_vindas_Gabriel():
    print('Olá Gabriel Lira!')
    print('Termos 5 laptops em estoque')

def boas_vindas_AmorDaMinhaVida():
    print('Olá Maria Rita!')
    print('Termos 4 laptops em estoque')

def boas_vindas_Thauanny():
    print('Olá Cunhada!')
    print('Termos 2 laptops em estoque')

boas_vindas_Gabriel()
boas_vindas_AmorDaMinhaVida()
boas_vindas_Thauanny()
'''




#                    ===P2===
'''
def boas_vindas(nome, quantidade):
    print(f'Olá {nome}!')
    print(f'Termos {str(quantidade)} laptops em estoque')

boas_vindas('Gabriel', 5)
boas_vindas('Maria Rita', 4)
boas_vindas('Thauanny', 2)
'''




# Functions (Funções)             ===P3===
        # DRY - Don't repeat yourself.
        # Parametro --> Argumento
        # Default = Aquele que você define o valor no parametro
        # Non-Default = Aquele que você não define o valor no parametro

def boas_vindas(quantidade, nome='Pedro'):
    print(f'Olá {nome}!')
    print(f'Termos {str(quantidade)} laptops em estoque')

boas_vindas(5)

boas_vindas(8, 'Maria Rita')

boas_vindas(2, 'Thauanny')
