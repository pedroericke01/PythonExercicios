#script que o computador vai escolher um numero entre 0 a 10 e o usuário vai tentar
# insistentemente acertar o numero escolhido pelo usuário
# o usuario possui o limite de 5 tentativas para acertar

from random import randint

print("\n{:=^45}\n".format(" DESCUBRA O NUMERO V.3 "))

escolha_maquina = randint(1, 10)
print("Pensei em um numero, tente descobrir qual...\n")

quant_tentativas = escolha_usuario = 0
limite_tentativas = 5

while escolha_usuario != escolha_maquina:
    escolha_usuario = int(input("Tente descobrir o numero:"))
    if escolha_usuario == escolha_maquina:
        print("Parabens, você venceu!")
        break
    print("Errou!")
    quant_tentativas += 1
    limite_tentativas -= 1
    print(f"Tentativas Disponíveis:{limite_tentativas}")
    print("="*45)
    if limite_tentativas == 0:
        print("Você alcançou o limite máximo de tentativas!")
        break
print("\nFim do Programa!")
