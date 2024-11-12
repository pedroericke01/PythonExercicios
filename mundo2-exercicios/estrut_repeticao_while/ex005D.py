#script que o computador vai escolher um numero entre 0 a 10 e o usuário vai tentar
# insistentemente acertar o numero escolhido#

from random import randint

escolha_maquina = randint(1, 10)
print("Pensei em um numero, tente descobrir qual...\n")

quant_tentativas = escolha_usuario = 0
while escolha_usuario != escolha_maquina:
    escolha_usuario = int(input("Descubra o numero:"))
    if escolha_usuario == escolha_maquina:
        print(f"Parabens, você venceu!")
        break
    print("Errou! tente novamente.")
    quant_tentativas += 1
print(f"Você realizou {quant_tentativas} tentativas anteriores para acertar o numero {escolha_usuario}")
