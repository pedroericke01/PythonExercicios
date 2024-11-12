matriz_pessoa = []
print(f"Matriz Original:{matriz_pessoa}")
print(f"Tam.Matriz Original:{len(matriz_pessoa)}")

dados_pessoa = list()

resposta_usuario = pesado = leve = 0
while True:
    dados_pessoa.append(str(input("\nNome:")).strip())
    dados_pessoa.append(float(input("Peso[kg]:")))
    dados_pessoa.append(str(input("Genero:")).strip())

    # enviando uma cópia dos dados inseridos pelo usuario para a matriz principal:
    matriz_pessoa.append(dados_pessoa[:])

    # limpando o "registro" dos dados inseridos acima, garantindo que novos dados poderão
    # ser inseridos corretamente:
    dados_pessoa.clear()
    # a partir do tamanho da matriz será possível realizar a abstração 'direta'
    # dos usuarios mais leves e mais pesados cadastrados, no momento de cada cadastro na matriz:
    if len(matriz_pessoa) >= 1:
        if len(matriz_pessoa) == 1:
            pesado = matriz_pessoa[0][1]
            leve = matriz_pessoa[0][1]
        else:
            for elem in matriz_pessoa:
                if elem[1] >= pesado:
                    pesado = elem[1]
                elif elem[1] <= leve:
                    leve = elem[1]

    resposta_usuario = str(input("Deseja Continuar[SIM/NAO]?")).strip().upper()
    while resposta_usuario not in "SIMNAO":
        resposta_usuario = str(input("\nDigite a resposta CORRETA[SIM/NAO]:")).strip().upper()
    if resposta_usuario == "NAO":
        break

print(f"\nMatriz Atualizada:{matriz_pessoa}")
print(f"Foram Cadastrados ao todo {len(matriz_pessoa)} pessoas no sistema.")

# loop que imprime os nomes das pessoas mais leves e mais pesadas, e caso existam duas ou mais
# pessoas com pesos semelhantes aos mais leves e mais pesados, o nome dessas tambem
# serão impressos:
print(f"O maior Peso é de {pesado}kg foi de ", end="")
for peso in matriz_pessoa:
    if peso[1] == pesado:
        print(f"{peso[0]}", end=", ")

print(f"\nO menor peso é de {leve}kg é de ", end="")
for peso in matriz_pessoa:
    if peso[1] == leve:
        print(f"{peso[0]}", end=", ")

print("\nFim!")
