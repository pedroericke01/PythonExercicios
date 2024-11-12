# script que permite cadastrar 3 pessoas em uma matriz de dados:
pessoas = []
# variavel que vai armazenar os dados de cada pessoa separadamente e após finalizar o cadastro
# de uma pessoa, será enviado uma cópia desse cadastro para a matriz e vamos limpar os dados
# da pessoa, visando manter o "formulário" de cadastro limpo para novas operações:
pessoa_cadastro = list()

for pessoa in range(0, 3):
    pessoa_cadastro.append(str(input("\nNome:")).strip().upper())
    pessoa_cadastro.append(int(input("Idade:")))
    pessoa_cadastro.append(str(input("Genero:")).strip().upper())
    # comando que envia uma cópia dos dados inseridos do usuário para a matriz#
    pessoas.append(pessoa_cadastro[:])
    # comando para limpar a lista que vai armazenar os dados inseridos pelos usuários e
    # manter essa lista limpa e preparada para novas operações:
    pessoa_cadastro.clear()
print(f"\nNova Matriz de dados:{pessoas}")
print("\nFim do Programa!\n")
