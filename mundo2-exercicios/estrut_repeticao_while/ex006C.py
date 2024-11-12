# script que lê 2 numeros e através de um menu na tela e da escolha de meu usuário nesse menu
# deverá realizar a operação solicitada em cada caso, que são:
# [1]-somar
# [2]-multiplicar
# [3]-maior dentre eles
# [4]-novos numeros
# [5]-finalizar o programa

while True:
    print("\n{:=^35}\n".format(" MENU DE OPÇÕES V.4 "))
    n1 = int(input("Primeiro Numero:"))
    n2 = int(input("Segundo Numero:"))
    print('''\nMenu de Opções:
     [1]-Somar
     [2]-Multiplicar
     [3]-Descobrir o Maior
     [4]-Inseir Novos Numeros
     [5]-Finalizar Programa
     ''')
    escolha_usuario = int(input("Escolha sua opção Acima[1/5]:"))
    while escolha_usuario <= 5:
        if escolha_usuario == 1:
            soma = (n1+n2)
            print(f"O Resultado da Soma será {soma}")
            break
        elif escolha_usuario == 2:
            multiplicar = (n1*n2)
            print(f"O Resultado da Multiplicação Será {multiplicar}")
            break
        elif escolha_usuario == 3:
            if n1 > n2:
                print(f"O Primeiro {n1} é maior que o Segundo {n2}")
            elif n2 > n1:
                print(f"O Segundo {n2} é maior que o Primeiro {n1}")
            else:
                print(f"{n1} e {n2} são iguais")
            break
        elif escolha_usuario == 4:
            print("\n{:=^35}\n".format(" INSIRA NOVOS NUMEROS "))
            n1 = int(input("Primeiro Numero:"))
            n2 = int(input("Segundo Numero:"))
            escolha_usuario = int(input("Escolha sua opção Acima[1/5]:"))
        elif escolha_usuario == 5:
            break
    escolha_usuario = str(input("Deseja Continuar[SIM/NAO]?")).strip().upper()
    if escolha_usuario == "NAO":
        break

print("\nFIM")
