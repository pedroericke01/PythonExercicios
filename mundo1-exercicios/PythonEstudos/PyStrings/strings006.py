#utilizando o loop iterável 'for' para imprimir cada linha do arquivo tratado, poupando
#a larga utilização de recursos computacionais#

arquivo = open('dados1.txt')
print('Informações do Arquivo:{}'.format(arquivo))

for linhas in arquivo:
    print(repr(linhas))

arquivo.close()
