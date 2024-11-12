''' crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
organizando os dados em forma tabular'''

#observe a etrutura dos dados  é: ("chave":valor), e considerando a contegem dos elementos
# internos da estrutura, iniciando de 0 á N, então os elementos "chaves" são representados
# por índices PAR ja os elementos valor por indices IMPAR
# dessa maneira, devemos percorrer os índices dos elementos dessa estrutura#

tupula_produtos = ("Lapis", 1.75,
                   "borracha", 2.00,
                   "Caderno", 15.90,
                   "Estojo", 25.00,
                   "Transferidor", 4.20,
                   "Compasso", 9.99,
                   "Mochila", 120.32,
                   "Canetas", 22.30,
                   "Livros", 34.90
                   )
print("-"*40)
#python 3:
#print("{:^30}".format("LISTAGEM DE PREÇOS"))

#python3.6+:
print(f"{'LISTAGEM DE PREÇOS':^30}")
print("-"*40)
for pos in range(0, len(tupula_produtos)):
    #caso o índice do elemento dentro da tupula seja PAR, então vamos imprimir sua formatação
    # Á Esquerda com 30 pontos á direita, sem quebra de linha para que os preços do produto
    # possa ser colocado corretamente ao seu lado#
    if pos % 2 == 0:
        print(f"{tupula_produtos[pos]:.<30}", end="")
    # ja no caso de o índice do elemento ser IMPAr então vamos formatar sua impressão á Esquerda
    # com 8 espaçamentos vazos e os valores serão com 2 casas decimais
    else:
        print(f"R${tupula_produtos[pos]:>8.2f}")
print("-"*40)
print("\nFim do Programa!\n")
