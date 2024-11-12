#script que vai receber 6 inputs do usuário e todos os INTEIROS IMPARES serão somados
# o laço de repetição FOR e os intervalos Range() serão utilizados para esse fim#

somar = 0

for num in range(0, 6, 1):
    numero = int(input("Insira um numero INTEIRO entre 1 e 10:"))
    if numero % 2 == 0:
        # pass == passar e ignorá-lo, ou seja, não fazer nada!
        pass
    else:
        somar += numero
print("\nA soma dos INTEIROS IMPARES será {}".format(somar))
print("Fim do Programa!")
