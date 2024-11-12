#progrema que lê a idade e genero de varias pessoas e para cada pessoa cadastrada o sistema deve perguntar se o usuario deseja continuar ou não, isso é, cadastrar ooutra pessoa ou finalizar o prigrama
# no final de tudo, o sistema deverá mostras:
#[1]- quantas pessoas tem mais de 18 anos,
#[2]-quantos homens foram cadastrados
#[3]-quantas mulheres tem menos de 21 anos

print("\n{:=^40}\n".format(" FORMULARIO VOL.2 "))

quant_maioridade = quant_homens = quant_mulheres = resp_usuario = quant_pessoa = 0
while True:
    idade = int(input("Quantos anos você tem?"))
    genero = str(input("Qual é o seu genero[M/F]?")).upper()
    quant_pessoa += 1
    if idade >= 18:
        quant_maioridade += 1
    if genero == "MASCULINO":
        quant_homens += 1
    elif genero == "FEMININO":
        if idade <= 20:
            quant_mulheres += 1
    else:
        genero = str(input("Digite o genero CORRETO[M/F]:")).upper()
    resp_usuario = str(input("Deseja Continuar?")).upper()
    if resp_usuario == "SIM":
        pass
    elif resp_usuario == "NAO":
        break
    else:
        resp_usuario = str(input("Deseja Continuar?")).upper()

print('''\nAo todo foi cadastrado {} pessoas
Temos {} pessoas Maior de idade.
Foram cadastrados {} Homens.
Foram cadastradas {} mulheres Menor de idade.'''.format(quant_pessoa, quant_maioridade, quant_homens, quant_mulheres))
print("\nFim do Programa!")
