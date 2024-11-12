# script que permite que o usuario insina 5 numeros no final da minha lista através do loop FOR
# e no final será impressa a nova lista e o tamanho dessa lista, podendo o usuario escolher
# ver a lista em ordem crescente ou decrescente:

lista_nums = list()
print(f"Lista Original:{lista_nums}")
print(f"Tam.Lista Original:{len(lista_nums)}")

for num in range(0, 5):
    lista_nums.append(int(input("\nEscolha um numero:")))
    print(f"Tam.Lista:{len(lista_nums)}")

print(f"\nNova Lista:{lista_nums}")
print(f"Tam.Nova Lista:{len(lista_nums)}")

escolha_usuario = str(input("Você deseja ver sua Lista na ordem Crescente ou Decrescente?")).strip().upper()
if escolha_usuario == "CRESCENTE":
    lista_nums.sort()
    print(f"Lista Ordem Crescente:{lista_nums}")
elif escolha_usuario == "DECRESCENTE":
    lista_nums.sort(reverse=True)
    print(f"Lista Ordem Decrescente:{lista_nums}")
print("\nFim do Programa!")
