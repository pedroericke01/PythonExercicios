# programa que cria uma matriz 3x3 que será preenchida pelos valores inseridos pelo usuario
# e no final, precisamos imprimir a matriz e suas respectivas dimensões e dados:#

# inicializando a matriz principal:
matriz_nums = []

lista_aux = list()

for pos in range(0, 9, 1):
    lista_aux.append(int(input(f"Escolha um numero para coloca-lo na posição [{pos}]:")))
    print("Numero Cadastrado!")
    if len(lista_aux) == 3:
        matriz_nums.append(lista_aux[:])
        lista_aux.clear()
print(f"\nMatriz:{matriz_nums}")

