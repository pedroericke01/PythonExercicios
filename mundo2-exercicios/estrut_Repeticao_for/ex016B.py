from datetime import *

print("{:+^40}\n".format(" Selecionando Pessoas "))

# armazenando o ano atual:
ano_atual = datetime.today().year

# variáveis ACUMULATIVAS que vão informar o numero de pessoas que alcançaram ou não a
# maioridade:
pess_maior = 0
pess_menor = 0

# variável NÃO ACUMULATIVA que vai armazenar a idade do usuário seguindo cada passada do loop
idade = 0

# variável não acumulativa que vai informar o ano que o usuário ja alcançou ou vai alcançar
# a maioridade:
ano_maioridade = 0

for data in range(0, 7, 1):
    nome = str(input("Qual é o seu nome?")).capitalize()
    data_nascimento = int(input("Em que ano você nasceu?"))
    idade = (ano_atual - data_nascimento)
    ano_maioridade = ano_atual + (18 - idade)
    if idade >= 18:
        pess_maior += 1
        print("Olá {} você tem {} anos, você alcançou a maioridade no ano de {}\n".format(nome, idade,
                                                                                          ano_maioridade))
    else:
        pess_menor += 1
        print("Olá {} você tem {} anos, você vai alcançar a maioridade no ano de {}\n".format(nome, idade,
                                                                                              ano_maioridade))
print("{} Pessoas Alcançaram a Maioridade!".format(pess_maior))
print("{} Pessoas NÃO ALCANÇARAM a maioridade!".format(pess_menor))

print("Fim do Programa!")
