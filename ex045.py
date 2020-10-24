from random import randint
itens = ('pedra', 'papel', 'tesoura')
print('''escolha e digite
0 para pedra 
1 para papel 
2 para tesoura 
Qualquer outro digito encerra o programa''')
while True:
    escolha = int(input('escolha : '))
    pc = randint(0, 2)
    if pc == 0 and escolha == 1:
        print('{:=^40}'.format(' GANHOU :D '))
        print('pc escolheu {}'.format(itens[pc]))
    elif pc ==1 and escolha == 2:
        print('{:=^40}'.format(' GANHOU :D '))
        print('pc escolheu {}'.format(itens[pc]))
    elif pc ==2 and escolha == 0:
        print('{:=^40}'.format(' GANHOU :D '))
        print('pc escolheu {}'.format(itens[pc]))
    elif pc==escolha:
        print('{:-^60}'.format(' EMPATOU '))
        print('voce e o pc escolheram {}'.format(itens[pc]))
    elif 0 < escolha > 2  :
        print('voce nao digitou uma opçao valida, mas o computador escolheu a opçao {} so para vc saber,encerrando...'.format(itens[pc]))
        break
    else:
        print('perdeu, vc jogou {} e o computador {}'.format(itens[escolha],itens[pc]))
'''while usado para facilitar testes a soluçao original nao usa operadores logicos e nem loop, fica gigante 
pq esse exercicio é antes da aula de while ...
'''
