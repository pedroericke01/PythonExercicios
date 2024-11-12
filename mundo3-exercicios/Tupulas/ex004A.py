# scritp que vai escolher 5 numeros inteiros e coloca-los dentro de uma túpula, no final sera
# exibido a tupula com os numeros, qual é o maior e o menor numero escolhido:#

from random import randint

print("\n{:=^40}\n".format(" SORTEANDO NUMEROS "))

numeros_sorteado = (randint(1, 10), randint(1, 10),
                    randint(1, 10), randint(1, 10))
