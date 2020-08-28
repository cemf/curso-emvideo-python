from math import sin,cos,tan, radians
ang = float(input('Digite o angulo : '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print('O seno de {0} é {1:.2f} \n O cosseno de {0} é {2:.2f} \n O valor da tangente de {0} é {3:.2f}'.format(ang, seno, coss, tang))