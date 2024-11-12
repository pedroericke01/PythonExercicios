nome = str(input('Escreva seu nome:')).strip()
print(nome)

print('Seu nome em MAIÚSCULAS:{}'.format(nome.upper()))

print('Seu nome em MINUSCULAS:{}'.format(nome.lower()))

print('Seu nome é composto por:{} caracteres'.format(len(nome) - nome.count(' ')))

nome = nome.split()
print('Seu nome primeiro nome é composto por:{} caracteres'.format(len(nome[0])))

