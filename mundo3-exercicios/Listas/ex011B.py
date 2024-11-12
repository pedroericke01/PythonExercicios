# programa que permite ao usuario digitar 7 numeros inteiros e inseri-los em uma lista única
# que manterá os valores pares e impares separados e no final, devemos imprimir os valores
# pares e impares na ordem crescente:#

# inicializando a matriz do programa:
matriz_nums = []
print(f"Matriz Original:{matriz_nums}")
print(f"Tam.Matriz::{len(matriz_nums)}\n")

# lista auxiliar que vai receber os inputs do usuario e armazena-los:
lista_aux = list()

# loop que permite o usuario inserir 7 numeros inteiros:
for elem in range(0, 7):
    numero = int(input("Escolha um numero[1/10]:"))
    while numero == 0 or numero in lista_aux:
        print("Esse numero ja existe!\n")
        numero = int(input("Escolha um numero[1/10]:"))
    lista_aux.append(numero)

# variáveis que serão usadas para armazenar os valores pares e impares separadamente
# e respectivamente:
lista_par = list()
lista_impar = list()

# loop que vai percorrer a lista auxiliar acima e separas os inteiros pares dos impares:
for nums in range(0, len(lista_aux)):
    if lista_aux[nums] % 2 == 0:
        lista_par.append(lista_aux[nums])
    else:
        lista_impar.append(lista_aux[nums])
# após separar os inteiros pares e impares em listas difernetes, podemos limpar a lista
# que recebe os inputs do usuario, visando economia de memória e segurança nos registros:
lista_aux.clear()

# seguindo as especificações do sistema, devemos imprimir os valores pares e impares
# ordenados na ordem crescente:
lista_par.sort()
lista_impar.sort()

# 1- enviando a cópia da lista_par para a matriz do sistema:
matriz_nums.append(lista_par[:])

# limpando a lista com inteiros pares, visando a economia de memória
# e segurança nos registros:
lista_par.clear()

# 2- enviando a cópia da lista_impar para a matriz do sistema:
matriz_nums.append(lista_impar[:])

# limpando a lista com inteiros pares, visando a economia de memória
# e segurança nos registros:
lista_impar.clear()

print(f"\nMatriz Atualizada:{matriz_nums}\n")
print("Fim\n")
