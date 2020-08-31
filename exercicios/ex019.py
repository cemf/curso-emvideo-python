from random import randint, choice

alun1 = input('Digite o nome de um aluno')
alun2 = input('Digite o nome de outro aluno')
alun3 = input('Digite o nome do proximo aluno')
alun4 = input('Digite o nome do ultimo aluno que pode ser escolhido')

aluns= [alun1,alun2,alun3,alun4]

print('O aluno escolhido foi {} '.format(aluns[randint(0, 3)]))
# alternativamente
print('O aluno escolhido foi {} '.format(choice(aluns)))

