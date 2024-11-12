#Iterando sobre um arquivo#

with open('dados1.txt') as arquivo:
    for listas in arquivo:
        print(listas)
    arquivo.close()
    