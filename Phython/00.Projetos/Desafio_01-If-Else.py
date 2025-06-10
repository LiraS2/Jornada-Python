# Desafio com If. Elif, Else

temperatura_C = int(input('Could you please tell me the temperature of the steak in Celsius? '))

if temperatura_C<=47:
    print(f'in the {temperatura_C}°C steak is Raw')
elif temperatura_C in range(48,53):     #48<=temperatura_C<=53:
    print(f'in the {temperatura_C}°C steak is Rare')
elif temperatura_C in range(54,59):     #54<=temperatura_C<=59:
    print(f'in the {temperatura_C}°C steak is Medium rare')
elif temperatura_C in range(60,64):     #60<=temperatura_C<=64:
    print(f'in the {temperatura_C}°C steak is Medium')
elif temperatura_C in range(65,70):     #65<=temperatura_C<=70:
    print(f'in the {temperatura_C}°C steak is Medium well')
elif temperatura_C in range(71,78):     #71<=temperatura_C<=78:
    print(f'in the {temperatura_C}°C steak is Well done')
else:
    print(f'in the {temperatura_C}°C steak is Overcooked')