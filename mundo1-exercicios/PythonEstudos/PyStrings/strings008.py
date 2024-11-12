#é possível inserir str assim como no metodo 'write()', a unica diferença é que
# no metodo 'writelines()' é possível inserir listas organizadas.#

arquivo = open('dados1.txt', 'w')
print('Informações do Arquivo:{}'.format(arquivo))

escrever = arquivo.writelines(list(str(['melancia', 'limão', 'uva'])))
arquivo.close()
