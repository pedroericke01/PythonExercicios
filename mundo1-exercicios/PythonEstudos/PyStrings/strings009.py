#Adicionando nova informação a um arquivo, no final do mesmo, através da declaração do
#'Append()', no metodo de entrada ao arquivo. ('a').
#Dessa maneira, o Arquivo não será Resetado desde o ínicio, apenas será acrescentada essa
#nova informação#

arquivo = open('dados1.txt', 'a')
print('informações do arquivo:{}'.format(arquivo))

adicionar = arquivo.write('\nBem vindos a Happy Lândia')
arquivo.close()
