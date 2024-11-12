# contando vogais de uma túpula com várias strings internas, cada string será analisada
# separadamente e corretamente#
palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON",
            "CURSO", "GRATIS", "ESTUDAR", "PRATICAR",
            "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO")
for palavra in palavras:
    print(f"\nNa palavra {palavra} temos ", end="")
    for caract in palavra:
        if caract.upper() in "AEIOU":
            print(f"{caract}", end=' ')
print("\nFim!")
