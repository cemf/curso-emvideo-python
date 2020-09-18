n1 = float(input('Digite o 1o numero :'))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('diGite o 3o nUmero : '))
numeros = [n1, n2, n3]
numeros.sort()
print('O maior desses 3 numeros é {} e o menor é {} '.format(numeros[2], numeros[0]))
'''Modo guanabara'''
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
elif n3 < n2 and n3 < n1:
    menor = n3
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
elif n3 > n2 and n3 > n1:
    maior = n3
print('O maior numero é {} e o menor é {}'.format(maior, menor))
