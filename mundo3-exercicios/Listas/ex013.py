# programa que cria uma matriz 3x3 que será preenchida pelos valores inseridos pelo usuario
# e no final, precisamos imprimir a matriz e suas respectivas dimensões e dados:
# no final:
# 1- a soma dos valores pares;
# 2- a soma dos valores da 3 coluna;
# 3- o maior valor da 2 coluna;#

matriz_nums = []
print(f"Matriz Principal:{matriz_nums}")
print(f"Tam.Matriz Principal:{len(matriz_nums)}\n")

lista_aux = list()
soma_par = soma = maior = 0

for colunas in range(0, 3):
    if colunas == 0:
        for linhas in range(0, 3):
            numero = int(input(f"Escolha um numero para a posição [{colunas}][{linhas}]:"))

            lista_aux.append(numero)

            matriz_nums.append(lista_aux[:])

            lista_aux.clear()

            if numero % 2 == 0:
                soma_par += numero

    if colunas == 1:

        for linhas in range(0, 3):
            numero = int(input(f"Escolha um numero para a posição [{colunas}][{linhas}]:"))

            lista_aux.append(numero)

            matriz_nums.append(lista_aux[:])

            lista_aux.clear()

            if numero % 2 == 0:
                soma_par += numero

            if linhas == 0:
                maior = numero
            else:
                if numero >= maior:
                    maior = numero

    if colunas == 2:

        for linhas in range(0, 3):
            numero = int(input(f"Escolha um numero para a posição [{colunas}][{linhas}]:"))

            lista_aux.append(numero)

            matriz_nums.append(lista_aux[:])

            lista_aux.clear()

            if numero % 2 == 0:
                soma_par += numero

            soma += numero

print(f"\nMatriz Atualizada:{matriz_nums}")

print("{:=^30}".format("DIMENSÃO 3X3:"))

for elem in range(0, len(matriz_nums)):
    if elem in range(0, len(matriz_nums), 3):
        print(f"\n{matriz_nums[elem]}", end=" ")
    else:
        print(f"{matriz_nums[elem]}", end=" ")

print(f"\nA soma dos PARES será:{soma_par}")
print(f"O maior numero da 2 Coluna será:{maior}")
print(f"A soma dos numeros da 3 Coluna será:{soma}")
