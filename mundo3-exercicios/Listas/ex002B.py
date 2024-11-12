# script que através do loop FOR vamos percorrer TODA essa lista e informar o elemento e sua
# respectiva posição nessa estrutura lista, nesse caso, usamos apenas 1 variável de controle
# no loop FOR e ao invés de tratarmos do elemento em si, agora estamo tratando do índice dos
# elementos existentes na estrutura#

numeros = list(range(1, 10+1))
print(f"Lista Original:{numeros}\n")

for elem in range(0, len(numeros)):
    print(f"O numero {numeros[elem]} está no índice {elem} da lista.")
print("\nFim do Programa!")
