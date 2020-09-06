ano = int(input('Digite um ano : '))

if ano%400 == 0:
    print('o ano {} é bissexto'.format(ano))
elif ano%4 ==0 and ano % 100 >0:
    print('o ano {} é bissexto'.format(ano))
else:
    print('o ano {} nao é bissexto '.format(ano))