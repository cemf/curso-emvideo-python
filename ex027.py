nome=str(input('Digite o seu nome: ')).strip()
n=nome.split()
print('Seu primeiro nome é {}, seu ultimo nome é {}'.format(n[0], n[len(n)-1]))
