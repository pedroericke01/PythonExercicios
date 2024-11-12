# programa que vai ler varios numeros digitados pelo usuario e coloca-los em uma lista
# depois, cria 2 listas extras que vão armazenar os valores pares e impares cada lista individualmente
# ao final, demostra o conteúdo das 3 listas geradas.
# nessa lista não poderá haver numeros repetidos;
# Os numero deverão ser ordenados em ordem CRESCENTE

# inicializando a lista principal:
lista_nums = list()
print(f"Lista Principal:{lista_nums}")
print(f"Tam.Lista Principal:{len(lista_nums)}\n")

# declarando, separadamente e atentamente ao conceito de conexão entre listas e estruturas de
# dados, as listas lista_par e Lista_impar que irão receber os valores par e impares respectivamente
# digitados pelo usuario:
lista_par = list()
lista_impar = list()
# esse loop infinito trata da lista principal, garantindo o posicionamento correto dos novos
# indices na ordem crescente, a não repetição de numeros dentro da lista, e que o usuario insira
# todos os dados corretamente, caso contrário vai força-lo a inserir os dados corretos:#
resposta_usuario = 0
while True:
    numero = int(input("Escolha um numero:"))
    while numero in lista_nums:
        print("Esse numero ja existe na Lista!")
        numero = int(input("\nEscolha Outro numero:"))
    # se a lista principal estiver vazia, ou seja, sem nenhum numero existentee:
    # o numero escolhido pelo usuario será colocado no final dessa lista, caso contrário, será
    # analisada a posição correta para colocar esse numero na lista:
    if len(lista_nums) == 0:
        lista_nums.append(numero)
        print("Numero Cadastrado!")
        print(f"Tam.Lista Nova:{len(lista_nums)}")
    else:
        for elem in range(0, len(lista_nums)):
            # no caso de existir um numero maior que o escolhido pelo usuario dentro da lista,
            # então o sistema vai pegar o índice desse elemento e inserir o novo numero(digitado pelo usuario)
            # na lista, empurrando o elemento MAIOR para á direita:
            if lista_nums[elem] > numero:
                lista_nums.insert(elem, numero)
                print("Numero Cadastrado!")
                print(f"Tam.Lista Nova:{len(lista_nums)}")
                break
            # no caso de o numero escolhido pelo usuario for maior que o ultimo elemento existente na lista
            # então, o numero escolhido pelo usuario será inserido no final da lista:
            elif numero > lista_nums[-1]:
                lista_nums.append(numero)
                print("Numero Cadastrado!")
                print(f"Tam.Lista Nova:{len(lista_nums)}")
                break
    resposta_usuario = str(input("\nDeseja Continuar[S/N]?")).upper().strip()
    while resposta_usuario not in "SIMNAO":
        resposta_usuario = str(input("Digite a resposta CORRETA[S/N]:\n")).upper().strip()
    if resposta_usuario == "NAO":
        break
print(f"\nLista Nova:{lista_nums}")
print(f"Tam.Lista Nova:{len(lista_nums)}")
# após a execução do loop infinito, então será possível percorrer a lista principal ja ordenada
# e apenas separar os inteiros pares dos impares e colocá-los no final das listas PAR e IMPAR:#
for num in range(0, len(lista_nums)):
    if lista_nums[num] % 2 == 0:
        lista_par.append(lista_nums[num])
    else:
        lista_impar.append(lista_nums[num])
print(f"\nLista com elementos PAR:{lista_par}")
print(f"Lista com elementos IMPAR:{lista_impar}")

print("Fim do Programa!\n")
