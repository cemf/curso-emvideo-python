from datetime import datetime

now = datetime.now()
ano = int(input('Digite um ano, digite 0 para ano atual: '))

if ano == 0:
    ano = now.year

if ano%400 == 0:
    print('o ano {} é bissexto'.format(ano))
elif ano%4 ==0 and ano % 100 >0:
    print('o ano {} é bissexto'.format(ano))
else:
    print('o ano {} nao é bissexto '.format(ano))

'''o guanabara apenas dividiu por 4 para achar o bissexto '''
