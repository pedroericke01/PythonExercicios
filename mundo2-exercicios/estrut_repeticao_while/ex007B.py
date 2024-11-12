# script que faz A tabuada de um numero digitado pelo usuário utilizando a
# estrutura de repetição:
# toda tabuada tem um inicio (1) e um fim (10), onde o numero Base da tabuada será multiplicado
# por todos os numeors existentes nesse intervalo#
resposta_usuario = 0
while True:
    print("\n{:+^35}\n".format(" APRENDENDO TABUADAS BASICA"))
    numero = int(input("Qual Tabuada Você deseja aprender?"))
    while numero <= 0:
        numero = int(input("Prefira Aprender tabuadas de numeros Válidos[1/10]:"))
    resultado = 0
    for cont in range(1, 10+1, 1):
        resultado = (numero*cont)
        print("{} x {} = {}".format(numero, cont, resultado))
    resposta_usuario = str(input("Deseja Continuar[SIM/NAO]?")).upper()
    while resposta_usuario not in "SIMNAO":
        resposta_usuario = str(input("Deseja Continuar[SIM/NAO]?")).upper()
    if resposta_usuario == "NAO":
        break
print("\nFim Do Programa!")
