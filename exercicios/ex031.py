km=float(input('Qual a distancia da viagem que voce vai fazer ? em Km  '))

if km <200:
    print('O preço da passagem será R${:.2f}'.format(km*0.50))
else:
    print('Essa passagem custará {:.2f} '.format(km*0.45))