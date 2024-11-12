# script que faz o calculo do fatorial de um numero inserido pelo usuáŕio, usando o laço
# de repetição com testes lógicos WHILE
# ex: 5! = 4*3*2*1 = x#

numero = int(input("Escolha um numero:"))

fat_num = (numero-1)
while fat_num >= 1:
    print("{}x{} = ".format(numero, fat_num), end=" ")
    numero *= fat_num
    print("{}".format(numero))
    fat_num -= 1
print("\nO Fatorial do numero escolhido será {}".format(numero))
print("Fim do Programa!\n")
