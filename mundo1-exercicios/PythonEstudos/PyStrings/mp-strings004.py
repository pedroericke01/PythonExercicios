#utilizando o metodo 'count()' para determinar quantas vezes o
# string 'amo' aparece em uma frase, sem o auxilio do metodo 'split()', essa busca pode
# retornar um resultado indesejado. observe:#

frase = 'amo suco de amoras'
print(frase)
print(frase.count('amo'))

#em uma busca válida, esse resultado estaria inválido, pois desejamos apenas o caractere 'amo'
# antes da string 'suco de amoras'.#
#precisamos ser especificos na busca, para a máquina. como seria o processamento:
#" 'amo' comer 'amo'ras "#
#observe a busca correta no proximo scripts(mp-strgs005.py):#