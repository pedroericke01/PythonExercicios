# script que através do input do usuário vai iniciar um loop de contagem em um intervalo de
# N a 0 em ordem DECRESCENTE através do laço FOR e do comando Range()#

numero = int(input("Escolha um numero entre 0 a 10:"))

for num in range(numero, 0, -1):
    print(num)
print("Fim do Programa!")
