n = int(input('Digite um numero : '))
converter = str(input('Digite para qual base deseja converter esse numero (binario, octal ou hexa) :'))
if converter == "binario":
    num_conv = bin(n)
elif converter == "octal":
    num_conv = oct(n)
elif converter == "hexa":
    num_conv = hex(n)
else:
    num_conv = ''
    print('voce digitou uma conversao invalida')

print('O numero que voce digitou {} em base {} é igual a {}'.format(n, converter, num_conv[2:]))
