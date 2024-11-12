# programa que lê o nome e duas notas de varios alunos e coloque-os em uma matriz,
# no final devemos mostrar:
# 1- um boletim contendo id, nome e média de cada aluno;
# 2- permite que o usuario busque por um aluno e suas respectivas informações;

matriz_alunos = []
print(f"Lista Principal:{matriz_alunos}")
print(f"Tam.Matriz:{len(matriz_alunos)}\n")

lista_dados = list()

resposta_usuario = 0
while True:
    lista_dados.append(str(input("\nNome:")).strip().upper())
    lista_dados.append(float(input("Primeiro Bimestre:")))
    lista_dados.append(float(input("Segundo Bimestre:")))

    matriz_alunos.append(lista_dados[:])

    lista_dados.clear()

    resposta_usuario = str(input("Deseja Continuar[SIM/NAO]?")).strip().upper()
    while resposta_usuario not in "SIMNAO":
        print("Resposta Inválida!\n")
        resposta_usuario = str(input("Deseja Continuar[SIM/NAO]?")).strip().upper()
    if resposta_usuario == "NAO":
        break

print("-"*20)

for aluno in range(0, len(matriz_alunos)):
    media = (matriz_alunos[aluno][1] + matriz_alunos[aluno][2]) / 2
    print(f"{aluno} {matriz_alunos[aluno][0]} {media}")

print("-"*20)

escolha_usuario = 0
while escolha_usuario != 999:
    escolha_usuario = int(input("Quer ver as notas de qual aluno(Flag de parada:999)?"))
    for elem in range(0, len(matriz_alunos)):
        if elem == escolha_usuario:
            print(matriz_alunos[elem])
            print("-"*20)
print("\nFim do Programa!")
