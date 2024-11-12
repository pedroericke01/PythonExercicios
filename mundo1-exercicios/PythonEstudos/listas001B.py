def buscarL(k, l, n):
    i = 0
    while i < n:
        if l[i] == k:
            i = i
            i = n + 1
        elif k > n:
            return -1
        else:
            i = i + 1
        return i


lista = list(range(0, 6))

a = int(input('Escolha um numero:'))
print(a)

busca = buscarL(a, lista, len(lista))
if busca != -1:
    print('Item {} encontrado!'.format(a))
else:
    print('Item {} Não encontrado!'.format(a))

print('Fim do programa!')
