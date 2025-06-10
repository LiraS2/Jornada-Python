# Functions (Funções)             ===P3===
        # DRY - Don't repeat yourself.
        # Parametro --> Argumento
        # Vários Argumentos (xargs) identificando o Parametro.

# Criar uma função que armazena numeros e strings (dados)

def agencia(**carro):
    return carro

print(agencia(marca='GT4', cor='Verde', mortor=8.0, placa=1234))
print(agencia(marca='GT4', cor='Rosa', mortor=7.0, placa=6666))
print(agencia(marca='GT4', cor='Preto', mortor=9.0, placa=0000))