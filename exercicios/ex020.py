from random import shuffle

n1 = str(input('Digite o nome de um aluno'))
n2 = str(input('Digite o nome de outro aluno'))
n3 = str(input('Digite o nome de mais um aluno'))
n4 = str(input('Ultimo nome que te peço , por favor : '))

alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('O primeiro aluno a apresentar será {} seguido de {} e depois {} e por ultimo {}'.format(alunos[0], alunos[1], alunos[2], alunos[3]))
print(alunos)

