vel=float(input('Digite a velocidade do carro:'))

if vel>80:
    print('Voce foi multado em R${:.2F}'.format((vel-80)*7))

print('Tenha um bom dia')
