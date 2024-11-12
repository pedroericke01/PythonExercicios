#inserindo um novo elemento na estrutura de dados:Lista Contígua(seus bits em mmemória sao
#armazenados sequencialmente/adjascente)#
#criamos um algoritmo de busca com os seguintes objetivos:
#1-verificar se existe algum elemento semelhante ao digitado pelo usuário(ñ pode existir)#
#2-selecionar o primeiro numero maior que o digitado pelo usuário e guardar seu índice
#3-selecionar todos os numeros seguintes do indice guardado e empurrá-los a direira(-1 indice)
#4-adicionar 1 novo campo vazio ao tamanho da estrutura:lista(esse iíndice será ocupado
# pelos numeros seguintes citados na linha3)#
#5-armazenar o numero digitado pelo usuário no indice armazenado anteriormnte#

from time import sleep

usuario = int(input('Digite um numero desejado(0<x>10):'))
print('Escolhido:{}'.format(usuario))

lista_nums = list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for num in lista_nums:
    i = 0
    while i < len(lista_nums):
        if lista_nums[num] >= usuario:
            if lista_nums[num] > usuario:
                indice = num
                i = len(lista_nums) + 1
                break
            else:
                print('Numero já existente na lista!')
                i = len(lista_nums) + 1
                break
        elif usuario >= len(lista_nums):
            if usuario == len(lista_nums):
                indice = len(lista_nums)
                print('O numero:{}, encontra-se no índice:{}'.format(usuario, indice))
                i = len(lista_nums) + 1
                break
            else:
                print('Adicionando novo elemento...')
                sleep(1)
                lista_nums = lista_nums.append(usuario)
                break
        else:
            i = i + 1

print(lista_nums)
print('Fim do programa!')