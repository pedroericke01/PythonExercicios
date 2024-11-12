# programa que cria uma matriz 3x3 que será preenchida pelos valores inseridos pelo usuario
# e no final, precisamos imprimir a matriz e suas respectivas dimensões e dados:#
matriz_nums = []
print(f"Matriz Original:{matriz_nums}")
print(f"Tam.Matriz:{len(matriz_nums)}\n")

lista_aux = list()
# lembre-se 3x3 == 9, exatamente o total de elementos dentro de uma matriz 3x3: #
for colunas in range(0, 3):
    for linhas in range(0, 3):
        lista_aux.append(int(input(f"Escolha um numero para a posição [{len(matriz_nums)}][{linhas}]")))
        if linhas == 2:
            matriz_nums.append(lista_aux[:])
            lista_aux.clear()
            break

print(f"\nMatriz Atualizada:{matriz_nums}")
print("{:=^30}".format(" DIMENSÃO 3X3: "))
for elem in matriz_nums:
    print(elem)
