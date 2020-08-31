num=int(input('Digite um numero de 0 a 9999 : '))
print((num//1000)*1000,((num-(num//1000)*1000))//100,num//10-((num//100)*100)//10)
print('esse numero tem: \n {} unidades \n {} dezenas \n {} centenas e \n {} milhares'.format(num-((num//10)*10),num//10-((num//100)*100)//10,((num-(num//1000)*1000))//100,num//1000))
strnum=str(num)
'''fiz de uma forma mo complicada, so para fazer por int'''
'''Abaixo a forma do guanabara, simples e com string tambem, eu so fiz com int'''
nume=int(input('Informa um numero'))
n=str(nume)
print('Unidades : {}'.format(n[3]))
print('Dezena : {}'.format(n[2]))
print('Centena : {}'.format(n[1]))
print('Milhar : {}'.format(n[0]))
