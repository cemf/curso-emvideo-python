from math import fabs

a = float(input('Digite um lado dos triangulos'))
b = float(input('Digite outro lado dos triangulos'))
c = float(input('Digite ultimo lado dos triangulos'))

if fabs(b-c) < a and a< b+c:
    print('\033[0;36;42mÉ TRIANGULO 1')
elif fabs(a-c) < b and b < a+c:
    print('É TRIANGULO 2')
elif fabs(a-b) < c and c <a+b:
    print('É TRIANGULO 3')
else:
    print('Nao é triangulo, lamento ')

'''guanabara solution'''
if a < b + c and b < a+ c and c < a + b :
    print('É triangulo')
else:
    print('Os seguimentos nao formam reta')