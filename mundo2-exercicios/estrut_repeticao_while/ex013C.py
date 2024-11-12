# script que permite que o usuário insira varios numeros inteiros pelo teclado e
# no final da execução mostre no final a média entre todos esses valores, tambem informa
# qual foi o maior e o menor numero digitado e no final o programa vai perguntar ao usuario
# se ele deseja inserir novos valores ou não
# Vol.3#

# variáveis globais do sistema:
media = quant_num = soma = maior = menor = 0

resposta_usuario = "sim".upper()
while resposta_usuario != "nao".upper():
    numero = int(input("Escolha o numero:"))
    soma += numero
    quant_num += 1
    if quant_num == 1:
        maior = numero
        menor = numero
    else:
        if numero >= maior:
            maior = numero
        if numero <= menor:
            menor = numero
        resposta_usuario = str(input("Deseja inserir novos numeros[SIM/NAO]?")).upper()
media = (soma/quant_num)
print('''\nAo todo foram inseridos {} numeros
O maior numero foi {}
O menor numero foi {}
A média entre os numeros será {:.2f}'''.format(quant_num, maior, menor, media))
print("\nFim do Programa!")
