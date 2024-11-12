# script que lê o Genero de uma pessoa, caso o genero seja diferente de
# masculino ou feminino o programa vai exigir que seja inserido um valor correto

# nas estruturas while, a variável principal que será analisada [não pode conter + de 1 valor]
# essa precisa ter seu valor único, os testes lógicos precisam estar dentro
# do escopo while e tambem ter testes únicos e especificos, não podem ser testes com duplas
# possibilidades exemplo:
# if num == A or B.#

genero = str(input("Insira seu Genero[M/F]:")).upper()
while genero is not None:
    if genero == "MASCULINO":
        print("Parabens, seu genero é {}".format(genero))
        break
    if genero == "FEMININO":
        print("Parabens, seu genero é {}".format(genero))
        break
    else:
        genero = str(input("Digite o genero CORRETO[M/F]:")).upper()
print("Fim do Programa!")
