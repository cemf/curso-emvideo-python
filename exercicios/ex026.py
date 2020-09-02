frase = str(input('Digite uma frase : ')).strip().lower()
a='a'
print('A letra "A" aparece nessa string {} vezes, pela primeira vez na posiçao {} na a ultima {}'.format(frase.count(a), frase.find(a)+1,frase.rfind(a)+1))
