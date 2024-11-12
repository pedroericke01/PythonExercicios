# script que permite ao usuario inserir varios numeros inteiros e cadastrá-los em uma lista.
# em sua posição/indice correto de inserção, sem usar o método Sort() para esse fim.
# não poderá haver numeros repetidos e no final, deverá mostrar a lista ordenada
# na tela sem o uso do método Sort() ou Sorted()
# vamos usar nesse caso o loop WHILE para percorrer toda a lista e verificar a posição correta
# para posicionar o novo elemento#

# inicializando a lista vazia:
lista_nums = list()
print(f"Lista Original:{lista_nums}")
print(f"Tam.Lista Original:{len(lista_nums)}\n")

# loop que permite o usuario inserir 5 numeros inteiros na lista:
for elem in range(0, 5):
    numero = int(input("Escolha um numero:"))
    # loop que garante que não haverá valores repetidos dentro da lista, caso o usuario
    # digite um valor que ja exista na lista(repetido), então o sistema vai força-lo
    # a inserir outro numero:
    while numero in lista_nums:
        print("Esse numero ja EXISTE na lista!\n")
        numero = int(input("Escolha OUTRO numero:"))
    # trabalhando com a iteração, garantindo que o primeiro numero inserido pelo usuario,
    # sabendo que a lista a principio é inicializada vazia, então esse primeiro numero será
    # inserido no final da lista na primeira iteração.
    if elem == 0:
        lista_nums.append(numero)
        print("Adicionado ao FINAL da lista!")
        print(f"Tam.Lista Atualizado:{len(lista_nums)}\n")
    # no caso de ser a segunda ou a ultima iteração do loop, então deverá ser analisada a
    # posição correta para inserir o meu elemento desejado:
    else:
        pos = 0
        while pos <= len(lista_nums):
            if lista_nums[pos] > numero:
                lista_nums.insert(pos, numero)
                print(f"Adicionado na posição {pos} da lista!\n")
                break
            if lista_nums[-1] < numero:
                lista_nums.append(numero)
                print("Adicionado no FINAL da lista!\n")
                break
            pos += 1
    print(f"Lista Nova:{lista_nums}")
    print(f"Tam.Lista Atualizado:{len(lista_nums)}\n")
print("Fim do Programa!\n")
