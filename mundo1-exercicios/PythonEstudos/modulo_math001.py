import math

num1 = int(input('Digite um numero:'))
raiz = math.sqrt(num1)
print('A rair de:{} é igual á:{}'.format(num1, raiz))

truncamentos = math.trunc(raiz)
print('O trancamento de:{} é igual á:{}'.format(num1, truncamentos))

