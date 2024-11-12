# script que Com uma Tupula que contem  várias frases, vamos determinar o numero de vogais
# Existentes nessa frase, em toda a tupula m Si#

print(f"\n{' CONTANDO VOGAIS V.1.5 ':=^40}\n")

tupula_frase = tuple(str(input("Escreva sua frase favotira:")).upper().strip())
#print(f"Tupula:{tupula_frase}")
#print(type(tupula_frase))
quant_vogal = 0
for caract in tupula_frase:
    if caract in "AEIOU":
        quant_vogal += 1

print(f"A vogal 'A' se repete {tupula_frase.count('A')} vezes na sua frase!")
print(f"A vogal 'E' se repete {tupula_frase.count('E')} vezes na sua frase!")
print(f"A vogal 'I' se repete {tupula_frase.count('I')} vezes na sua frase!")
print(f"A vogal 'O' se repete {tupula_frase.count('O')} vezes na sua frase!")
print(f"A vogal 'U' se repete {tupula_frase.count('U')} vezes na sua frase!")
print(f"Existem ao todo {quant_vogal} vogais na sua frase!")

print("\nFim do Programa!\n")
