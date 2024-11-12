nome = str(input('Digite seu nome:')).strip()
print(nome)
print(len(nome) - nome.count(' '))

print('Seu nome tem Silva?{}'.format('SILVA' in nome.upper()))
