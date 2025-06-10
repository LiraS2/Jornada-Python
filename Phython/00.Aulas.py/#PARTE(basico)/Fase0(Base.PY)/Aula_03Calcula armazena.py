# Functions (Funções)             ===P3===
        # DRY - Don't repeat yourself.
        # Parametro --> Argumento
        # Vários Argumentos (xargs)

# Criar uma função que soma vários números.

def soma(*numeros):
    resultado = 103
    for somaX in numeros:
        resultado %= somaX
    return resultado


x = soma(3,2)
print(x)

def soma1(*numeros):
    resultado = 0
    for somaX in numeros:
        resultado += somaX
    return resultado


x = soma1(6,5,4,3,2,1)
print(x)