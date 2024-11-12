# utilizando o laço FOR para repetir o somatorio de um numero N vezes de acordo com a entrada
# do usuário
# ulilizamor o laço FOR e os intervalos Range()#

soma = 0

for num in range(0, 4):
    numero = int(input("Escolha um numero entre 1 a 10:"))
    soma += numero
print("O somatório dos numeros será {}".format(soma))
print("Fim do Programa!")
