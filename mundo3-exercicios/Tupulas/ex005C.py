# programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado numero 3 está na tupula:
#C) Quantos numeros Pares existem na tupula:

numero = (int(input("Primeiro Numero:")),
          int(input("Segundo Numero:")),
          int(input("Terceiro Numero:")),
          int(input("Quarto Numero:")))

tupula_numeros = (numero)
quant_par = 0
for numero in tupula_numeros:
    if numero % 2 == 0:
        quant_par += 1
print(f"Você escolheu os numeros {tupula_numeros}")
print(f"O numero 9 aparece {tupula_numeros.count(9)} vezes!")
print(f"O numero 3 está na posição {tupula_numeros.index(3)} na tupula")
print(f"Temos ao todo {quant_par} numeros Pares na Tupula")
