from datetime import datetime
hoje = datetime.now()

ano = int(input('Digite o ano do seu nascimento'))
idade = hoje.year - ano
if idade == 18:
    print('Voce vai se alistar nesse ano de ',hoje.year)
elif idade < 18:
    print('''Voce nao se alista esse ano, vc se alistará no ano de {}, 
    ou seja daqui a {} anos, vc tem {} '''.format(ano+18,18-2,idade))
else:
    print('Voce Ja passou do periodo de alistamento, vc se alistou no ano de {}'.format(ano+18))