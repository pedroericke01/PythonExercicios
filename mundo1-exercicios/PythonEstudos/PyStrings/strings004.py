#o metodo 'readline()' lê o conteúdo do arquivo, uma linha por vez#

arquivo = open('dados1.txt')
print('Informações do Arquivo:{}'.format(arquivo))

conteudo = arquivo.readline()
print('Dados do Arquivo:{}'.format(type(conteudo)))

print('Conteúdo da primeira linha do arquivo:{}'.format(repr(conteudo)))
