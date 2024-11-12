from random import randint

print("\n{:+^40}\n".format(" SORTEANDO NUMEROS "))

escolha_maquina = (randint(1, 10), randint(1, 10),
                   randint(1, 10), randint(1, 10))
print(f"Os Valores Sorteados Foram:{escolha_maquina}")

maior = menor = 0
for cont, numero in enumerate(escolha_maquina):
    if cont == 1:
        maior = numero
        menor = numero
    else:
        if numero >= maior:
            maior = numero
        elif numero <= menor:
            menor = numero
print(f"O maior numero foi {maior} e o menor numero foi {menor}")
print("\nFim")
