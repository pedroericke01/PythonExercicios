# script que através do loop FOR vamos percorrer TODA essa lista e informar o elemento e sua
# respectiva posição nessa estrutura lista, nesse caso, usamos 2 variáveis de controle no
# loop FOR e a função Enumerate()que enumera o elemento e seu respectivo índice na estrutura:

numero = list(range(1, 10+1))
print(f"Lista Original:{numero}\n")

for pos, elem in enumerate(numero):
    print(f"O numero {elem} está no índice {pos} da lista.")
print("\nFim")
