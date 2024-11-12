# script que vai permitir o usuário ler 6 inputs e somar apenas os inteiros Pares, desconsiderando
# os Impares
# o loop FOR e os intervalos Range() serão utilizados para essa finalidade#

somar = 0

for num in range(0, 6, 1):
    numero = int(input("Insira um numero INTEIRO entre 1 e 10:"))
    if numero % 2 == 0:
        somar += numero
    else:
        pass
print("\nA soma entre os INTEIROS PARES será {}".format(somar))
print("Fim do Programa!")
