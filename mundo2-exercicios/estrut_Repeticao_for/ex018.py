# script para encontrar uma frase palindromo, isso  é pode ser lida de frente para tras e de
# trás para frente#

frase = str(input("Escreva a frase:")).strip().upper()

# quebrando a frase em palavras, como em uma lista sequencial#
palavras = frase.split()

# juntando a frase e ignorando os espaços em branco nela:#
junt_palavras = "".join(palavras)

# criando variável que vai armazenar o resultado da manipulação dos palindromos, essa será
# Global:
inverso = ""

# len(junt_palavras) - vai informar o tamanho da string da letra,
# -1 = equivale ao numero anterior a primeiro caractere da string
# -1 = informa que vamos realizar a leitura de trás para frente.
# exemplo: 10, 1, -1 (10,9,8,7,5,6,4,3,2,1)#
for letra in range(len(junt_palavras)-1, -1, -1):
    inverso += junt_palavras[letra]
print("Original {}, Invertido {}".format(junt_palavras, inverso))
if inverso == junt_palavras:
    print("Temos um PALINDROMO")
else:
    print("NÃO temos um PALINDROMO")
print("\nFim do Programa!\n")
