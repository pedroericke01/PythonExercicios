# script que melhora a Progressaõ Aritmetica permitindo que o usuário digite se ele deseja
# mostrar mais algum termo > 10 (maior que os 10 anteriores)#

print("\n{:=^40}\n".format(" PROGRESSAO ARITMÉTICA V.3 "))

primeiro_termo = int(input("Primeiro Termo:"))
razao_progressao = int(input("Razão da Progressão Aritmética:"))

interacao_usuario = 0

quant_termos = 10
while quant_termos >= 1:
    if quant_termos == 10:
        print("\n{}".format(primeiro_termo), end="->")
        quant_termos -= 1
    else:
        primeiro_termo += razao_progressao
        print("{}".format(primeiro_termo), end="->")
        quant_termos -= 1
    if quant_termos == 1:
        print("ACABOU!\n")
        interacao_usuario = int(input("Quantos Termos Você deseja ver a mais?"))
        if interacao_usuario > 0:
            quant_termos += interacao_usuario
        else:
            break
print("Fim do Programa!")
