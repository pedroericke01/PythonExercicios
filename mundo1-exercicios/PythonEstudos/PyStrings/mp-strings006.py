#observe o algoritmo desenvolvido para determonar quantas vezes determinada strings se
# repete em um conjunto de strings de um arquivo ou frase.
# Essa busca será feita de maneira Específica:#

frase = 'amo suco de amoras no café da manhã'
quant_term = 0
for termo in frase.split():
    if termo == 'amo':
        quant_term += 1

print('O termo:{}, se repete:{} Vezes.'.format('amo', quant_term))
print('Fim do programa!')
