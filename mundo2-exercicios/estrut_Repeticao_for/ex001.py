#script que através da estrutura de repetição for vai imprimir o nome do usuário 10 vezes
# na tela#

nome = str(input("Digite seu nome:")).capitalize()

# perseba que a impressão do nome está dentro do escopo para o loop for() que vai repetir
# em um intervalo de 10x

# o comado print("fim do programa") será executado quando o loop finalizar sua execução, ou
# seja 10x#
for nome_pessoa in range(0, 10):
    print(nome)
print("Fim do Programa!")
