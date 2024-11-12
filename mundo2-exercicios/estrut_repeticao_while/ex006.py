# script que lê 2 numeros e através de um menu na tela e da escolha de meu usuário nesse menu
# deverá realizar a operação solicitada em cada caso, que são:
# [1]-somar
# [2]-multiplicar
# [3]-maior dentre eles
# [4]-novos numeros
# [5]-finalizar o programa

print("\n{:+^40}\n".format(" APRIMORANDO MENU DE OPÇÕES "))

n1 = int(input("Escolha o Primeiro numero:"))
n2 = int(input("Escolha o Segundo numero:"))


print('''\nMenu de Opções:
 [1]-Somar
 [2]-Multiplicar
 [3]-Descobrir o Maior
 [4]-Inserir novos numeros
 [5]-Finalizar Programa\n''')

escolha_usuario = int(input("Escolha uma das opções ACIMA:"))
while escolha_usuario != 5:
    if escolha_usuario == 1:
        somar = (n1+n2)
        print("O resultado da Soma será {}".format(somar))
        break
    elif escolha_usuario == 2:
        multiplicar = (n1*n2)
        print("O resultado da Multiplicação será {}".format(multiplicar))
        break
    elif escolha_usuario == 3:
        if n1 > n2:
            print("O Primeiro Numero é Maior!")
            break
        elif n1 < n2:
            print("O Segundo Numero é maior!")
            break
        else:
            print("Ambos os numeros são iguais!")
            break
    elif escolha_usuario == 4:
        n1 = int(input("\nEscolha o Primeiro numero:"))
        n2 = int(input("Escolha o Segundo numero:"))
        # reativando o loop desde o inicio pois o conteúdo da variável "ecolha_usuário" foi
        # modificado e toda essa logica do sistema está intimamente ligada a ela.
        escolha_usuario = int(input("Escolha uma das opções ACIMA:"))
    else:
        break
print("Fim do Programa!")
