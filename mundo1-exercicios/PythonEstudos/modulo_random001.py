#Professor escolhe aleatoriamente um dos quatros alunos para apagar o quadro#
#foi utilizado a biblioteca 'random' e a funcionalidade 'choice(parametro)' dessa biblioteca#

#'choice(parametro) seleciona aleatoriamente 1 itein presente dentro do parametro passado no choice'#


import random

a1 = str(input('Digite o valor do Primeiro Aluno:'))
#print(a1)
a2 = str(input('Digite o valor do Segundo Aluno:'))
#print(a2)
a3 = str(input('Digite o valor do Terceiro Aluno:'))
#print(a3)
a4 = str(input('Digite o valor do Quarto Aluno:'))
#print(a4)

alunos = [a1, a2, a3, a4]
escolha = random.choice(alunos)
print('O aluno {} foi escolhido para apagar o quadro!'.format(escolha))
