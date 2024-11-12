# script que mostra a Tabuada De cada numero digitado pelo usuário, um de cada vez
# e no final pergunta se ele deseja ver mais alguma tabuada
# esse loop INFINITO termina quando o usuario digitar um numero negativo, isso é menor que zero
print("\n{:+^40}\n".format(" TABUADAS Vol.4 "))
# foi ultilizado um while FINITO dentro de um while INFINITO#
while True:
    numero = int(input("Qual Tabuada você deseja aprender?"))
    if numero <= 0:
        print("\nPrograma Tabuada Vol.4 ENCERRADO!")
        break
    else:
        contador = 1
        resultado = 0
        print("{:-^35}".format("-"))
        while contador <= 10:
            resultado = (numero*contador)
            print("{}x{}={}".format(numero, contador, resultado))
            contador += 1
    print("{:-^35}".format("-"))
print("\nFim do Programa!")
