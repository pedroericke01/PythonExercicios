#script que cria uma tabuada de acordo com o input do meu usuário
# o laço FOR e os intervalor Range() serão utilizados para facilitar o desenvolvimento do meu
# sistema:#
from time import sleep
print("{:=^40}\n".format(" Aprendendo Tabuadas! "))

numero = int(input("Qual Tabuada você deseja aprender?"))

print("Estruturando a Tabudada de {}...\n".format(numero))
sleep(1)

resultado = 0

for tabuada in range(1, 10+1, 1):
    #essa não será uma variável acumulativa!
    #vai apenas realizar a multiplicação dos numeros e apresentar o resultado na tela
    resultado = (numero*tabuada)
    print("{} x {} = {}".format(numero, tabuada, resultado))
print("\nFim do Programa!")
