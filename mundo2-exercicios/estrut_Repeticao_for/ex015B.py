#script que lê o 1° e 2° termos da sequencia numerica e determina-ra
# que a razão dessa progressão tambem vai permitir descobrir o valor de um termo específico
# nessa sequencia de termos#

primeiro_termo = int(input("Digite o Valor do Primeiro Termo:"))
segundo_termo = int(input("Digite o Valor do Segundo Termo:"))

# declarando variáveis globais, essas podem ter o seu valor modificado pelas funções existentes
# no sistema, isso é seu valor pode ser tocado e alterado a qualquer momento. Nesse caso,
# foi modificado pela estrutura condicional IF, Else
razao_prog = 0

if primeiro_termo > segundo_termo:
    razao_prog = (primeiro_termo-segundo_termo)
else:
    razao_prog = (segundo_termo - primeiro_termo)

# podemos ver o valor da variável "razao_porg" alterado pela função acima:
print("A razão dessa Prograssão Aritmética será {}".format(razao_prog))

busca_termo = int(input("Qual Termo Você deseja Pesquisar?"))
# formula para identificar o valor de um termo em específico na sequenca numerica:
# an = a1 + (n - 1) . r ##

val_termo = (primeiro_termo + (busca_termo - 1)) * razao_prog
print("O termo {} corresponde á {}".format(busca_termo, val_termo - 1))

print("Fim do Programa!")
