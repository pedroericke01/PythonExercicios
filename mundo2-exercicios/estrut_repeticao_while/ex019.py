# programa que simula o funcionamento de um caixa eletrônicoe no inicio pergunta ao usuario
# qual será o valor que vai ser sacado assim, o programa vai informar quantas Cédulas de cada
# valor será entregue (R$50, R$20, R$10, R$1)#
# o programa deve informar quantas cédulas de cada valor deverá ser entregue

# vamos sacar R$110: quantas vezes (inteiro) eu consigo tirar R$50 desse valor?
# 2x(2x50 = 100) 110 - 100 = 10. Agora não conseguimos tirar nenhuma cédula de 50
# desse valor#

# vamos precisar das variáveis Total_cedulas (respectiva tratadaex:50)
# então vamos tentar tirar a cédula respectiva do valor total enquanto se é possível#

salario = 110
cedula_cinquenta = 50
total_cedula = 0
while True:
    if salario >= cedula_cinquenta:
        salario -= cedula_cinquenta
        total_cedula += 1
    else:
        print("Saldo Atual {}".format(salario))
        break
print(f"Foram sacados {total_cedula} cédulas de R$50")
