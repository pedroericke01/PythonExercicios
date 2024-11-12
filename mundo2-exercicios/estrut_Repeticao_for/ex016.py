# script que recebe o ano de nascimento de 8 pessoas e verifica quantas ja
# são de maioridade(idade>18) e quantas sãos de menor idade(idade<18)

print("{:=^40}\n".format(" Selecionando Pessoas "))

pes_maioridade = 0
pes_menoridade = 0

for dado in range(0, 7, 1):
    idade = int(input("Quantos anos você tem?"))
    if idade >= 18:
        pes_maioridade += 1
    else:
        pes_menoridade += 1
print("\n{} Pessoas Alcançaram a Maioridade!".format(pes_maioridade))
print("{} Pessoas são de Menor Idade!".format(pes_menoridade))

print("\nFim do Programa!")
