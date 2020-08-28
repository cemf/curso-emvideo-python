frase = ' Curso em Video Python '
print(frase.capitalize(), frase.lower().title(), frase.lower().title().replace('Em', 'em'))
print('Curso ' in frase, frase.find('Curso'))
print(frase.split())
separado=frase.split()
print(separado,"  ".join(separado))
