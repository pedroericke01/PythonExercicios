# programa que simula o funcionamento de um caixa eletrônicoe no inicio pergunta ao usuario
# qual será o valor que vai ser sacado assim, o programa vai informar quantas Cédulas de cada
# valor será entregue (R$50, R$20, R$10, R$1)#
# o programa deve informar quantas cédulas de cada valor deverá ser entregue
# o loop while vai manipular os valores do salario e cédulas existentes no sistema#
print("\n{:=^40}\n".format(" BANCO PES "))

salario = int(input("Quanto Você deseja Sacar?"))
# vamos iniciar com a maior cédula requisitada pelo desafio:
cedula_atual = 50
# permite demostrar o numero de cédulas que serão sacadas do salário do usuário:
total_cedula = 0
# esse será o loop Recursivo que vai permitir de maneira repetitiva e segura executar a
# logica do sistema:
while True:
    # varifica a possibilidade de sacar um numero específico(inteiro) de vezes uma célula
    # especifica, nesse caso, seria a 1°-R$50
    if salario >= cedula_atual:
        salario -= cedula_atual
        total_cedula += 1
    # quando não for mais possivel sacar a célula_atual do valor do usuário, então vamos
    # precisar trocar de cédula, nesse caso seria para a 2° cédula-R$20
    # ex: salario = 110
    #     cedula_atual = 50
    #     50-110=60
    #     50-60=10
    #     50 > 10
    #     então teriamos que mudar de cédula, agora para 3°-R$10#
    else:
        if total_cedula > 0:
            print(f"Foram Sacados {total_cedula} cédulas de R${cedula_atual}")
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        total_cedula = 0
        # quando não houver mais possibilidade para sacar nenhuma cédula do salário do usuario
        # então o loop infinito vai terminar sua execução#
        if salario == 0:
            break
print("\n{:=^40}\n".format(" VOLTE SEMPRE "))
print("\nFim do Programa!")
