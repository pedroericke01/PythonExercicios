# script que permite que o usuario insira 5 valores no final da lista com o loop FOR e no
# final imprime a Nova Lista, com os novos 5 valores em ordem crescente:#

# inicializando minha lista VAZIA
lista_nums = list()
print(f"Lista Original:{lista_nums}")
print(f"Tamanho Lista Original:{len(lista_nums)}")

for num in range(0, 5, 1):
    lista_nums.append(int(input("\nEscolha um numero:")))
    print(f"Tam.Lista:{len(lista_nums)}")
# Imprimindo a nova lista com os novos numeros escolhidos pelo usuario e
# informando o tamanho dessa nova lista:
print(f"\nNova Lista:{lista_nums}")
print(f"Tam.Nova Lista:{len(lista_nums)}")
# ordenando a nova lista em ordem crescente:
lista_nums.sort()
print(f"\nNova Lista Ordenada Crescente:{lista_nums}")

print("\nFim do Programa!")
