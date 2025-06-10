# === While Loops ===

# Excelente para loops dependentes de uma condição.

# Publicar um produto com comissão 10% se for acima de R$20

valor = int(input('Qual o valor do produto em reais?\n').strip())

while valor >= 20:
    valor = (valor * 1.10)
    print(f'O valor final do seu produto será de R${valor}')
    break