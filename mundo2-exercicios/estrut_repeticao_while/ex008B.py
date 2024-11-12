# script que faz o calculo do fatorial de um numero inserido pelo usuáŕio, usando o laço
# de repetição com testes lógicos WHILE
# ex: 5! = 4*3*2*1 = x#
resposta_usuario = 0
while True:
    numero = int(input("Você deseja conhecer o Fatorial de qual numero?"))
    for cont in range(numero-1, 0, -1):
        if cont == numero-1:
            print("{}!=".format(numero), end=" ")
        numero *= cont
        print("{} x ".format(cont), end="")
        if cont == 1:
            print(" = {}".format(numero), end="\n")
    resposta_usuario = str(input("Deseja Conhecer o Fatorial de outro numero[SIM/NAO]?")).strip().upper()
    while resposta_usuario not in "SIMNAO":
        resposta_usuario = str(input("Digite a Resposta CORRETA[SIM/NAO]:")).strip().upper()
    if resposta_usuario == "NAO":
        break
print("Fim do Programa!")