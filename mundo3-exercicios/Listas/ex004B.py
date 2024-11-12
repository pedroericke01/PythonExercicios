# script que permite o usuario inserir varios numeros inteiros ao final da lista e
# tambem vai garantir que o usuario não insira numeros repetidos na lista.
# nessa versão, vamos criar um loop infiniro que estará dependendo da resposta do usuario para
# continuar ou parar sua execução:

# inicializando lista vazia:
lista_nums = list()
# analisando principais informações da lista:
print(f"Lista Original:{lista_nums}")
print(f"Tam.Lista Original:{len(lista_nums)}")

# criando o loop infinito que vai manipular os dados da lista e dependendo da resposta do usuario
# pode interrompar ou continuar a execução do sistema:
resposta_usuario = 0
while True:
    numero = int(input("\nEscolha um Numero para cadastra-lo na lista:"))
    # loop que garante que o numero inserido pelo usuario não existe, isso é, não será repetido
    # dentro dos elementos da minha lista:
    while numero in lista_nums:
        print("Esse numero Ja existe na lista!")
        numero = int(input("\nEscolha Outro Numero:"))
    # caso o numero que o usuario digitou não seja Repetido, isso é, ele é NOVO, então, será
    # cadastrado corretamente na minha lista e será exibido que foi corretamente cadastrado!
    # assim como será impresso o tamanho atualizado da minha lista para o usuario acompanhar
    # o crescimento da lista:
    lista_nums.append(numero)
    print("Numero Cadastrado!")
    print(f"Tam.Atualizado da Lista:{len(lista_nums)}")

    resposta_usuario = str(input("Deseja Continuar[S/N]?")).upper().strip()
    # loop que garante que a reposta do usuario seja SIM ou NÃO para dar continuidade ou
    # interromper a execução do sistema:
    while resposta_usuario not in "SIMNAO":
        resposta_usuario = str(input("\nDeseja Continuar[SIM/NAO]?")).strip().upper()
    # caso a resposta do usuario seja: nao, então o sistema será interrompido:
    if resposta_usuario == "NAO":
        break

print(f"\nNova Lista:{lista_nums}")
print(f"Tam.Nova Lista:{len(lista_nums)}")

lista_nums.sort()
print(f"Lista Ordenada em Ordem Crescente:{lista_nums}")

print("\nFim do Programa!")
