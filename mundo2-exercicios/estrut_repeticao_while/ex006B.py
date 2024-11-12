# script que lê 2 numeros e através de um menu na tela e da escolha de meu usuário nesse menu
# deverá realizar a operação solicitada em cada caso, que são:
# [1]-somar
# [2]-multiplicar
# [3]-maior dentre eles
# [4]-novos numeros
# [5]-finalizar o programa

n1 = int(input("Primeiro Numero:"))
n2 = int(input("Segundo Numero:"))

print('''Menu de Opções:
[1]-Somar
[2]-Multiplicar
[3]-Descobrir o maior
[4]-Inserir novos numeros
[5]-Finalizar o Programa''')

resposta_usuario = int(input("Escolha Sua opção Acima[1/5]:"))
while resposta_usuario <= 5:
    if resposta_usuario == 1:
        soma = (n1+n2)
        print(f"O Resultado da Soma será {soma}")
        break
    elif resposta_usuario == 2:
        multiplicacao = (n1*n2)
        print(f"O Resultado da Multiplicação será {multiplicacao}")
        break
    elif resposta_usuario == 3:
        if n1 > n2:
            print(f"O Primeiro {n1} é maior que o Segundo {n2}")
        elif n2 > n1:
            print(f"O Segundo {n2} é Maior que o Primeiro {n1}")
        else:
            print(f"{n1} e {n2} são Iguais")
        break
    elif resposta_usuario == 4:
        print("\n{:+^35}\n".format(" INSIRA NOVOS NUMEROS "))
        n1 = int(input("Primeiro Numero:"))
        n2 = int(input("Segundo Numero:"))
        resposta_usuario = int(input("Escolha uma das opções Acima[1/5]:"))
    elif resposta_usuario == 5:
        print("Finalizando o Programa...")
        break
print("\nFim do Programa!")
