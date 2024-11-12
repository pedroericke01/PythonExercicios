#Escrevendo um novo conteúdo em um Arquivo#
#o método 'write()' formata o arquivo tratado desde o zero, e reescreve os caracteres
# passados como parÂmetro#

arquivo = open('dados1.txt', 'w')
print('informações do arquivo:{}'.format(arquivo))


escreve = arquivo.write('Um Sistema Auxiliar, meu nome é Pdr33')
arquivo.close()
