#cidade[0(inicio_string):5(final_string) // 5 = conjunto de caracteres da palavra 'santo']#

cidade = str(input('Em que cidade voce nasceu?')).strip()
print('O nome da cidade começa com santo:{}'.format(cidade[0:5].upper() == 'SANTO'))
