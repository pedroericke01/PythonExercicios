#problema:Descobrir o maior numero da lista#
#através do loop 'for', cada indicd maior será armazdenado em uma variável#
#e comparado com o proximo índice dessa lista#

numbs = list(range(0, 10))
i = 0
while i < len(numbs):
    for elem in numbs:
        maior = numbs[0]
        if numbs[elem] > maior:
            maior += 1
            print(maior)
            i += 1
        else:
            print('O maior elemento dessa lista é:{}'.format(maior))
            i = len(numbs) + 1

print('Fim do programa!')
