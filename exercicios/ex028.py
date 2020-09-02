from random import randint

numero = randint(0,5)
guess = int(input('chute um numero de 0 a 5: '))
if guess == numero:
    print('Parabens, voce acertou, o numero era {} e vc digitou {}'.format(numero,guess))
else:
    print('Errou !, o numero era {}'.format(numero))




'''Versao divertida de jogo da senha abaixo'''
'''while guess != numero:
    guess = int(input('tente de novo'))
else:
    print('parabens, acertou, era o numero {}'.format(numero))'''