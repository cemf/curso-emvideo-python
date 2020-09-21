var =str(input('digite o nome da variavel, sem espaços '))

pedra=1
papel=2
tesoura=3
nome = 'joao'
idade = 25

if var in ' '.join(list(locals().keys())):
    print('essa variavel existe no sistema')
else:
    print("variavel nao existe no sistema")
