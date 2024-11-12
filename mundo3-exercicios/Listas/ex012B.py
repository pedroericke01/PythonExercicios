# programa que cria uma matriz 3x3 que será preenchida pelos valores inseridos pelo usuario
# e no final, precisamos imprimir a matriz e suas respectivas dimensões e dados:#

# inicializando a matriz principal do sistema:
matriz_dados = []
print(f"Matriz Original:{matriz_dados}")
print(f"Tam.Matriz Original:{len(matriz_dados)}\n")

# lista auxiliar que vai armazenar as informações inseridas pelo usuario:
lista_dados = list()

# loop que vai permitir cadastrar 3 usuario e suas respectivas informações no sistema:
for cadastro in range(0, 3):
    nome = str(input("\nNome:")).strip().upper()
    # loop interno que percorre a matriz principal e verifica se em cada lista interna
    # da matriz, o nome de cada elemento, está se repetindo com o input do usuario, pois
    # NÃO PODE TER NOMES IGUAIS NESSE SISTEMA:#
    for elem in range(0, len(matriz_dados)):
        while matriz_dados[elem][0] == nome:
            print("Esse nome de usuario ja existe!\n")
            nome = str(input("Escolha OUTRO Nome:")).strip().upper()
    # após analisarmos que o nome inserido pelo usuário não existe na matriz, isso é, será um
    # nome NOVO, então poderemos inseri-lo na lista auxiliar do sistema, que vai armazenar os
    # dados digitados pelo usuário:
    lista_dados.append(nome)

    idade = int(input("Idade:"))
    lista_dados.append(idade)
    # temos por base os generos masculino e feminino:
    genero = str(input("Genero[M/F]:")).strip().upper()
    # loop que garante que o usuario insira os generos masculino ou feminino, caso contrário,
    # o sistema vai força-lo a inserir o genero correto:
    while genero not in "MASCULINOFEMININO":
        print("Genero inválido!\n")
        genero = str(input("Genero[M/F]:")).strip().upper()
    # após validarmos o genero, seja masculino ou feminino, poderemos dar continuidade a execução
    # do sistema, isso é adicionar esses dados a lista auxiliar:
    lista_dados.append(genero)

    # criando uma cópia do registro dessas informações acima e adicionando-o a matriz:
    matriz_dados.append(lista_dados[:])

    # após enviar a cópia dos dados de cadastro acima do respectivo usuario, vamos limpar
    # esse cadastro, visando a economia de memória e garantir a segurança dos dados:
    lista_dados.clear()

# loop que vai percorrer a matriz dos dados e imprimir suas dimensões e respectivas informações:
print("="*35)
for dimensoes in matriz_dados:
    print(f"{dimensoes}")
print("="*35)
print("\nFim\n")
