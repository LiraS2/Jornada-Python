# Functions (Funções)             ===P3===
        # DRY - Don't repeat yourself.
        # Parametro --> Argumento
        # Realizam uma tarefa
        # Calcula e retorna um Valor

def cliente1(numero1, numero2):
    print(f'Olá {str(numero1 + numero2)}')

def cliente2(numero1, numero2):
    return f'Olá {str(numero1 + numero2)}'


x = cliente1(1, 2)

y = cliente2(1, 2)

print(x)
print(y)