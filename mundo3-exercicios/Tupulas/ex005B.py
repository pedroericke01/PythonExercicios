
# programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

n1 = int(input("Primeiro Numero:"))
n2 = int(input("Segundo Numero:"))
n3 = int(input("Terceiro Numero:"))
n4 = int(input("Quarto Numero:"))

tupula_numeros = (n1, n2, n3, n4)
quant_par = 0
for elem in tupula_numeros:
    if elem % 2 == 0:
        quant_par += 1
print(f"\nVocê digitou os numeros: {tupula_numeros}")
print(f"O numero 9 aparece {tupula_numeros.count(9)} vezes!")
print(f"O numero 3 está na posição {tupula_numeros .index(3)} da tupula")
print(f"Temos Ao todo {quant_par} numeros Pares!")
print("\nFim do Programa!")
