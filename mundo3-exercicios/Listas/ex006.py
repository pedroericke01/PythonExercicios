# script que lê varios numeros e colocar em uma lista, no final mostre:
# 1- a quant de numeros que foram inseridos;
# 2- a lisa ordenada na ordem decrescente;
# 3- se o numero 5 foi inserido, e sua respectiva posição na lista;#
from typing import List

lista_nums = list()
print(f"Lista Original:{lista_nums}")
print(f"Tam.Lista Original:{len(lista_nums)}\n")

resposta_usuario = 0
while True:
    numero = int(input("Escolha um numero:"))
    while numero in lista_nums:
        print("Esse numero Ja existe na Lista!")
        numero = int(input("Escolha Outro numero:"))
    lista_nums.append(numero)
    print("Numero Cadastrado!")
    print(f"Lista Nova:{lista_nums}")
    resposta_usuario = str(input("\nDeseja Continuar[S/N]?")).upper().strip()
    while resposta_usuario not in "SIMNAO":
        resposta_usuario = str(input("\nDeseja Continuar[S/N]?")).upper().strip()
    if resposta_usuario == "NAO":
        break

print(f"\nForam inseridos ao todo {len(lista_nums)} numeros!")
# Aplicando o método de Ordem Decrescente na Lista criada acima:
lista_nums.sort(reverse=True)
print(f"Lista Ordenada em Ordem Decrescente {lista_nums}")

# loop que percorre a lista e busca o numero 5 e seu respectivo índice:
for elem in range(0, len(lista_nums)):
    if lista_nums[elem] == 5:
        print(f"O numero {lista_nums[elem]} está no índice {elem} da lista,"
              f" considerando a ordem reversa!")
print("\nFim")
