#utilizando o metodo: "write()" duas vezes, é possível inserir 2
#informações no mesmo arquivo em uma mesma iteração.#

#"as == nova nomeação para o 'dados1.txt' "

with open('dados1.txt', 'w') as arquivo:
    print('Informações do Arquivo:{}'.format(arquivo))
#e1
    arquivo.write('Olá mundo')
#e2
    arquivo.write('\nHappy Lândia')
#fechamento do arquivo.#
    arquivo.close()