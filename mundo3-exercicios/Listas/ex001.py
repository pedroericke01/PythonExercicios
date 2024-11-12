# inserindo valores no final de uma lista através da interação com o usuario
# e no final essa lista será impressa seguindo a sequência de numeros escolhidos pelo
# usuario:

# inicializando uma lista Vazia:#
lista_nums = list()
# loop que permite que vai se repetir 4 vezes pedindo que o usuario insira um numero inteiro
# no final da lista:
for num in range(0, 5, 1):
    lista_nums.append(int(input("Escolha um numero:")))
    # analisando o tamanho da lista:
    print(f"Tamanho da Lista {len(lista_nums)}\n")

# apos o loop acima terminar vamos imprimir a nova lista com os novos elementos escolhidos:
print(f"\nNova Lista:{lista_nums}")
print(f"Novo Tamanho da lista:{len(lista_nums)}")
print("\nFim")
