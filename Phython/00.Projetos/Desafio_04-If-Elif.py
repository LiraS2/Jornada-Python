# Desafio com if elif

altura = int(input("Qual é a sua Altura em cm?")) / 100 # pega em CM transforma em M
peso = int(input("Qual é o seu peso em kg?" ))
imc = round(peso/(altura**2),2)

if imc <= 18.5:
    print(f'Com essas medidas seu imc é dado como "magresa"')
elif 18.5 < imc <= 24.9:
    print(f'Com essas medidas seu imc é dado como "normal"')
elif 25 <= imc <= 29.9:
    print(f'Com essas medidas seu imc é dado como "sobrepeso"')
elif 30 <= imc <= 39.9:
    print(f'Com essas medidas seu imc é dado como "obesidade"')
else:
    print(f'Com essas medidas seu imc é dado como "obesidade grave"')