#buscando um indice na estrutura de dados:lista contígua;#
#com algoritmo de busca e um input do usuário#

usuario = int(input('Digite o numero Desejado(0<x>10):'))
print('Escolhido:{}'.format(usuario))

lista_nums = list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for num in lista_nums:
    i = 0
    #indice = 0

    while i < len(lista_nums):
        if lista_nums[num] == usuario:
            indice = num
            print('O numero:{}, encontra-se no índice:{}'.format(usuario, indice))
            i = len(lista_nums) + 1
            break
        elif usuario >= len(lista_nums):
            if usuario > len(lista_nums):
                print('Esse numero não existe na lista!')
                i = len(lista_nums) + 1
                break
            else:
                indice = len(lista_nums)
                print('O numero:{}, encontra-se no índice:{}'.format(usuario, indice))
                i = len(lista_nums) + 1
                break
        else:
            i = i + 1

print('Fim do programa!')
