dias = int(input('Digite quantos dias voce ficou com o carro :'))
km = float(input('informe quantos kilometros você andou '))
total = (dias * 60)+(km * 0.15)
print('O carro andando {} dias e {} km tem o custo de aluguel de R${:.2f}'.format(dias, km, total))