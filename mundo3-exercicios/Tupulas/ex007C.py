print(f"\n{'CONTANDO VOGAIS V.1.8'}\n")
tupula_frase = tuple(str(input("Escreva sua frase favorita:")).upper().strip())
# informa que o tipo do objeto Acima é uma Tupula Válida:
#print(f"Tipo de Objeto {type(tupula_frase)}")
# imprimindo a tupula Acima, de acordo com a entrada do usuário, garantindo:
# caracteres maiúsculos e invalidação para caracteres de espaços vazios no inicio e fim da str
#print(f"Tupula:{tupula_frase}")
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
