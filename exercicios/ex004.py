coisa = input('digite algo ')
tipo=type(coisa)
print('É alfa numerico ? {} \n É numero?{} \n é letra? {} \n é minusculo ? {} \n tipo ? {}'.format(coisa.isalnum(), coisa.isnumeric(),coisa.isalpha(), coisa.islower(), tipo))