# programa que vai ler varios numeros digitados pelo usuario e coloca-los em uma lista
# depois, cria 2 listas extras que vão armazenar os valores pares e impares cada lista individualmente
# ao final, demostra o conteúdo das 3 listas geradas.#
# ex:LISTA ORIGINAL:[1,2,3,4,5]
# LISTA PARES: [2,4]
# LISTA IMPAR: [1,3,5]#

# inicilizando a lista original:
lista_nums = list()
print(f"Lista Original:{lista_nums}")
print(f"Tam.Lista Original:{len(lista_nums)}")

# inicializando as lista de numeros Par e impar respectivamente, que serão variáveis
# Globais no sistema, lembre-se do conceito de conexão entre listas e estruturas de dados,
# em uma declaração como exemplo: lista_par = lista_impar = list(), estaremos inicializando 2
# listas com conexão de memória entre elas, e o conceito de conexão de listas afirma que:
# "o que acontece em uma tambem vai acontecer na outra"!#
lista_par = list()
lista_impar = list()

resposta_usuario = 0
while True:
    numero = int(input("\nEscolha um numero:"))
    while numero in lista_nums:
        print("Esse numero ja existe na lista!")
        numero = int(input("\nEscolha outro numero:"))
    lista_nums.append(numero)
    print("Numero Cadastrado!")
    print(f"Tam.Nova Lista:{len(lista_nums)}")
    resposta_usuario = str(input("\nDeseja Continuar[S/N]?")).strip().upper()
    while resposta_usuario not in "SIMNAO":
        resposta_usuario = str(input("\nDigite a Resposta CORRETA[S/N]")).strip().upper()
    if resposta_usuario == "NAO":
        break
print(f"\nLista Nova:{lista_nums}")

for elem in range(0, len(lista_nums)):
    if lista_nums[elem] % 2 == 0:
        lista_par.append(lista_nums[elem])
    else:
        lista_impar.append(lista_nums[elem])
print(f"Lista com Elementos PAR:{lista_par}")
print(f"Lista com elementos IMPAR:{lista_impar}")

print("\nFim do Programa!")
