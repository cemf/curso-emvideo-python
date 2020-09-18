prec_casa = float(input('Digite o preco da casa : R$ '))
salario = float(input('Digite o seu salario: R$ '))
anos = int(input('Digite em quantos anos voce deseja pagar '))

parcelas=prec_casa/(anos*12)

if parcelas < salario*0.3:
    print('Emprestimo aprovado, o valor das parcelas é {:.2f}'.format(parcelas))
else:
    print('emprestimo negado, pois o valor das parcelas é mais de 30% do salario o preço das parcelas é {:.2f}'.format(
        parcelas))
