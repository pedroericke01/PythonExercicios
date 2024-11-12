# scritp que vai escolher 5 numeros inteiros e coloca-los dentro de uma túpula, no final sera
# exibido a tupula com os numeros, qual é o maior e o menor numero escolhido:#

from random import randint

print("\n{:+^40}\n".format(" SORTEANDO NUMEROS "))

escolha_maquina = maior = menor = tupula_numeros = 0

for cont in range(0, 5):
    escolha_maquina = randint(1, 10)
    print(escolha_maquina, end=" ")
    # verificando maiores e menores numeros com auxilio da variável cont:
    if cont == 1:
        maior = escolha_maquina
        menor = escolha_maquina
    else:
        if escolha_maquina >= maior:
            maior = escolha_maquina
        elif escolha_maquina <= menor:
            menor = escolha_maquina
tupula_numeros = (maior, menor)
print(f"\nMinha Tupula:{tupula_numeros}")

print(f"O maior numero é {maior} e o menor numero é {menor}")

print("\nFim!")

