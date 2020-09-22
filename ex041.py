from datetime import date
hj = date.today()
nv_atleta = int(input('Digite o ano de nascimento do atleta '))
idade = hj.year - nv_atleta
if idade <= 9 :
    print('Essse atleta esta na categoria MIRIM com idade {} '.format(idade))
elif idade <= 14:
    print('Essse atleta esta na categoria INFANTIL com idade {} '.format(idade))
elif idade <= 19 :
    print('Essse atleta esta na categoria JUNIOR com idade {} '.format(idade))
elif idade <= 25 :
    print('Essse atleta esta na categoria SENIOR com idade {} '.format(idade))
elif idade > 25:
    print('Essse atleta esta na categoria MASTER com idade {} '.format(idade))
