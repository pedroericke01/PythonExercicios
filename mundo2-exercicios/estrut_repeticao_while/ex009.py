# scriprt que realiza o calculo da progressão aritmética de um numero inteiro,
# a partir de 2 elementos principais: primeiro termo e razão da progressão Aritmética#
print("\n{:=^40}\n".format(" PROGRESSÃO ARITMETICA V.2 "))

primeiro_termo = int(input("Primeiro Termo:"))
razao_progressao = int(input("Razão da Progressão Aritmética:"))

cont_termos = 10
while cont_termos > 0:
    if cont_termos == 10:
        print("\n{}".format(primeiro_termo), end="->")
    else:
        primeiro_termo += razao_progressao
        print("{}".format(primeiro_termo), end="->")
    cont_termos -= 1
print("Acabou!")
print("\nFim do Programa!\n")
