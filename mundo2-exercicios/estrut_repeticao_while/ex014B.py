#mudando o tipo de formatação utilizada, de acordo com a do python 3.6+ (print(f"...")#

print("\n{:=^40}\n".format("FLAG DE PARADA 999"))

quant_num = soma = 0
while True:
    numero = int(input("Escolha um numero:"))
    if numero == 999:
        break
    else:
        quant_num += 1
        soma += numero
print(f'''\nAo todo foram inseridos {quant_num} numeros Válidos!
O Resultado da soma entre os numeros será {soma}''')
print("\nFim do Programa\n")
