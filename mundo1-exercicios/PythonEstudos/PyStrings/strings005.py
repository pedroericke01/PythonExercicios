#o método 'ReadLines()', converte todos as strings em lista, e cada linha da string
#será como um índice da lista#

arquivo = open('dados1.txt')
print('Informações do Arquivo:{}'.format(arquivo))

conteudo = arquivo.readlines()
print('Dados do Arquivo:{}'.format(type(conteudo)))
print('conteúdo do Arquivo:{}'.format(repr(conteudo)))
