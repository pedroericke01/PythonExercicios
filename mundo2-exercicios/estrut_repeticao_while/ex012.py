# script que lÊ vario numeros digitados pelo usuário até que o usuário digite o numero 999,
# que é a condição de parada desse laço de repetição
# no final, deve ser apresentada a soma de todos os numeros digitados pelo usuário e a
# quantidade dos numeros inseridos, desconsiderando a flag(condição de parada [999])#

print("\n{:*^40}\n".format(" APRENDENDO FLAGS DE PARADA "))
numero = 0
quant_num = 0
soma = 0
while numero != 999:
    numero = int(input("Escolha um numero:"))
    soma += numero
    quant_num += 1
    if numero == 999:
        soma -= numero
        quant_num -= 1
print('''\nForam inseridos ao todo {} numeros
O resultado da soma desses numeros será {}'''.format(quant_num, soma))
print("\nFim do Programa!\n")
