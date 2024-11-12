# script que permite que o usuario 5 numeros no final da lista e no final vamos informar a
# posição que o respectivo numero foi colocado na lista:#

# inicializando uma lista vazia:
numeros = list()
print(f"Lista Original:{numeros}")
print(f"Tam.Lista Original:{len(numeros)}")
# loop que insere 5 numeros no final da lista e informa o tamanho atualizado da lista:
for num in range(0, 5):
    numeros.append(int(input("Escolha um numero:")))
    print(f"Tam.Lista:{len(numeros)}")
# imprimindo a lista nova com os novos numeros inseridos pelo usuario na lista e informando
# o tamanho da nova lista atualizada:
print(f"\nNova Lista:{numeros}")
print(f"Tam.Nova Lista:{len(numeros)}\n")
# informando o elemento e o respectivo índice na lista:
for elem in range(0, len(numeros)):
    print(f"O numero {numeros[elem]} foi colocado no índice {elem} da lista")
print("\nFim do Programa!")
