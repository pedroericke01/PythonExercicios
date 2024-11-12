import math

a = int(input('Digite o valor de A:'))
print(a)
b = int(input('Digite o valor de B:'))
print(b)

#res = math.ceil(a)
#print('O limite máximo de:{} é:{}'.format(a, res))

#res2 = math.floor(a)
#print('O limite mínimo de:{} é:{}'.format(a, res2))

res3 = math.fabs(a / b)
print('A divisão entre:{} e {} == Exato:{:.1f}'.format(a, b, res3))
