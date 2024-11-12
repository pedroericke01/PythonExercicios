# min() -> Método que Analisa o menor valor inteiro em uma túpula
# max() -> Metodo que Analisa o Maior valor inteiro em uma Túpula

from random import randint

print("\n{:+^40}\n".format(" SORTEANDO NUMEROS "))

numeros = (randint(1,10), randint(1,10),
           randint(1,10), randint(1,10))

for numero in numeros:
    print(numero, end=" ")
print(f"\nO maior numero foi: {max(numeros)}")
print(f"O menor numero foi: {min(numeros)}")
print("\nFim do Programa!")
