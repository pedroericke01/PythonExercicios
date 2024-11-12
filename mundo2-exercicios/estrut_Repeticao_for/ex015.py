# script que Lê o 1°Termo de um Progressão Aritmética e a Razão dessa Progressão.
# Após isso o programa vai determinar os 10 primeiros Termos dessa Sequencia numérica

from time import sleep

print("\n{:=^40}\n".format(" Progressaõ Aritmética "))

primeiro_termo = int(input("Digite o Valor do Primeiro Termo:"))

razao_prog = int(input("Qual será a RAZÃO dessa Progressão Aritmética?"))

print("\nAnalisando...\n")
sleep(1)

for num in range(0, 10+1, 1):
    if num == 0:
        print(primeiro_termo, end="->")
    elif num == 10:
        print("ACABOU", end=" ")
    else:
        primeiro_termo += razao_prog
        print(primeiro_termo, end="->")
print("\nFim do Programa!")
