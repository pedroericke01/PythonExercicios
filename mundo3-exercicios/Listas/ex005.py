# script que permite ao usuario inserir 5 numeros inteiros e cadastrá-los em uma lista.
# em sua posição/indice correto de inserção, sem usar o método Sort() para esse fim.
# no final, deverá mostrar a lista ordenada na tela sem o uso do método Sort() ou Sorted()#

# iniciando lista vazia:
lista_nums = list()
# analisando as informações importantes da minha lista:
print(f"Lista Original:{lista_nums}")
print(f"Tam.Lista:{len(lista_nums)}")

# loop que permite inserir novos 5 numeros na lista:
for num in range(0, 5):
    numero = int(input(f"Escolha um numero para colocar na posição {num}:"))
    # loop que verifica se o numero escolhido acima ja existe ou não na minha lista tratada,
    # caso ja exista, o loop vai forçar o usuario a inserir um novo numero na lista:
    while numero in lista_nums:
        print("Esse numero ja existe na Lista!")
        numero = int(input(f"Escolha Outro numero para colocar na posição {num}:"))
    # caso seja a primeira iteração do loop, então, esse novo numero será colocado no final
    # da lista pois á princípio a lista está vazia:
    if num == 0:
        lista_nums.append(numero)
    # agora, a lista ja terá +1 elemento, então será possível realizar as analises de posicionamento
    # abaixo:
    else:
        # loop que trabalha tanto com os índices quanto com o proprio elemento na lista,
        # esse lopp
        for elem in range(0, len(lista_nums)):
            # usa como padrõa de analisa a busca pelo primeiro elemento que seje maior que o escolhido
            # pelo usuario, quando o encontra, então vai posicionar o numero escolhido na posição
            # anterior ao primeiro maior (encontrado)
            # e empurra o elemento maior mais á direita:
            if lista_nums[elem] > numero:
                lista_nums.insert(elem, numero)
                break
            # caso o numero escolhido seja maior que o ultimo numero existente na lista, então o
            # numero escolhido pelo usuario será posicionado no final da lista:
            elif numero > lista_nums[-1]:
                lista_nums.append(numero)
                break
print(f"Nova Lista:{lista_nums}")
print(f"Tam.NovaLista:{len(lista_nums)}")
