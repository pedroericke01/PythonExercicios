# script que com apenas uma TUPULA estruturando seus dados: ("produto":Valor), vamos
# no final imprimir todos esses dados de maneira Tabular e organizada#

produtos = ("Lapis", 1.75,
            "Borracha", 2.00,
            "Caderno", 15.90,
            "Estojo", 25.00,
            "Transferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 120.32,
            "Canetas", 22.30,
            "Livros", 34.90
            )
print("="*40)
print(f"{'TABELA DE PREÇOS':^30}")
print("="*40)
# considerando a contagem dos elementos internos dessa Tupula, iniciando de 0 até N
# e a estruturação dos dados: ("chave":Valor), então todos os Produtos(chaves) serão representados por
# indices PAR, ja os Preços(valor) do respectivo produto serão Representados por indices IMPAR#
for indice in range(0, len(produtos)):
    # verificando se o indice é PAR, caso seja, vamos formatar a impressao desse produto ("chave")
    if indice % 2 == 0:
        print(f"{produtos[indice]:<30}", end="")
   # no caso do indice ser IMPAR, vamos formatar sua impressão desse produto (valor)
   # definindo que cada valor deverá ter 2 casas decimais
    else:
        print(f"R${produtos[indice]:>8.2f}")
print("="*40)
print("\nFim do Programa!\n")
