#progrema que lê a idade e genero de varias pessoas e para cada pessoa cadastrada o sistema deve perguntar se o usuario deseja continuar ou não, isso é, cadastrar ooutra pessoa ou finalizar o prigrama
# no final de tudo, o sistema deverá mostras:
#[1]- quantas pessoas tem mais de 18 anos,
#[2]-quantos homens foram cadastrados
#[3]-quantas mulheres tem menos de 21 anos

quant_maioridade = quant_homens = quant_mulheres = resposta_usuario = 0
while True:
    print("\n{:=^35}\n".format(" CADASTRANDO PESSOAS "))
    idade = int(input("Quantos anos você tem?"))
    # tratamento para a variável genero, com esse loop asseguramos que o usuario digite apenas
    # os valores MASCULINO ou FEMININO, enquanto o usuario nao digitar esses valores então o
    # sistema vai força-los a inserir tais valores
    genero = str(input("Qual é o seu genero[Masculino/Feminino]")).strip().upper()
    while genero not in "MASCULINOFEMININO":
        genero = str(input("Digite o Genero CORRETO[Masculino/Feminino]:")).strip().upper()
    # após essa validação segura, então poderemos dar continuidade a lófgica do sistema:
    if idade >= 18:
        quant_maioridade += 1
    if genero == "MASCULINO":
        quant_homens += 1
    elif genero == "FEMININO":
        if idade <= 21:
            quant_mulheres += 1
    # tratamento para a variável resposta_usuario, com esse loop vamos assegurar que o usuario
    # possa inserir apenas os valores SIM ou NAO, caso contrário, o sistema vai força-los a inserir
    # tais valores#
    resposta_usuario = str(input("Deseja Continuar[S/N]?")).strip().upper()
    while resposta_usuario not in "SIMNAO":
        resposta_usuario = str(input("Deseja Continuar[S/N]?")).strip().upper()
    # após essa validação acima, poderemos dar continuidade a logica do sistema, onde o ssitema
    # vai continuar ao cadastro de uma nova pessoa ou vai parar sua execução#
    if resposta_usuario == "SIM":
        pass
    elif resposta_usuario == "NAO":
        break
print(f'''\nAo todo {quant_maioridade} pessoas maior de idade foram cadastradas
foram cadastrados {quant_homens} homens 
foram cadastradas {quant_mulheres} mulheres menor de idade''')
print("\nFim do Programa!")
