preco = float(input('digite o preço do produto : R$'))
modo = input('''Digite c caso o pagamento usando cartao
e qualquer outra coisa se for em dinheiro ou cheque
Lembramos que parcelamentos apenas estao disponiveis por cartao ''')
if modo == 'c':
    vezes = int(input('digite em quantas vezes deseja parcelar , digite 1 para pagamento a vista '))
    if vezes == 2:
        total = preco/vezes
    elif vezes >= 3:
        total = (preco + (preco*(20/100)))/vezes
    else:
        vezes = 1
        total=preco-(preco*(5/100))
    print('''Voce pagara o produto em {} vez(es) de R${:.2f}
A sua compra de {:.2f} saira por {:.2f} com os devidos juros ou descontos aplicados'''.format(vezes,total,preco,total*vezes))
else:
    total = preco - (preco*(10/100))
    print('O produto sairá pelo preço de R${:.2f}'.format(total))
