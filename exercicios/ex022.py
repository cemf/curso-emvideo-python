nome=str(input('Digite seu nome completo : '))
masc=nome.upper()
mins=nome.lower()
sep=nome.split()
print('''Nome com maiusculas: {} 
Nome com tudo minusculo {}
O nome tem {} letras e 
O primeiro nome, {},  tem {} letras'''.format(masc,mins,len(''.join(sep)),sep[0], len(sep[0])))
'''Na 1ª resoluçao do guanabara, achei que criou uma complexidade desnescessaria, no input colocou o .strip() e no numero de letras colocou
 len(nome)-nome.count(' ') , isso apenas para remover todos os espaços,
Me parece muito mais facil transformar em lista e juntar de novo, isso remove ja todos os espaços, 
pareceu que ele fez isso para fazer tudo com apenas uma variavel '''