# script que verifica a respsosta do usuário para continuar ou interromper a execução
# do sistema permitindo em sua execução que o usuário insira um numero inteiro:

resposta = "SIM"
while resposta == "SIM":
    numero = int(input("Escolha um numero:"))
    resposta = str(input("Deseja continuar [S/N]:")).upper()
print("Fim do Programa!")
