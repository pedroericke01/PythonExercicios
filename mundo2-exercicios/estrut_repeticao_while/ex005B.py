from random import choice

print("\n{:+^40}\n".format(" PENSANDO EM NUMEROS V.2 "))

lista_nums = list(range(1, 10+1))
escolha_sistema = int(choice(lista_nums))
print("Pensei em um numero, tente descobrir qual...\n")

quant_tentativas = 0
escolha_usuario = 0
while escolha_usuario != escolha_sistema:
    escolha_usuario = int(input("Escolha um numero[1/10]:"))
    if escolha_usuario != escolha_sistema:
        quant_tentativas += 1
        print("Errou, tente de novo!")
        print("Quantidade de tentativas:{}\n".format(quant_tentativas))
        if quant_tentativas == 5:
            print("Você chegou ao Limite de tentativas {}\n".format(quant_tentativas))
            break
    else:
        quant_tentativas += 1
        print("Você Acertou, o numero escolhido foi {}".format(escolha_sistema))

print('''\nVocê fez {} Tentativas!
O numero escolhido foi {}'''.format(quant_tentativas, escolha_sistema))
print("Fim do Programa!\n")
