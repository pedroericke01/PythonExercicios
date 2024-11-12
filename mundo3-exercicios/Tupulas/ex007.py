# script que Com uma Tupula que contem  várias frases, vamos determinar o numero de vogais
# Existentes nessa frase, em toda a tupula em Si#
print(f"\n{'CONTANDO VOGAIS V.1.0':=^45}\n")

frase = tuple(str(input("Escreva sua frase favorita:")).upper().strip())
print(f"Tupula:{frase}")

print(f"-"*45)

print(f"A vogal 'A' se repete {frase.count('A')} vezes na sua frase!")
print(f"A Vogal 'E' se repete {frase.count('E')} vezes na sua frase!")
print(f"A vogal 'I' se repete {frase.count('I')} vezes na sua frase!")
print(f"A vogal 'O' se repete {frase.count('O')} vezes na sua frase!")
print(f"A vogal 'U' se repete {frase.count('U')} vezes na sua frase!")

print("-"*45)

print("\nFim do Programa!\n")
