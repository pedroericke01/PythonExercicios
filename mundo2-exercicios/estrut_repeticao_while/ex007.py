# script que faz A tabuada de um numero digitado pelo usuário utilizando a
# estrutura de repetição while:

print("\n{:*^40}\n".format(" APRENDENDO TABUADAS ABC "))

numero = int(input("Escolha o numero:"))

fat_num = numero
while fat_num >= 1:
    if fat_num == numero:
        res_fat = (numero*fat_num)
        print("{}x{} = {}".format(numero, fat_num, res_fat))
        fat_num -= 1
    else:
        res_fat = (numero*fat_num)
        print("{}x{} = {}".format(numero, fat_num, res_fat))
        fat_num -= 1

print("\nFim do Programa!\n")
