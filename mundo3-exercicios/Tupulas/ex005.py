# programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

n1 = int(input("Primeiro Numero:"))
n2 = int(input("Segundo Numero:"))
n3 = int(input("Terceiro Numero:"))
n4 = int(input("Quarto Numero:"))

tupula_numeros = (n1, n2, n3, n4)
print(f"Você digitou os valores {tupula_numeros}")

quant_par = quant_nums = 0
for elem in tupula_numeros:
    if elem == 9:
        quant_nums += 1
    if elem % 2 == 0:
        quant_par += 1
print(f"\nO numero 9 aparece {quant_nums} vezes!")
print(f"O numero 3 está na posição {tupula_numeros.index(3)}")
print(f"Temos ao Todo {quant_par} numeros Pares!")
