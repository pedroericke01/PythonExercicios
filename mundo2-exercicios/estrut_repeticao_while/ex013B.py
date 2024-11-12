# script que permite que o usuário insira varios numeros inteiros pelo teclado e
# no final da execução mostre no final a média entre todos esses valores, tambem informa
# qual foi o maior e o menor numero digitado e no final o programa vai perguntar ao usuario
# se ele deseja inserir novos valores ou não#

print("\n{:+^40}\n".format(" PRATICANDO LOOPS "))

quant_nums = 0
maior = 0
menor = 0
soma = 0
media = 0

resp_usuario = "SIM"
while resp_usuario != "NAO":
    if resp_usuario == "SIM":
        numero = int(input("Escolha um numero:"))
        quant_nums += 1
        soma += numero
        media = (soma/quant_nums)
        if quant_nums == 1:
            maior = numero
            menor = numero
        else:
            if numero >= maior:
                maior = numero
            elif numero <= menor:
                menor = numero
        resp_usuario = str(input("Deseja inserir novos numeros[S/N]?")).upper()
    elif resp_usuario == "NAO":
        break
    else:
        resp_usuario = str(input("Digite a resposta CORRETA[S/N]:")).upper()

print('''\nAo todo foram inseridos {} numeros
O maior numero foi {}
O menor numero foi {}
A media Entre os numeros é {:.1f}'''.format(quant_nums, maior, menor, media))
print("\nFim do Programa!\n")
