#script que o computador vai escolher um numero entre 0 a 10 e o usuário vai tentar
# insistentemente acertar o numero escolhido pelo usuário#

from random import choice

print("\n{:=^40}\n".format(" PENSANDO EM NUMEROS "))

lista_nums = list(range(1, 10+1))
escolha_maquina = choice(lista_nums)
print("Pensei em um numero, tente descobrir.\n")

quant_tentativas = 0
escolha_usuario = 0

while escolha_usuario != escolha_maquina:
    escolha_usuario = int(input("Descubra o numero escolhido:"))
    if escolha_usuario != escolha_maquina:
        quant_tentativas += 1
        print("Você errou, Tente novamente!")
    else:
        print('Você acertou, O numero escolhido foi {}!'.format(escolha_usuario))
print("\nVocê errou {} vezes!".format(quant_tentativas))
print("Fim do Programa!\n")
