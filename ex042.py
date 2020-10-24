
a = float(input('Digite um lado dos triangulos'))
b = float(input('Digite outro lado dos triangulos'))
c = float(input('Digite ultimo lado dos triangulos'))

if a < b + c and b < a+ c and c < a + b :
    if a == b == c :
        print('É um triangulo equilatero com lado {}'.format(a))
    elif a == b !=c or a == c != b or b == c != a:
        print('É um triangulo isoceles de lados {}, {} e {}'.format(a, b, c))
    else:
        print('É triangulo escaleno')
else:
    print('Os seguimentos de reta nao formam triangulo')