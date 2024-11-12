#script que vai somar TODOS os inteiros dados como input pelo usuário no sistema, serão no total
# 6 inputs para esse fim. vamos utilizar o laco de repetição FOR e os intervalos Range()#

somar = 0

for num in range(0, 6, 1):
    numero = int(input("Insira um numero INTEIRO entre 1 e 10:"))
    somar += numero
print("A soma dos INTEIROS será {}".format(somar))
print("Fim do Programa!")
