def repetir(k, n):
    i = 0
    while i < n:
        print(k)
        i += 1
    if i == n:
        i = n + 1


frase = 'amo comer amoras'

print(frase.split())
repetir('+', 2)

#contagem antiga#
print(frase.count('amo'))
repetir('+', 2)

#nova contagem com abstracao#
for term in frase.split():
    cont = 0
    if term == 'amo':
        cont += 1
        print('contagem correta:{}'.format(cont))
