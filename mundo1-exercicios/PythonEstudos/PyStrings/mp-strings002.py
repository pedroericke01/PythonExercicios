#A principio, contando o numero de linhas existentes no arquivo, considerando as linhas
#sem conteúdo como linhas válidas tambem#

#Sabemos que em uma operação válida, linhas sem conteúdo são irrelevantes nas contagens, para isso
#devemos criar um algoritmo para invalidar as linhas sem conteúdo e contar apenas as linhas
#com conteúdos. no proximo script(mp-strgs003)#

with open('dados1.txt') as arquivo:
    num_linhas = 0
    for linha in arquivo:
        if linha:
            num_linhas += 1

    print('Numero Total de linhas:{}'.format(num_linhas))
    print('Fim do programa!')
