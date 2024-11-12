# script que permite cadastrar 4 pessoas em uma Matriz:

# inicializando a matriz:
matriz_pessoas = []
# variável que vai armazanar os dados de cada usuario, como nome, idade e genero, para no final
# inserir esses dados na matriz principal do sistema:
cadastro_pessoa = list()
quant_maior = quant_menor = 0
for cadastro in range(0, 4):
    # inserindo as informações de cadastro de cada usuário separadamente ao final da lista
    # "cadastro_pessoa":
    cadastro_pessoa.append(str(input("\nNome:")).strip().upper())
    cadastro_pessoa.append(int(input("Idade:")))
    cadastro_pessoa.append(str(input("Genero:")).strip().upper())
    # criando uma cópia dessas informações de cadastro acima e enviando-as para a matriz
    # principal do sistema:
    matriz_pessoas.append(cadastro_pessoa[:])
    # comando que limpa toda a lista que armazena o cadastro de cada pessoa no sistema, para dar
    # inicio ao novo cadastro de usuario seguindo o intervalo de vezes definido no loop:
    cadastro_pessoa.clear()
print(f"\nMatriz:{matriz_pessoas}\n")
# loop que percorre a matriz que contêm os dados de cada pessoa inserida e vai imprimir os
# dados das pessoas com idade >= 18 anos:#
for pessoa in matriz_pessoas:
    # pessoa[1] corresponde a idade de cada pessoa separadamente, pessoa[0] corresponde ao nome
    # de cada pessoa e pessoa[2] corresponde ao genero de cada pessoa
    if pessoa[1] >= 18:
        print(f"{pessoa[0]} é maior de idade!")
        quant_maior += 1
    else:
        print(f"{pessoa[0]} é menor de idade!")
        quant_menor += 1
print(f'''\nTemos ao todo {quant_maior} pessoas maiores de idade 
e {quant_menor} menores de idade!''')
print("\nFim")
