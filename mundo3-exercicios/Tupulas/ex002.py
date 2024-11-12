# script que tem uma tupula com numeros de 0 a 20, escrito por extensso, o programa deverá
# receber a entrada do usuario e verificar se esse numero existe ou não na tupula:#

numeros = ("zero", "um", "dois", 'tres', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez','onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
# esse loop vai assegurar que o o usuário digite um numero inteiro possitivo ou seja
# > 0 e que seja menor
# que vinte(< 20), caso contrário, vai forçar o usuario a inserir o numero entre 0 e 20:#
numero_usuario = int(input("Escolha um numero[0/20]:"))
while numero_usuario < 0 or numero_usuario > 20:
    numero_usuario = int(input("Escolha o numero CORRETO[0/20]:"))
# loop que garante que seguindo o numero digitado pelo usuario vamos imprimir o elemento
# correto da tupula, ou seja, vamos imprimir o elemento da tupula que aponta possui o índice
# representado pelo numero escolhido pelo usuario:
for contador in range(0, len(numeros)):
    if contador == numero_usuario:
        print(f"Você escolheu o numero {numeros[contador]}")
print("\nFim")
