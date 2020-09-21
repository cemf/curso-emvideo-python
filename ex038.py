n1 = float(input('Digite um numero'))
n2 = float(input('Digite outro numero '))

if n1 > n2:
    print('O numero {} é maior que {}'.format(n1,n2))
elif n2 > n1:
    print('O numero {} é maior que {} '.format(n2,n1))
else:
    print('Os dois valores sao iguais {} e {} '.format(n1, n2))
