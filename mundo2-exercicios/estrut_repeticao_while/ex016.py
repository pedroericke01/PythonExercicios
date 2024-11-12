# jogando par ou impar com o computador;
# o loop infinito do jogo será interrompido quando o usuarío perder e
# no final, mostrará o numero de vitorias que o usuario teve;
# o que determina quem ganha ou perde no jogo do impar ou par é o resultado final da
# soma dos numeros escolhidos por cada usuario#

from random import choice
print("{:=^40}".format(" PAR OU IMPAR "))

lista_opcoes = list(range(1, 10+1))
escolha_maquina = choice(lista_opcoes)

resultado = soma = quant_vitorias = 0

while True:
    escolha_numero = int(input("Escolha um numero[1/10]:"))
    escolha_usuario = str(input("Você escolha IMPAR OU PAR?")).upper()
    soma = (escolha_maquina+escolha_numero)
    if soma % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "IMPAR"
    print('Você jogou {} e o computador jogou {}, o total de {} resulta em {}'.format(escolha_numero,
                                                                                      escolha_maquina, soma, resultado))
    if escolha_usuario == resultado:
        print("Você Venceu!")
        quant_vitorias += 1
    else:
        print("Você Perdeu!")
        break
print("\nVocê teve {} Vitórias!".format(quant_vitorias))
print("\nFim do Programa!")
