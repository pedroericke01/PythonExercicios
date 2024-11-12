#script que vai repetir o nome do usuário de acordo com o tamanho do seu nome#
#através do laço de repetição for e da estrutura de controle Range() que determina um intervalo
#de controle para o loop#

nome = str(input("Digite seu nome:")).capitalize()

tam_nome = len(nome)
print("Seu nome tem {} caracteres e será repetido {}x".format(tam_nome, tam_nome))

for nome_pessoa in range(tam_nome):
    print(nome)
print("Fim do Programa!")
