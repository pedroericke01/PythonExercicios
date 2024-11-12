# script que lê o nome e o peso de varias pessoas e coloca esses dados no final de uma
# lista, no final mostre:
# 1- quantas pessoas foram caastradas
# 2- uma lista com as pessoas mais pesadas
# 3- uma lista com pessoas mais leves#

# inicializando a matriz principal do programa, a princípio vazia:
matriz_pessoas = []
print(f"matriz Original:{matriz_pessoas}")
print(f"Tam.Matriz Original:{len(matriz_pessoas)}")

# inicializando lista AUXILIAR que vai armazenar os dados de cada usuario separadamente
# e colocá-los na matriz:
cadastro_pessoa = list()

resposta_usuario = 0
while True:
    cadastro_pessoa.append(str(input("\nNome:")).strip())
    cadastro_pessoa.append(float(input("Peso[kg]:")))
    # criando uma cópia dos dados inserido pelo usuario e colocando-os na matriz
    # principal do programa:
    matriz_pessoas.append(cadastro_pessoa[:])
    # limpando os dados inseridos pelo usuário após ja envia-los para a matriz
    # principal do programa:
    cadastro_pessoa.clear()

    resposta_usuario = str(input("Deseja Continuar[SIM/NAO]?")).strip().upper()
    while resposta_usuario not in "SIMNAO":
        resposta_usuario = str(input("\nDigite a Resposta CORRETA[sim/nao]:")).strip().upper()
    if resposta_usuario == "NAO":
        break
print(f"\nNova Matriz:{matriz_pessoas}")
print(f"Foram cadastrados ao todo {len(matriz_pessoas)} pessoas no sistema!")

pesado = leve = 0
# loop que vai percorrer a matriz e analisar os usuarios pelo peso mais leve e mais pesado:
for pessoa in matriz_pessoas:
    # verificando se é a primeira iteraçaõ, caso seja, então, vamos iniciar a busca pelo peso
    # mais pesado e mais leve:
    if pessoa == matriz_pessoas[0]:
        pesado = pessoa[1]
        leve = pessoa[1]
    else:
        if pessoa[1] >= pesado:
            pesado = pessoa[1]
        elif pessoa[1] <= leve:
            leve = pessoa[1]
# após definir os valores de mais pesado e leve, será possível pesquisar por repetições de
# pesos entre usuarios no sistema, e no final imprimir seus respectivos nomes:
print(f"O maior peso:{pesado}kg foi de ", end="")
for peso in matriz_pessoas:
    if peso[1] == pesado:
        print(f"{peso[0]},", end=" ")

print(f"\nO menor peso:{leve}kg foi de ", end="")
for peso in matriz_pessoas:
    if peso[1] == leve:
        print(f"{peso[0]},", end=" ")

print("\nFim do Programa!\n")
