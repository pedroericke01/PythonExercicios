# script que permite que o usuário insira varios numeros inteiros pelo teclado e
# no final da execução mostre no final a média entre todos esses valores, tambem informa
# qual foi o maior e o menor numero digitado e no final o programa vai perguntar ao usuario
# se ele deseja inserir novos valores ou não#
print("\n{:+^40}\n".format(" APRENDENDO LOOPS "))
# variáveis globais que serão terão seus valores manipulados no laço de repetição while:
quant_nums = 0
soma = 0
maior = 0
menor = 0
media = 0

resp_usuario = "SIM"
while resp_usuario != "NAO":
    # inicialmente o programa a resp_usuário começa com o sim, então será possível inserir
    # numeros
    if resp_usuario == "SIM":
        numero = int(input("Escolha um numero:"))
        soma += numero
        quant_nums += 1
        # caso seja a primeira interação do loop no sistema, ou seja, o usuário insira o primeiro
        # numero existente e válido no sistema então vamos fazer esse teste:#
        if quant_nums == 1:
            # o valor do primeiro numero inserido será atribbuído as variáveis de maior e menor
            # numero existente no sistema, pois antes do sistema começar, não haviam numeros
            # validos para a analise correta#
            maior = numero
            menor = numero
        else:  # caso seja a 2° ou 100° interação do sistema, vamos avancar com as analises de maior
               # e menor numeros válidos no sistema
               # caso o novo numero digitado pelo usuário seja maior ou igual ao maior numero
               # inserido anteriormente, a variável "maior" será atualizada#
            if numero >= maior:
                maior = numero
            # ou caso o novo numero inserido pelo usuário seja menor que o numero presente na
            # variável "menor" então essa mesma que será atualizada.#
            elif numero <= menor:
                menor = numero
        # para que eu consiga media a média dos numeros, eu preciso no mínimo de 2 numeros
        # inteiros, por isso, na 2° iteração do loop, que permite inserir um novo numero no
        # meu sistema, que eu vou utilizar a variáel média e perguntar ao usuário se ele
        # deseja inserir algum novo numero ou finalizar de vez o prigrama#
        if quant_nums >= 2:
            media = (soma/quant_nums)
            resp_usuario = str(input("Deseja inserir novos numeros?[SIM/NAO]")).upper()
    # caso a resposta do usuário seja não, ou seja a 2° opção VALIDA para a segurança do
    # meu sistema, então vamos finalizar o programa de vez#
    elif resp_usuario == "NAO":
        break
    # caso a resposta do usuário não seja nem a 1° ou 2° opção VALIDA então o usuário será
    # forçado a inserir o valor CORRETO exigido pelo sistema#
    else:
        resp_usuario = str(input("Insira a resposta CORRETA[SIM/NAO]:")).upper()

print('''\nAo todo foram inseridos {} numeros
O maior numero foi {}
O menor numero foi {}
A media Entre os numeros será {:.1f}'''.format(quant_nums, maior, menor, media))

print("\nFim do Programa!\n")
