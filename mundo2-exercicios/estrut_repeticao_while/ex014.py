# script que lê varios numeros inteiros digitados pelo usuario e no final mostre a
# quantidade de numeros inseridos, a soma entre os numeros
# para que esse loop INFINITO venha acabar, o usuario deve inserir a flag(condicao de parada)
# 999, o resultado da soma e a quantidade de numeros inseridos não vai considerar essa flag
# como um numero válido para essas operações#

quant_num = soma = 0
while True:
    numero = int(input("Escolha um numero:"))
    if numero == 999:
        break
    else:
        quant_num += 1
        soma += numero
print('''\nAo todo foram inseridos {} numeros Válidos
O resultado da soma dos numeros será {}'''.format(quant_num, soma))
print("\nFim do Programa!\n")
