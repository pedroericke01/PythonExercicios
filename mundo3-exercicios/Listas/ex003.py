# script que lê 5 numeros inteiros e coloca-os em uma lista, no final mostra qual numero foi
# o maior e o menor e suas respectivas posições/indices na lista.#

# inicializando lista vazia:
lista_nums = list()
# analisando informações importantes da lista, como: estado e tamanho da lista:
print(f"Lista Original:{lista_nums}")
print(f"Tam,Lista Original:{len(lista_nums)}")
# declarando variáveis Globais que serão utilizadas por todo meu sistema:
maior = menor = posmaior = posmenor = 0
# nessa estrutura do FOR, podemos trabalhar tanto com índices quanto com o elemento correspondente
# ao índice tratado no loop. Dessa forma, conseguimos inserir numeros no FINAL da lista e
# garantir que os Maior e o Menor seja Declarado corretamente:
for num in range(0, 5):
    lista_nums.append(int(input("\nEscolha um numero:")))
    print(f"Tam.Lista:{len(lista_nums)}")
    if num == 0:
        maior = lista_nums[num]
        posmaior = num
        menor = lista_nums[num]
        posmenor = num
    else:
        if lista_nums[num] >= maior:
            maior = lista_nums[num]
            posmaior = num
        elif lista_nums[num] <= menor:
            menor = lista_nums[num]
            posmenor = num

print(f"\nLista Nova:{lista_nums}")
print(f"Tam.Lista Nova:{len(lista_nums)}")

print('''\nO Menor Numero da lista é {} que está na posição {}
O maior Numero da lista é {} que está na posição {} da lista!'''.format(menor, posmenor,
                                                                        maior, posmaior))
print("\nFim do Programa!")
