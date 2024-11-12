# programa que permite ao usuario digitar 7 numeros inteiros e inseri-los em uma lista única
# que manterá os valores pares e impares separados:#

matriz_nums = []
print(f"Matriz Principal:{matriz_nums}")
print(f"Tam.Matriz:{len(matriz_nums)}\n")

lista_nums = list()

lista_par = list()
lista_impar = list()

for elem in range(0, 7):
    lista_nums.append(int(input("Escolha um numero:")))
    # com base no almento de tamanho da lista que vai receber os inputs do usuario, podemos
    # executar as validações de dados em cada iteração individualmente:
    if len(lista_nums) >= 1:
        # loop que vai percorrer a lista_nums, com o numero inserido acima e vamos analisar
        # esse numero com 2 parametros base: se é par ou impar!
        for num in range(0, len(lista_nums)):
            if lista_nums[num] % 2 == 0:
                lista_par.append(lista_nums[num])
            else:
                lista_impar.append(lista_nums[num])
        # limpando a lista que recebeu o numero inserido pelo usuario, após posicioná-lo
        # na respectiva lista de PAR ou IMPAR:
        lista_nums.clear()
    # ao chegarmos a ultima iteração válida do sistema, podemos criar cópias dos valores
    # PAR e IMPAR e coloca-los na matriz principal do sistema:
    if elem == 6:
        lista_par.sort()
        matriz_nums.append(lista_par[:])
        lista_impar.sort()
        matriz_nums.append(lista_impar[:])
        # limpando ambas as listas PAR e IMPAR garantindo que não haja desperdício de memória
        # na execução do sistema:
        lista_par.clear()
        lista_impar.clear()

print(f"Matriz Atualizada:{matriz_nums}")
print(f"Tam.Matriz Atualizada:{len(matriz_nums)}\n")
