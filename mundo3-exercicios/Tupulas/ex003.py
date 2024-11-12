# script que atraves da Tabela do Brasileirão será criada uma tupula com os 20 times selecinados
# e no final, vamos demoar:
# 1-os 5 primeiros Colocados
# 2-os 4 ultimos colocados
# 3-Onde o time Fluminense(ou outro time) se encontra na tupula, considerando seu índice#

'''
1-Palmeiras, 2-Grêmio, 3-Atlético-MG, 4-Flamengo, 5-Botafogo, 6-Bragantino, 7-Fluminense
8-Athletico-PR, 9-Internacional, 10-Fortaleza, 11-São Paulo, 12-Cuiabá, 13-Corinthians
14-Cruzeiro, 15-Vasco, 16-Bahia, 17-Santos, 18-Goiás, 19-Coritiba, 20-América-MG
'''

print("\n{:-^40}\n".format(" TABELA DO BRASILEIRÃO "))

lista_times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino',
               'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo'
               'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco',
               'Bahia', 'Santos', 'Goiás',
                                  'Coritiba', 'América-MG')

print(f"Tupula Base: {lista_times}\n")

print(f"Os 5 Primeiros Colocados foram: {lista_times[0:5]}")

print(f"Os 4 Ultimos Colocados Foram: {lista_times[-4:]}\n")

print(f"Organizando em ordem Alfabética: {sorted(lista_times)}\n")

print(f"O time Fluminense está na posição {lista_times.index('Fluminense')}")

print("\nFim do Programa!")
