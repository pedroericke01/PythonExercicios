# programa que cria uma matriz 3x3 que será preenchida pelos valores inseridos pelo usuario
# e no final, precisamos imprimir a matriz e suas respectivas dimensões e dados:#

matriz_dados = []
print(f"Matriz Original:{matriz_dados}")
print(f"Tam.Matriz Original:{len(matriz_dados)}\n")

# lista auxiliar que vai armazenar os dados inseridos pelo usuario:
lista_dados = list()
# loop que vai permitir o usuario inserir 9 numeros inteiros:
for num in range(0, 9, 1):
    lista_dados.append(int(input(f"Escolha um numero para colocar a posição {num}:")))
    # criando uma cópia do numero inserido pelo usuario, após esse ja ter sido inserido
    # no final da lista auxiliar, e enviando essa cópia para a matriz principal:
    matriz_dados.append(lista_dados[:])
    # após a cópia ter sido enviada, podemos limpar a lista auxiliar, garantia economia de
    # memória e segurança dos registros:
    lista_dados.clear()
print(f"\nMatriz Atualizada:{matriz_dados}")
print(f"Tam.Matriz:{len(matriz_dados)}\n")
# loop que vai percorrer a matriz principal do sistema,
# suas dimensões(3x3) e dados respectivamente:
print("Matriz na dimensão 3x3:", end=" ")
for dimensao in range(0, len(matriz_dados)):
    if dimensao in range(0, len(matriz_dados), 3):
        print(f"\n{matriz_dados[dimensao]}", end=" ")
    else:
        print(f"{matriz_dados[dimensao]}", end=" ")
print("\nFim do Programa!")
