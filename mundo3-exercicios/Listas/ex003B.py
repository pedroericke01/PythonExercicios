# script que lê 5 numeros inteiros e coloca-os em uma lista, no final mostra qual numero foi
# o maior e o menor e suas respectivas posições/indices na lista.
# tambem permite no caso de numeros repetidos identificas as respectivas posições dos valores
# maior e menor que se repetiram na lista:#

lista_nums = list()
print(f"Lista Original:{lista_nums}")
print(f"Tam.Lista Original:{len(lista_nums)}\n")

maior = pos_maior = menor = pos_menor = 0

for num in range(0, 5):
    lista_nums.append(int(input(f"Escolha um numero para colocar na posição {num} da lista:")))

    if num == 0:
        maior = menor = lista_nums[num]
        pos_maior = pos_menor = num
    else:
        if lista_nums[num] >= maior:
            maior = lista_nums[num]
            pos_maior = num
        elif lista_nums[num] <= menor:
            menor = lista_nums[num]
            pos_menor = num

    print("Numero Cadastrado!")
    print(f"Tam.Lista Atualizado:{len(lista_nums)}\n")

print(f"Lista Nova:{lista_nums}")
print(f"Tam.Lista Nova:{len(lista_nums)}")

# loop que vai percorrer a lista ja criada e verificar possiveis repetições
# dos valores maior, a organização do Enumarate:
# for indice, elemento in enumarate(lista_tratada):
print(f"O maior numero inserido foi {maior} está nas posições ", end="")
for pos, elem in enumerate(lista_nums):
    if elem == maior:
        print(f"{pos}...", end="")

# loop que percorre toda a lista e verifica possiveis repetições dos valores Menor:
print(f"\nO menor numero inserido foi {menor} está nas posições ", end="")
for pos, elem in enumerate(lista_nums):
    if elem == menor:
        print(f"{pos}...", end="")

print("\nFim do Programa!")
