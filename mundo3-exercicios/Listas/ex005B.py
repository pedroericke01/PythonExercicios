# script que permite ao usuario inserir varios numeros inteiros e cadastrá-los em uma lista.
# em sua posição/indice correto de inserção, sem usar o método Sort() para esse fim.
# todo esse sistema estará dependendo da resposta do usuario, não poderá haver numeros repetidos,
# caso o usuario não corrija a escolha para colocar um novo numero 3 vezes, então o sistema será
# Interrompido:
# no final, deverá mostrar a lista ordenada na tela sem o uso do método Sort() ou Sorted()#

# inicializando a lista vazia:
lista_nums = list()
# verificando informações principais da lista:
print(f"Lista Original:{lista_nums}")
print(f"Tam.Lista Original:{len(lista_nums)}")

resposta_usuario = 0
while True:
    numero = int(input("Escolha um numero:"))
    while numero in lista_nums:
        print("Esse numero ja Existe na Lista")
        numero = int(input("Escolhah OUTRO numero:"))
    if len(lista_nums) == 0:
        lista_nums.append(numero)
    elif len(lista_nums) >= 1:
        for elem in range(0, len(lista_nums)):
            if lista_nums[elem] > numero:
                lista_nums.insert(elem, numero)
                break
            elif numero > lista_nums[-1]:
                lista_nums.append(numero)
                break
        print(f"Lista Nova:{lista_nums}")
        print(f"Tam.Lista Nova:{len(lista_nums)}")
    resposta_usuario = str(input("Deseja Continuar[S/N]?")).upper().strip()
    while resposta_usuario not in "SIMNAO":
        resposta_usuario = str(input("Deseja Continuar[S/N]?")).upper().strip()
    if resposta_usuario == "NAO":
        break
print("Fim do Programa!")
