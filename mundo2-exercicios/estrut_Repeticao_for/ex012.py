# script que soma todos os numeros impares no intervalo de 1 a 500
# será possivel desenvolver esse codigo com o laço de repetição FOR e o intervalo Range()
# todos os numeros IMPARES são multiplos de 3#

soma = 0

for num in range(1, 500+1, 2):
    soma += num
print("O resultado da soma dos multiplos de 3 será {}".format(soma))
print("Fim do Programa!")
