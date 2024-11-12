# programa que cria uma matriz 3x3 que será preenchida pelos valores inseridos pelo usuario
# e no final, precisamos imprimir a matriz e suas respectivas dimensões e dados:#

# inicializando matriz do programa:
matriz_dados = []
print(f"Matriz Original:{matriz_dados}")
print(f"Tam.Matriz Original:{len(matriz_dados)}\n")

# lista que receberá os inputs do usuario:
lista_dados = list()

# loop que permite cadastrar 3 usuarios dentro da matriz, com suas informações como:
# nome, idade e genero:
for cadastro in range(0, 3):
    lista_dados.append(str(input("\nNome:")).strip().upper())
    lista_dados.append(int(input("Idade:")))
    lista_dados.append(str(input("Genero:")).strip().upper())

    # criando uma cópia dessas informações acima, e enviando para a matriz principal:
    matriz_dados.append(lista_dados[:])
    # após enviar a cópia das informações do usuario para a matriz, devemos limpar esses dados,
    # garantindo economia de memória e segurança das informações:
    lista_dados.clear()

# loop que vai percorrer toda a matriz principal do sistema e imprimir seus dados,
# na dimensão 3x3:
for dimensao in matriz_dados:
    print(f"\n{dimensao}")
print("\nFim\n")
