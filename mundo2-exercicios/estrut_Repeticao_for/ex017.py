#script que lÊ nome, idade, genero de 4 pessoas e informa:
# 1-Nome do Homem mais velho entre as 4 pessoas
# 2- A média da idade do grupo
# 3- Quantas mulheres tem idade < 21 anos#

nome = 0

idade_homem = 0

quant_mulheres = 0

media = 0

for pessoa in range(0, 5, 1):
    nome = str(input("\nQual é o seu nome?")).capitalize()
    idade = int(input("Quantos anos você tem?"))
    genero = str(input("Qual é o seu Genero(M/F)?")).upper()
    media += idade
    if genero == "MASCULINO":
        # armazena a idade do Homem mais velho dentre os 4 inputs do loop, mexendo na
        # variável Global 'idade_homem' e manipulando seu valor interno
        if idade > idade_homem:
            idade_homem = idade
        else:
            # caso a idade do homem seguinte for menor comparado a idade anterior inserida
            # o sistema apenas vai ignorá-la e passar por ela.
            pass
    elif genero == "FEMININO":
        # abstraindo o objetivo de nosso sistema, contabilizar o numero de mulheres que
        # tem < que 21 anos de idade dentre os 4 inputs do laço FOR#
        if idade <= 21:
            quant_mulheres += 1
        else:
            # caso a mulher tenha mais que 21 anos, apenas vamos ignora-la, pois não
            # segue o objetivo do programa, o sistema simplesmente vai passar por ela.#
            pass
    else:
        print("Erro No Genero!")
        break
print("\n{:.1f} é a média de idade entre essas pessoas!".format(media/5))
print("{} é o homem de maior idade, tendo {} anos!".format(nome, idade_homem))
print("{} é o numero de Mulheres com menos de 21 anos!".format(quant_mulheres))

print("\nFim do Programa!\n")
