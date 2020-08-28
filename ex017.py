from math import hypot

co = float(input('Digite o valor do cateto oposto : '))
ca = float(input('Digite o valor do cateto adjacente : '))
hip = (co ** 2 + ca ** 2) ** (1 / 2)
print('triangulo com cateto oposto {}, adjacente {}, logo, hipotenusa é {:.3f} '.format(co, ca, hip))
print('usando o metodo hypot fica {:.3f}'.format(hypot(co, ca)))