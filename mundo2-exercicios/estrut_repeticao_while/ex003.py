# script que informa a quantidade de numeros Pares e impares digitadas pelo usuário
# o laço de repetição vai funcionar enquanto o input do usuário for diferente de zero#

# zero é considerado um numero PAR, então no sistema, a analise da quantidade de PARES e
# IMPARES serão analisadas apenas se o numero inserido pelo usuário for diferente de zero
# tambem.#

numero = 1
# atribuição dupla de valores a variáveis, nesse caso serão acumulativas na estrutura de repe
# ticao abaixo:
quant_par = quant_impar = 0
while numero != 0:
    numero = int(input("Digite um numero:"))
    if numero != 0:
        if numero % 2 == 0:
            quant_par += 1
        else:
            quant_impar += 1
print("Foram digitados {} numeros PARES e {} numeros IMPARES!".format(quant_par, quant_impar))
print("\nFim do Programa!\n")
