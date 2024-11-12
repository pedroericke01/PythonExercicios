# programa que ajuda um jogador de mega cena a criar palpites, o programa vai perguntar
# ao usuario quantos jogos serão gerados e vai sortear 6 numeros entre 1 a 60, para cada
# jogo, cadastrando tudo em uma lista composta no final e não poderá haver numeros repetidos
# nessas listas:

# importando a biblioteca random e time:
from random import randint
from time import sleep

# inicializando a matriz principal do sistema:
matriz_sorteios = []
print(f"Matriz Principal:{matriz_sorteios}")
print(f"Tam.Matriz Principal:{len(matriz_sorteios)}\n")

# criando lista auxiliar:
lista_aux = list()

# variável que vai armazenar a quantidade de soteios que o usuairo deseja fazer:
quant_sorteios = int(input("Quantos Jogos serão gerados?"))

# loop que permitirá o sorteio de 6 numeros aleatórios e não repetidos e no final,
# inserir esses numeros em uma lista auxiliar:
for quant_jogos in range(0, quant_sorteios):

    for sorteios in range(0, 6):
        # criamos a variável sorteio que permitirá o sorteio de
        # um numero entre 1 a 60 de modo aleatório:
        sorteio = randint(1, 60)
        # loop de segurança que garante que não haverão numeros repetdos dentro da lista
        # de sorteios:
        while sorteio in lista_aux:
            sorteio = randint(1, 60)
        lista_aux.append(sorteio)

    # após finalizar o sorteio dos 6 valores e colocálos em uma lista respectiva, então
    # podemos enviar uma cópia dessa lista para a matriz principal do sistema:
    matriz_sorteios.append(lista_aux[:])
    # após enviarmos a cópia da lista com os 6 numeros serteados, então, poderemos limpar
    # a lista com os numeros, permitindo a inserção de novos numeros na lista auxiliar:
    lista_aux.clear()
# loop que vai percorrer a matriz principal do sistema imprimir cada lista com os 6 numeros
# sorteados:
print("\n{:=^35}\n".format(" SORTEANDO VALORES "))
for jogo in range(0, len(matriz_sorteios)):
    print(f"Jogo {jogo}:{matriz_sorteios[jogo]}")
    sleep(1)
print("="*35)
print("\nfim")
