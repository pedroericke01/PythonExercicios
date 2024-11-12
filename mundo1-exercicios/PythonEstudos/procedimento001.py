def imprime(k, n):
    i = 0
    while i < n:
        print(k)
        i = i + 1
        if i == n:
            break

chave = str(input('Caracere desejado:'))
print(chave)
vezes = int(input('Quantidade desejada:'))
print(vezes)

imprime(chave, vezes)
imprime('eva', 3)
