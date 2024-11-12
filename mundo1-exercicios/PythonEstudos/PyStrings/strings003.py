#metodo 'read()' lê o conteúdo de um arquivo de uma só vez, em uma mesma linha#

arquivo = open('dados1.txt')
print('Informações do Arquivo:{}'.format(arquivo))

conteudo = arquivo.read()
print('Dados do arquivo:{}'.format(type(conteudo)))

print('Conteúdo do Arquivo:{}'.format(repr(conteudo)))
