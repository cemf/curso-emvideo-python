from datetime import datetime
hoje = datetime.now()

ano = int(input('Digite o ano do seu nascimento'))
idade = hoje.year - ano
if idade == 18:
    print('Voce vai se alistar nesse ano de ',hoje.year)
elif idade < 18:
    print('Voce nao se alista esse ano, vc se alistará no ano de {}'.format(ano+18))
else:
    print('Voce Ja passou do periodo de alistamento, vc se alistou no ano de {}'.format(ano+18))