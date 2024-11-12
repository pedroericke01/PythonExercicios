frase = str(input('Digite uma frase:')).strip().upper()
print('Analisando...')

print('A letra: A, apareceu:{} vezes'.format(frase.count('A')))

print('A primeira apareceu no índice:{}'.format(frase.find('A')))

frase = len(frase) - frase.count(' ')
print('A ultima apareceu no índice:{}'.format(str(frase.rfind(''))))


