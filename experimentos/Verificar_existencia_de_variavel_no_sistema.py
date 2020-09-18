var =str(input('digite o nome da variavel, sem espaços '))

pedra=1
papel=2
tesoura=3


if var in ' '.join(list(globals().keys())):
    print('essa variavel existe no sistema')
else:
    print("variavel nao existe no sistema")

pedra=1
papel=2
tesoura=3
