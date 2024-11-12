# script que fará a contagem Regressiva para O ano novo, contando de 10 a 0, com intervalo de
# tempo de 1s para cada contagem
# vamos utilizar o laço de repetição FOR e o intervalo Range() de 10 a 0
# tambe vamos utilizar a biblioteca Time e o metodo Sleep() para esse fim#

from time import sleep

print("{:=^40}\n".format(" Ano Novo "))

nome = str(input("Digite seu nome:")).capitalize()

print("\nIniciando Contagem Regressiva...\n")
sleep(1)

for segundos in range(10, 0, -1):
    print("Contagem Regressiva {}".format(segundos))
    sleep(1)
print("\nFeliz Ano Novo {}!".format(nome))
print("Fim do Programa!")
