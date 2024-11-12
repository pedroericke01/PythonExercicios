# script que permite que o usuario insira 5 valores numericos e insira-os em uma lista.
# caso esse numero ja exista, ele não será adicionado na lista, ou seja, não haverá numeros
# repetidos nessa lista e no final será impresso toda a lista numerica em ordem Crescente#

# inicializando lista vazia:
lista_nums = list()
# verificando informações importantes sobre a lista, como tamanho e elementos existentes:
print(f"Lista Original:{lista_nums}")
print(f"Tam.Lista Original:{len(lista_nums)}")
# loop que permite o usuario inserir 5 numeros inteiros no final da lista e tambem trabalha
# com os índices e com os proprios elementos dos índices respectivos na lista:
for num in range(0, 5):
    numero = int(input(f"\nEscolha um numero para colocar na posição {num}:"))
# com o loop WHILE garante que o usuario insira apenas numeros novos na lista e não
# numeros repetidos, caso o usuario tente inserir numeros repetidos o sistema vai força-lo
# a inserir numeros novos.
    while numero in lista_nums:
        print("Numero Ja Existe na Lista!")
        numero = int(input(f"\nEscolha outro numero para colocar na posição {num}:"))
# quando o usuario inserir numeros novos na lista, então esses serão cadastrados na lista e
# será impresso o tamanho atualizado da minha lista para que o usuario acompanhe seu crescimento#
    lista_nums.append(numero)
    print("Numero Cadastado!")
    print(f"Tam.Lista Nova {len(lista_nums)}")
# no final do loop, vamos imprimir toda a lista nova com os 5 novos inteiros inserido pelo usuario
# e o respectivo tamanho da lista atualizado:
print(f"\nLista Nova:{lista_nums}")
print(f"Tam.Lista Nova:{len(lista_nums)}")
# agora, vamos ordenar a lista em ordem crescente, primeiro, chamamos a função sort() e depois
# imprimimos a própria lista desejada:
lista_nums.sort()
print(f"Lista Nova Ordenada Crescente:{lista_nums}")
# informando o fim do programa ao usuario:
print("\nFim do Programa!")
