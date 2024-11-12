#contando o total de linhas válidas/com conteúdo no arquivo,
# desconsiderando linhas sem conteúdo. para esse fim, criamos o
# seguinte algoritmo.#

with open('dados1.txt', 'r') as arquivo:
    num_linhas = 0
    for linhas in arquivo:
        if linhas.split():
            num_linhas += 1

    print('O numero de linhas válidas no arquivo:{}'.format(num_linhas))
    print('Fim do programa!')
    