n1 = float(input('Digite e primeira nota'))
n2 = float(input('Digite e segunda nota'))
media = (n1+n2)/2
if media < 5 :
    print('Lamento, aluno reprovado')
elif media>5 and media < 6.9:
    print('O aluno esta com media {} e esta de recuperaçao'.format(media))
elif media >= 7 :
    print('Parabens, voce foi aprovado com media {}'.format(media))
