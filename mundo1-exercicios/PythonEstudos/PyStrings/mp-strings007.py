#concatenando Strings com um caractere desejado e o método 'join()', para efetuar a
# correta concatenação desejada, ultilizamos o metodo 'split()' para auxiliar no resultado
# final desejado#

nome = 'pedro ericke marques gomes'
print('Nome:{}'.format(nome))

print('Nome Formatado:{}'.format('.'.join(nome.split())))
