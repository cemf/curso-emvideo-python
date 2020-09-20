import sys
import baseconvert
n = int(input('Digite um numero : '))
converter = str(input('Digite para qual base deseja converter esse numero (binario, octal ou hexa) :'))
if converter == "binario":
    num_conv = baseconvert.base(n, 10, 2, string=True)
elif converter == "octal":
    num_conv = baseconvert.base(n, 10, 8, string=True)
elif converter == "hexa" :
    num_conv = baseconvert.base(n, 10, 16, string=True)
else:
    num_conv = ''
    print('voce digitou uma conversao invalida')

print('O numero que voce digitou {} em base {} é igual a {}'.format(n, converter, num_conv))
